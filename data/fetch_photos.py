"""
Haalt bevestigde Wikimedia Commons bestandsnamen op via de Wikipedia API
en schrijft een bijgewerkte _photos.py.

Gebruik:
    python data/fetch_photos.py [--dry-run]

Vereisten: alleen standaardbibliotheek (urllib, json, re).
"""
from __future__ import annotations
import sys, os, time, json, re, argparse
import urllib.request, urllib.parse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.stdout.reconfigure(encoding="utf-8")

UA = "PlantenpediaPhotoFetcher/1.0 (jonathanmeijers2000@gmail.com)"
PAUSE = 0.3   # seconden tussen API-aanroepen


def api_get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            return json.loads(r.read())
    except Exception as e:
        print(f"    [API-fout] {e}", file=sys.stderr)
        return {}


def extract_filename(thumb_url: str) -> str | None:
    """Haal de Wikimedia Commons bestandsnaam uit een thumb-URL."""
    # Patroon: /commons/thumb/X/XX/BESTAND.ext/NNNpx-BESTAND.ext
    m = re.search(
        r"/commons/(?:thumb/[^/]+/[^/]+/|)([^/]+\.(?:jpg|jpeg|png|JPG|PNG))(?:/\d|$)",
        thumb_url, re.I
    )
    if m:
        return urllib.parse.unquote(m.group(1))
    return None


def batch_wiki_images(names: list[str]) -> dict[str, str]:
    """Hoofdafbeelding (pageimage) per plant via Wikipedia API — batch van max 50."""
    result: dict[str, str] = {}
    # Maak alternatieve zoektitels voor hybridennamen en cultivargroepen
    lookup: dict[str, str] = {}  # wiki-title → originele naam
    for n in names:
        title = n.replace(" ", "_")
        # Hybride: 'x' → '×' (Unicode kruisteken)
        alt = title.replace("_x_", "_×_").replace("_'", "'")
        lookup[alt] = n
        if alt != title:
            lookup[title] = n  # ook originele titel proberen

    titles_str = "|".join(lookup.keys())
    url = (
        "https://en.wikipedia.org/w/api.php?action=query"
        f"&titles={urllib.parse.quote(titles_str)}"
        "&prop=pageimages&pithumbsize=1200&format=json&pilicense=any"
    )
    data = api_get(url)
    redirects = data.get("query", {}).get("redirects", [])
    redirect_map = {r["from"].replace("_", " "): r["to"].replace("_", " ") for r in redirects}

    for page in data.get("query", {}).get("pages", {}).values():
        wiki_title = page.get("title", "").replace("_", " ")
        thumb = page.get("thumbnail", {}).get("source", "")
        if not thumb:
            continue
        fn = extract_filename(thumb)
        if not fn:
            continue
        # Zoek de originele plantnaam terug
        orig = lookup.get(wiki_title.replace(" ", "_"))
        if not orig:
            # Via redirect
            redirected_from = redirect_map.get(wiki_title)
            if redirected_from:
                orig = lookup.get(redirected_from.replace(" ", "_"))
        if not orig:
            orig = wiki_title
        result[orig] = fn
    return result


_FILTER_KEYWORDS = [
    "icon", "flag", "logo", "map", "commons-logo", "question", "stub",
    "wikidata", "edit", "arrow", "sound", "audio", ".svg", "portal",
    "wikimedia", "wikipedia", "p_vip", "red_pencil",
]
# Alleen echte foto-extensies accepteren
_PHOTO_EXTENSIONS = (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG")


def _img_filter(fn: str) -> bool:
    """Geef True als het bestand een bruikbare foto is."""
    low = fn.lower()
    if any(x in low for x in _FILTER_KEYWORDS):
        return False
    # Alleen foto-bestanden (geen PDF, DJVU, OGG, etc.)
    if not any(low.endswith(ext.lower()) for ext in _PHOTO_EXTENSIONS):
        return False
    return True


def wiki_article_images(name: str) -> list[str]:
    """Alle afbeeldingen die in het Wikipedia-artikel voorkomen (bevestigd bestaand).
    Probeert ook Unicode-hybrideteken en vereenvoudigde naam als fallback.
    """
    candidates = [
        name.replace(" ", "_"),
        name.replace(" x ", " × ").replace(" ", "_"),
        name.split()[0],  # genus-only als laatste redmiddel
    ]
    for title_raw in dict.fromkeys(candidates):  # deduplicate, order-preserving
        title = urllib.parse.quote(title_raw)
        url = (
            "https://en.wikipedia.org/w/api.php?action=query"
            f"&titles={title}"
            "&prop=images&imlimit=25&format=json"
        )
        data = api_get(url)
        filenames: list[str] = []
        for page in data.get("query", {}).get("pages", {}).values():
            if page.get("pageid", -1) == -1:
                continue  # artikel bestaat niet
            for img in page.get("images", []):
                t = img.get("title", "")
                if t.startswith("File:") and _img_filter(t[5:]):
                    filenames.append(t[5:])
        if filenames:
            return filenames
    return []


def commons_search(plant_name: str, limit: int = 6) -> list[str]:
    """Zoek in Wikimedia Commons als Wikipedia geen afbeeldingen geeft."""
    q = urllib.parse.quote(plant_name)
    url = (
        "https://commons.wikimedia.org/w/api.php?action=query"
        f"&list=search&srsearch={q}&srnamespace=6&srlimit={limit}&format=json"
    )
    data = api_get(url)
    files: list[str] = []
    for r in data.get("query", {}).get("search", []):
        t = r.get("title", "")
        if t.startswith("File:") and _img_filter(t[5:]):
            files.append(t[5:])
    return files


def classify_filename(fn: str, plant_name: str) -> str:
    """Schat het fototype op basis van de bestandsnaam."""
    low = fn.lower()
    if any(x in low for x in ["fruit", "berry", "berries", "nut", "seed", "hip",
                               "acorn", "cone", "vrucht", "bes"]):
        return "vrucht"
    if any(x in low for x in ["leaf", "leaves", "blad", "foliage"]):
        return "blad"
    if any(x in low for x in ["flower", "bloom", "blossom", "blüte", "bloem",
                               "fleur", "catkin", "pollen"]):
        return "bloeiwijze"
    if any(x in low for x in ["habit", "habitus", "plant", "tree", "shrub",
                               "growth", "overview", "general"]):
        return "habitus"
    # Generieke nummering: kz01 / 1 / 002 → vermoedelijk habitus
    if re.search(r"[_\-](?:kz)?\d+\.(?:jpg|png)$", low):
        return "habitus"
    return "algemeen"


def pick_photos(main_fn: str | None, extras: list[str], plant_name: str) -> list[dict]:
    """
    Stel een set van 2–3 foto's samen:
      1. Hoofdafbeelding → bloeiwijze (meest informatief voor app)
      2. Extra: liefst 'vrucht' of 'blad'
      3. Extra: habitus of algemeen
    """
    photos: list[dict] = []

    def make(fn: str, type_: str) -> dict:
        encoded = urllib.parse.quote(fn, safe="_-.")
        caption = f"{plant_name.split()[-1]} — {type_}"
        return {
            "fn": fn,
            "url": f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded}",
            "source": "Wikimedia Commons",
            "license": "CC BY-SA 4.0",
            "type": type_,
            "caption": caption,
        }

    if main_fn:
        photos.append(make(main_fn, "bloeiwijze"))

    used = {main_fn} if main_fn else set()
    buckets: dict[str, list[str]] = {"bloeiwijze": [], "vrucht": [], "blad": [], "habitus": [], "algemeen": []}
    for fn in extras:
        if fn in used:
            continue
        t = classify_filename(fn, plant_name)
        buckets[t].append(fn)

    # Voeg in volgorde toe: habitus → vrucht of blad
    for preferred_type in ("habitus", "bloeiwijze", "vrucht", "blad", "algemeen"):
        for fn in buckets[preferred_type]:
            if fn not in used and len(photos) < 3:
                photos.append(make(fn, preferred_type))
                used.add(fn)

    return photos


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Toon resultaat zonder te schrijven")
    args = parser.parse_args()

    # Haal plantnamen op uit _sources.py (geen afhankelijkheid van _photos.py)
    from data.enrichments._sources import SOURCES
    plants = list(SOURCES.keys())
    print(f"Planten verwerken: {len(plants)}\n")

    # Stap 1: Hoofdafbeeldingen ophalen in batches van 50
    print("Stap 1 — Wikipedia hoofdafbeeldingen ophalen (batches van 50)...")
    main_images: dict[str, str] = {}
    for i in range(0, len(plants), 50):
        batch = plants[i:i + 50]
        imgs = batch_wiki_images(batch)
        main_images.update(imgs)
        print(f"  Batch {i // 50 + 1}/{(len(plants) - 1) // 50 + 1}: "
              f"{len(imgs)}/{len(batch)} gevonden")
        time.sleep(PAUSE)
    print(f"  Totaal: {len(main_images)}/{len(plants)} hoofdafbeeldingen\n")

    # Stap 2: Artikel-afbeeldingen voor extra foto's
    print("Stap 2 — Wikipedia artikel-afbeeldingen ophalen voor extra foto's...")
    article_images: dict[str, list[str]] = {}
    for i, name in enumerate(plants):
        imgs = wiki_article_images(name)
        article_images[name] = imgs
        if (i + 1) % 25 == 0:
            print(f"  Voortgang: {i + 1}/{len(plants)}")
        time.sleep(PAUSE)
    print("  Klaar.\n")

    # Stap 3: Foto's samenstellen; bij lege sets → Commons-fallback
    print("Stap 3 — Foto's samenstellen (met Commons-fallback voor lege sets)...")
    result: dict[str, list[dict]] = {}
    missing_after_fallback: list[str] = []

    for name in plants:
        main_fn = main_images.get(name)
        extras = article_images.get(name, [])
        photos = pick_photos(main_fn, extras, name)

        if not photos:
            # Probeer Commons search als fallback
            commons_files = commons_search(name, limit=6)
            time.sleep(PAUSE)
            photos = pick_photos(None, commons_files, name)
            if photos:
                print(f"  [Commons-fallback] {name}: {len(photos)} foto(s)")

        if not photos:
            missing_after_fallback.append(name)
        result[name] = photos

    if missing_after_fallback:
        print(f"\n  Geen foto's gevonden voor {len(missing_after_fallback)} planten:")
        for m in missing_after_fallback:
            print(f"    - {m}")

    if args.dry_run:
        print("\n[DRY-RUN] Eerste 5 planten preview:")
        for name in plants[:5]:
            print(f"  {name}:")
            for p in result[name]:
                print(f"    [{p['type']}] {p['fn']}")
        return

    # Schrijf _photos.py
    out_path = os.path.join(os.path.dirname(__file__), "enrichments", "_photos.py")
    lines: list[str] = []
    lines.append('"""')
    lines.append("Plantenpedia — Foto's per plant (gegenereerd via fetch_photos.py)")
    lines.append("Foto's zijn bevestigde Wikimedia Commons bestanden uit Wikipedia-artikelen.")
    lines.append("")
    lines.append("Upload: python data/upload.py --fields photos")
    lines.append('"""')
    lines.append("from ._helpers import wiki")
    lines.append("")
    lines.append("PHOTOS: dict = {")
    lines.append("")

    for name in plants:
        photos = result[name]
        if not photos:
            lines.append(f'# {name}: geen foto gevonden')
            lines.append(f'"{name}": {{"photos": []}},')
            lines.append("")
            continue
        lines.append(f'"{name}": {{"photos": [')
        for p in photos:
            fn_escaped = p["fn"].replace("\\", "\\\\").replace('"', '\\"')
            caption = p["caption"].replace('"', '\\"')
            lines.append(f'    wiki("{fn_escaped}", "{caption}", type_="{p["type"]}"),')
        lines.append("]},")   # ]  sluit list, }  sluit inner dict, ,  separator
        lines.append("")

    lines.append("}")
    lines.append("")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nGeschreven naar {out_path}")
    found = sum(1 for p in result.values() if p)
    print(f"Planten met ≥1 foto: {found}/{len(plants)}")
    print(f"Planten met ≥2 foto's: {sum(1 for p in result.values() if len(p) >= 2)}/{len(plants)}")
    print(f"Planten met 3 foto's: {sum(1 for p in result.values() if len(p) == 3)}/{len(plants)}")
    print("\nKlaar! Run nu: python data/upload.py --fields photos")


if __name__ == "__main__":
    main()
