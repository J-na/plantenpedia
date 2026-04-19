"""
Plantenpedia — Upload CLI

Uploadt verrijkingsdata vanuit data/enrichments/ naar de Supabase database.

Gebruik:
    python data/upload.py                          # Alle planten, alle velden
    python data/upload.py --safe                   # Sla velden over die al ingevuld zijn in de DB
    python data/upload.py --plant "Taxus baccata"  # Één plant bijwerken
    python data/upload.py --category bomen         # Alle planten in een categorie
    python data/upload.py --fields photos,description  # Alleen deze velden bijwerken
    python data/upload.py --dry-run                # Toon wat er bijgewerkt wordt zonder te schrijven

Opties combineren:
    python data/upload.py --plant "Taxus baccata" --fields photos
    python data/upload.py --category wilde_planten --safe

Beschikbare categorieën:
    vaste_planten, eenjarigen, bollen_knollen, kuipplanten,
    wilde_planten, keukenkruiden, grassen, heesters,
    klimplanten, bomen
"""
from __future__ import annotations
import argparse, os, sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ── Supabase verbinding ────────────────────────────────────────────────────────
try:
    import streamlit as st
    _url = st.secrets["supabase"]["url"]
    _key = st.secrets["supabase"].get("service_key", st.secrets["supabase"]["key"])
except Exception:
    _url = os.environ.get("SUPABASE_URL", "")
    _key = os.environ.get("SUPABASE_SERVICE_KEY", os.environ.get("SUPABASE_KEY", ""))

if not _url or not _key:
    print("Stel SUPABASE_URL en SUPABASE_SERVICE_KEY in als omgevingsvariabelen.")
    sys.exit(1)

from supabase import create_client
_client = create_client(_url, _key)

# ── Categorie → module-naam mapping ──────────────────────────────────────────
CATEGORY_TO_FILE = {
    "vaste_plant":           "vaste_planten",
    "vaste_planten":         "vaste_planten",
    "eenjarige":             "eenjarigen",
    "tweejarige":            "eenjarigen",
    "eenjarigen":            "eenjarigen",
    "bol_knol":              "bollen_knollen",
    "bollen_knollen":        "bollen_knollen",
    "kuipplant":             "kuipplanten",
    "kuipplanten":           "kuipplanten",
    "wilde_plant":           "wilde_planten",
    "waterplant":            "wilde_planten",
    "wilde_planten":         "wilde_planten",
    "keukenkruid":           "keukenkruiden",
    "keukenkruiden":         "keukenkruiden",
    "gras":                  "grassen",
    "grassen":               "grassen",
    "heester":               "heesters",
    "wintergroene_heester":  "heesters",
    "heesters":              "heesters",
    "boom":                  "bomen",
    "conifeer":              "bomen",
    "bomen":                 "bomen",
    "klimplant":             "klimplanten",
    "roos":                  "klimplanten",
    "klimplanten":           "klimplanten",
}


def load_enrichments(category_filter: str | None = None) -> dict:
    """Laad ENRICHMENTS, optioneel gefilterd op categorie-bestand."""
    if category_filter:
        file_base = CATEGORY_TO_FILE.get(category_filter)
        if not file_base:
            print(f"Onbekende categorie: {category_filter!r}")
            print(f"Geldig: {sorted(set(CATEGORY_TO_FILE.values()))}")
            sys.exit(1)
        mod = __import__(f"data.enrichments.{file_base}", fromlist=["ENRICHMENTS"])
        return mod.ENRICHMENTS
    from data.enrichments import ENRICHMENTS
    return ENRICHMENTS


def fetch_existing_fields(scientific_names: list[str]) -> dict[str, dict]:
    """Haal bestaande DB-waarden op voor de gegeven planten (voor --safe modus)."""
    existing = {}
    # Supabase heeft een limiet van ~100 items per .in_() call
    batch_size = 50
    for i in range(0, len(scientific_names), batch_size):
        batch = scientific_names[i:i + batch_size]
        resp = (
            _client.table("plants")
            .select("*")
            .in_("scientific_name", batch)
            .execute()
        )
        for row in (resp.data or []):
            existing[row["scientific_name"]] = row
    return existing


def filter_payload(data: dict, existing_row: dict | None, fields: list[str] | None, safe: bool) -> dict:
    """
    Bepaal welke velden daadwerkelijk worden gestuurd naar de DB.

    - fields: als opgegeven, stuur alleen deze velden
    - safe:   als True, sla velden over die al een waarde hebben in de DB
    """
    payload = dict(data)

    if fields:
        payload = {k: v for k, v in payload.items() if k in fields or k == "scientific_name"}

    if safe and existing_row:
        # Verwijder velden die al een niet-lege waarde hebben in de DB
        skip = set()
        for k, v in list(payload.items()):
            existing_val = existing_row.get(k)
            if existing_val is not None:
                # Sla leeg of default-waarden niet over
                if isinstance(existing_val, list) and len(existing_val) == 0:
                    continue
                if isinstance(existing_val, str) and existing_val.strip() == "":
                    continue
                skip.add(k)
        if skip:
            payload = {k: v for k, v in payload.items() if k not in skip}

    return payload


def run(args: argparse.Namespace) -> None:
    enrichments = load_enrichments(args.category)

    # Filter op specifieke plant
    if args.plant:
        if args.plant not in enrichments:
            print(f"Plant niet gevonden: {args.plant!r}")
            print("Controleer de spelling (wetenschappelijke naam).")
            sys.exit(1)
        enrichments = {args.plant: enrichments[args.plant]}

    fields = [f.strip() for f in args.fields.split(",")] if args.fields else None

    # In safe-modus: eerst bestaande waarden ophalen
    existing = {}
    if args.safe:
        print(f"--safe: bestaande DB-waarden ophalen voor {len(enrichments)} planten...")
        existing = fetch_existing_fields(list(enrichments.keys()))
        print(f"  {len(existing)} gevonden in DB")

    items = list(enrichments.items())
    print(f"Uploaden: {len(items)} plant(en)" +
          (f" | velden: {fields}" if fields else "") +
          (" | DRY-RUN" if args.dry_run else "") +
          (" | SAFE" if args.safe else ""))

    success = errors = skipped = 0

    for sci_name, data in items:
        data = dict(data)
        data["scientific_name"] = sci_name

        payload = filter_payload(data, existing.get(sci_name), fields, args.safe)

        if not payload or (len(payload) == 1 and "scientific_name" in payload):
            print(f"  – {sci_name} (niets te uploaden)")
            skipped += 1
            continue

        if args.dry_run:
            field_list = ", ".join(k for k in payload if k != "scientific_name")
            print(f"  [DRY] {sci_name}: {field_list}")
            success += 1
            continue

        try:
            _client.table("plants").upsert(payload, on_conflict="scientific_name").execute()
            print(f"  ✓ {sci_name}")
            success += 1
        except Exception as exc:
            print(f"  ✗ {sci_name}: {exc}")
            errors += 1

    print(f"\nKlaar: {success} bijgewerkt, {skipped} overgeslagen, {errors} fouten.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Upload Plantenpedia verrijkingsdata naar Supabase.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--plant", metavar="NAAM",
        help='Wetenschappelijke naam van één plant, bijv. "Taxus baccata"',
    )
    parser.add_argument(
        "--category", metavar="CAT",
        help="Alleen planten uit dit categorie-bestand uploaden",
    )
    parser.add_argument(
        "--fields", metavar="VELD1,VELD2",
        help="Komma-gescheiden lijst van velden om te uploaden (bijv. photos,description)",
    )
    parser.add_argument(
        "--safe", action="store_true",
        help="Sla velden over die al een waarde hebben in de DB (beschermt handmatige aanpassingen)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Toon wat er bijgewerkt zou worden zonder iets te schrijven",
    )
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
