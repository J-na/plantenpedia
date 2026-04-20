"""
Renderingfuncties voor plantinformatie in Streamlit.
"""
from __future__ import annotations

import re
from typing import Dict, List, Optional

import streamlit as st

from utils.database import make_slug

# ── Constanten & labels ──────────────────────────────────────────────────────

MONTH_NAMES = {
    1: "januari", 2: "februari", 3: "maart", 4: "april",
    5: "mei", 6: "juni", 7: "juli", 8: "augustus",
    9: "september", 10: "oktober", 11: "november", 12: "december",
}

CATEGORY_LABELS: Dict[str, str] = {
    "vaste_plant":            "Vaste plant",
    "eenjarige":              "Éénjarige",
    "tweejarige":             "Tweejarige",
    "bol_knol":               "Bol / Knol",
    "kuipplant":              "Kuipplant",
    "wilde_plant":            "Wilde plant",
    "waterplant":             "Waterplant",
    "keukenkruid":            "Keukenkruid",
    "gras":                   "Siergras",
    "heester":                "Heester",
    "wintergroene_heester":   "Wintergroene heester",
    "boom":                   "Boom",
    "conifeer":               "Conifeer",
    "klimplant":              "Klimplant",
    "roos":                   "Roos",
    "overig":                 "Overig",
}

LIGHT_LABELS: Dict[str, str] = {
    "vol_zon":              "Vol zon",
    "zon_halfschaduw":      "Zon tot halfschaduw",
    "halfschaduw":          "Halfschaduw",
    "halfschaduw_schaduw":  "Halfschaduw tot schaduw",
    "schaduw":              "Schaduw",
}

LIGHT_ICONS: Dict[str, str] = {
    "vol_zon":              "☀️",
    "zon_halfschaduw":      "🌤️",
    "halfschaduw":          "⛅",
    "halfschaduw_schaduw":  "🌥️",
    "schaduw":              "🌥️",
}

SOIL_LABELS: Dict[str, str] = {
    "zand":       "Zandgrond",
    "klei":       "Kleigrond",
    "leem":       "Leemgrond",
    "veen":       "Veengrond",
    "humusrijk":  "Humusrijke grond",
    "kalkrijk":   "Kalkrijke grond",
    "droog":      "Droge grond",
    "vochtig":    "Vochtige grond",
    "nat":        "Natte / moerassige grond",
}

HARDINESS_LABELS: Dict[str, str] = {
    "volledig_winterhard": "Volledig winterhard",
    "winterhard":          "Winterhard",
    "matig_winterhard":    "Matig winterhard",
    "vorstgevoelig":       "Vorstgevoelig",
    "niet_winterhard":     "Niet winterhard",
}

WATER_NEEDS_LABELS: Dict[str, str] = {
    "droog":   "Droog",
    "normaal": "Normaal",
    "vochtig": "Vochtig",
    "nat":     "Nat / moerassig",
}

HARDINESS_ICONS: Dict[str, str] = {
    "volledig_winterhard": "❄️❄️",
    "winterhard":          "❄️",
    "matig_winterhard":    "🌡️",
    "vorstgevoelig":       "⚠️",
    "niet_winterhard":     "🌴",
}

PHOTO_TYPE_LABELS: Dict[str, str] = {
    "jonge_plant":  "Jonge plant",
    "bloeiwijze":   "Bloeiwijze",
    "zaad":         "Zaad / vrucht",
    "habitus":      "Totaalbeeld",
    "blad":         "Blad",
    "stam":         "Stam / schors",
    "vrucht":       "Vrucht",
    "algemeen":     "Algemeen",
}

# ── Eco-score ────────────────────────────────────────────────────────────────

def display_eco_score(plant: Dict) -> None:
    """Toont ecologische scores (insecten, vogels, bodem) als sterren."""
    scores = {
        "🐝 Insecten": plant.get("score_insects"),
        "🐦 Vogels":   plant.get("score_birds"),
        "🌱 Bodem":    plant.get("score_soil"),
    }
    if not any(v for v in scores.values()):
        return
    cols = st.columns(3)
    for col, (label, val) in zip(cols, scores.items()):
        if val is not None:
            stars = "★" * val + "☆" * (5 - val)
            col.metric(label, stars)


# ── Hulpfuncties ─────────────────────────────────────────────────────────────

def _parse_height_from_growth_habit(text: str) -> Optional[str]:
    """Extraheert hoogte-informatie uit een groeiwijze-tekst als fallback."""
    if not text:
        return None
    m = re.search(r'\b(\d+)\s*[–\-]\s*(\d+)\s*(cm|m)\b', text)
    if m:
        return f"{m.group(1)}–{m.group(2)} {m.group(3)}"
    m = re.search(r'tot\s+(\d+)\s*(cm|m)\b', text)
    if m:
        return f"tot {m.group(1)} {m.group(2)}"
    return None


def bloom_label(start: Optional[int], end: Optional[int]) -> str:
    if start and end:
        return f"{MONTH_NAMES[start].capitalize()} – {MONTH_NAMES[end]}"
    if start:
        return f"Vanaf {MONTH_NAMES[start]}"
    if end:
        return f"Tot {MONTH_NAMES[end]}"
    return "Onbekend"


def first_photo(plant: Dict, preferred: Optional[List[str]] = None) -> Optional[Dict]:
    """Geeft de eerste foto terug in voorkeursvolgorde."""
    photos = plant.get("photos")
    if not isinstance(photos, list) or not photos:
        return None
    valid = [p for p in photos if isinstance(p, dict) and isinstance(p.get("url"), str) and p["url"]]
    if not valid:
        return None
    order = preferred or ["bloeiwijze", "habitus", "algemeen", "jonge_plant"]
    for ptype in order:
        for p in valid:
            if p.get("type") == ptype:
                return p
    return valid[0]


def render_photo_caption(photo: Dict) -> None:
    parts = []
    if photo.get("source"):
        parts.append(f"Bron: {photo['source']}")
    if photo.get("license"):
        parts.append(photo["license"])
    if parts:
        st.caption(" | ".join(parts))


# ── Kaartje voor lijstweergave ────────────────────────────────────────────────

def render_plant_card(plant: Dict, col_key: str = "") -> bool:
    """
    Compacte plantkaart voor de rasterweergave.
    Geeft True terug als de gebruiker op 'Bekijk' klikt.
    """
    photo = first_photo(plant, preferred=["habitus", "algemeen", "bloeiwijze", "blad"])
    dutch_names = plant.get("dutch_names") or []
    primary_name = dutch_names[0] if dutch_names else plant["scientific_name"]
    cat = plant.get("category", "overig")
    slug = plant.get("slug") or make_slug(plant["scientific_name"])

    clicked = False
    with st.container(border=True):
        if photo:
            url = photo["url"].replace('"', "%22")
            st.markdown(
                f'<img src="{url}" style="width:100%;max-height:160px;'
                'object-fit:cover;border-radius:6px;display:block;" '
                'loading="lazy" />',
                unsafe_allow_html=True,
            )
        st.markdown(f"**{primary_name}**")
        st.markdown(f"*{plant['scientific_name']}*")
        st.caption(CATEGORY_LABELS.get(cat, cat))
        bl = bloom_label(plant.get("bloom_start"), plant.get("bloom_end"))
        if bl != "Onbekend":
            st.caption(f"🌸 {bl}")
        if st.button("Bekijk →", key=f"card_{slug}_{col_key}", width="stretch"):
            clicked = True
    return clicked


# ── Volledige plantpagina ─────────────────────────────────────────────────────

def _render_mijn_tuin_button(plant: Dict) -> None:
    slug = plant.get("slug", "")
    if not slug:
        return
    if "mijn_tuin" not in st.session_state:
        st.session_state["mijn_tuin"] = []
    in_tuin = slug in st.session_state["mijn_tuin"]
    btn_col, _ = st.columns([2, 5])
    with btn_col:
        if in_tuin:
            if st.button("✓ In mijn tuin  —  verwijder", type="secondary", width="stretch"):
                st.session_state["mijn_tuin"].remove(slug)
                st.rerun()
        else:
            if st.button("♥ Voeg toe aan mijn tuin", type="primary", width="stretch"):
                st.session_state["mijn_tuin"].append(slug)
                st.rerun()


def render_plant_page(plant: Dict) -> None:
    """Render de volledige detailpagina voor een plant."""
    _render_header(plant)
    _render_mijn_tuin_button(plant)
    st.divider()
    _render_basic_info(plant)
    st.divider()
    _render_needs(plant)

    companions = plant.get("companion_plants") or []
    if companions:
        st.divider()
        _render_companion_plants(companions)

    st.divider()
    _render_human_relations(plant)

    cultivars = plant.get("cultivars") or []
    if cultivars:
        st.divider()
        _render_cultivars(cultivars)

    sources = plant.get("sources") or []
    if sources:
        st.divider()
        _render_sources(sources)


def _render_companion_plants(companions: List[Dict]) -> None:
    st.header("🌿 Goed mee combineren")
    cols_per_row = min(len(companions), 3)
    for row_start in range(0, len(companions), cols_per_row):
        row_items = companions[row_start: row_start + cols_per_row]
        cols = st.columns(cols_per_row)
        for i, comp in enumerate(row_items):
            with cols[i]:
                with st.container(border=True):
                    sci = comp.get("scientific_name", "")
                    dutch = comp.get("dutch_name") or sci
                    reason = comp.get("reason", "")
                    slug = make_slug(sci) if sci else ""
                    if slug:
                        st.markdown(
                            f'**<a href="/Planten?plant={slug}" target="_self" '
                            f'style="color:inherit;text-decoration:none">{dutch}</a>**',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(f"**{dutch}**")
                    if sci and sci != dutch:
                        st.caption(f"*{sci}*")
                    if reason:
                        st.markdown(reason)


# ── Sectie: header ────────────────────────────────────────────────────────────

def _render_header(plant: Dict) -> None:
    dutch_names = plant.get("dutch_names") or []
    dutch_str = ", ".join(dutch_names)

    # Titel met wintergroen-badge
    title_parts = [dutch_str or plant["scientific_name"]]
    evergreen_badge = " 🌲 *Wintergroen*" if plant.get("evergreen") else ""
    st.title(dutch_str or plant["scientific_name"])
    if evergreen_badge:
        st.caption("🌲 Wintergroene plant — behoudt zijn blad het hele jaar door")
    st.markdown(f"### *{plant['scientific_name']}*")

    # Eigenschappen-badges (compact HTML, geen grote st.metric)
    cat = plant.get("category", "overig")
    bl = bloom_label(plant.get("bloom_start"), plant.get("bloom_end"))
    light = plant.get("light_needs")
    h_min = plant.get("height_min")
    h_max = plant.get("height_max")
    hardiness = plant.get("hardiness")

    if h_min and h_max:
        hoogte_val = f"{h_min}–{h_max} cm"
    elif h_max:
        hoogte_val = f"tot {h_max} cm"
    else:
        hoogte_val = _parse_height_from_growth_habit(plant.get("growth_habit") or "") or "–"

    if light:
        licht_val = f"{LIGHT_ICONS.get(light, '')} {LIGHT_LABELS.get(light, light)}"
    else:
        licht_val = "–"

    if hardiness:
        hard_val = f"{HARDINESS_ICONS.get(hardiness, '❄️')} {HARDINESS_LABELS.get(hardiness, hardiness)}"
    else:
        hard_val = "–"

    if plant.get("toxic"):
        status_val = "⚠️ Giftig"
    elif plant.get("edible"):
        status_val = "✅ Eetbaar"
    else:
        status_val = "–"

    def _badge(label: str, value: str) -> str:
        return (
            f'<div style="background:#eef4eb;border:1px solid #c5ddbf;border-radius:7px;'
            f'padding:0.45rem 0.9rem;display:inline-block;margin:0.2rem 0.3rem 0.2rem 0">'
            f'<div style="font-size:0.85rem;color:#5a7a55;text-transform:uppercase;'
            f'font-weight:600;letter-spacing:0.03em">{label}</div>'
            f'<div style="font-size:1.07rem;font-weight:600;color:#1e5218;line-height:1.3">{value}</div>'
            f'</div>'
        )

    badges_html = (
        '<div style="display:flex;flex-wrap:wrap;margin:0.6rem 0 0.8rem">'
        + _badge("Type", CATEGORY_LABELS.get(cat, cat))
        + _badge("Bloeitijd", bl)
        + _badge("Licht", licht_val)
        + _badge("Hoogte", hoogte_val)
        + _badge("Winterhardheid", hard_val)
        + _badge("Status", status_val)
        + '</div>'
    )
    st.markdown(badges_html, unsafe_allow_html=True)

    # Foto's
    photos = plant.get("photos")
    valid_photos = [p for p in (photos or []) if isinstance(p, dict) and isinstance(p.get("url"), str) and p["url"]]
    if valid_photos:
        order_keys = list(PHOTO_TYPE_LABELS.keys())
        def sort_key(p):
            t = p.get("type", "algemeen")
            return order_keys.index(t) if t in order_keys else len(order_keys)
        sorted_photos = sorted(valid_photos, key=sort_key)[:5]

        _, _photo_area, _ = st.columns([0.1, 0.8, 0.1])
        with _photo_area:
            photo_cols = st.columns(len(sorted_photos))
            for i, photo in enumerate(sorted_photos):
                with photo_cols[i]:
                    caption_text = photo.get("caption") or ""
                    label = PHOTO_TYPE_LABELS.get(photo.get("type", ""), caption_text or "Foto")
                    try:
                        st.image(photo["url"], caption=str(label), width="stretch")
                    except Exception:
                        st.caption("*(foto niet beschikbaar)*")
                    render_photo_caption(photo)


# ── Sectie: basisinformatie ───────────────────────────────────────────────────

def _render_basic_info(plant: Dict) -> None:
    st.header("Basisinformatie")

    # Herkomst & familie — compacte metarij
    family = plant.get("family")
    family_common = plant.get("family_common")
    origin = plant.get("origin")
    meta_items = []
    if origin:
        meta_items.append(f"🌍 **Herkomst:** {origin}")
    if family:
        fam_label = family
        if family_common:
            fam_label = f"{family} ({family_common})"
        meta_items.append(f"🌿 **Familie:** {fam_label}")
    if meta_items:
        meta_col, btn_col = st.columns([4, 1])
        with meta_col:
            st.markdown(" &nbsp;·&nbsp; ".join(meta_items), unsafe_allow_html=True)
        with btn_col:
            if family and st.button(
                f"Bekijk familie →",
                key=f"fam_btn_{plant.get('slug', family)}",
                help=f"Alle soorten in de familie {family}",
            ):
                st.query_params["family"] = family
                st.switch_page("pages/4_Families.py")

    if plant.get("description"):
        st.markdown(plant["description"])
    else:
        st.info("Beschrijving nog niet beschikbaar.")

    col1, col2 = st.columns(2)
    with col1:
        if plant.get("distribution"):
            st.subheader("Verspreidingsgebied")
            st.markdown(plant["distribution"])
    with col2:
        if plant.get("growth_habit"):
            st.subheader("Groeiwijze")
            st.markdown(plant["growth_habit"])


# ── Sectie: behoeftes ─────────────────────────────────────────────────────────

def _render_needs(plant: Dict) -> None:
    st.header("Behoeftes van de plant")

    col1, col2 = st.columns(2)

    with col1:
        # Grondsoort
        soils = plant.get("soil_types") or []
        if soils:
            st.subheader("🌱 Grondsoort")
            for s in soils:
                st.markdown(f"- {SOIL_LABELS.get(s, s)}")

        # Voeding
        if plant.get("fertilizer_needs"):
            st.subheader("🌿 Voeding & bemesting")
            st.markdown(plant["fertilizer_needs"])

        # Ecologische waarde
        if plant.get("ecological_value"):
            st.subheader("🦋 Ecologische waarde")
            st.markdown(plant["ecological_value"])

    with col2:
        # Snoeien
        if plant.get("pruning_info"):
            st.subheader("✂️ Snoeien")
            st.markdown(plant["pruning_info"])

        # Woekeren
        if plant.get("weed_behavior"):
            st.subheader("⚠️ Woekerende eigenschappen")
            st.markdown(plant["weed_behavior"])

        # Plagen & ziektes
        if plant.get("pests_diseases"):
            st.subheader("🔴 Plagen & ziektes")
            st.markdown(plant["pests_diseases"])

    # Insecten & dieren
    insects = plant.get("insects_animals") or []
    if insects:
        st.subheader("Insecten & dieren")
        for item in insects:
            icon = "✅" if item.get("desirable", True) else "⚠️"
            name = item.get("name", "Onbekend")
            desc = item.get("description", "")
            st.markdown(f"{icon} **{name}** — {desc}")


# ── Sectie: relatie met de mens ───────────────────────────────────────────────

def _render_human_relations(plant: Dict) -> None:
    st.header("Relatie met de mens")

    col1, col2 = st.columns(2)

    with col1:
        # Eetbaarheid
        st.subheader("🍽️ Eetbaarheid")
        if plant.get("edible"):
            st.success("Deze plant is (deels) eetbaar.")
            if plant.get("edible_parts"):
                st.markdown(f"**Eetbare delen:** {plant['edible_parts']}")
            if plant.get("taste"):
                st.markdown(f"**Smaak:** {plant['taste']}")
            if plant.get("recipes"):
                st.markdown("**Bereiding & recepten:**")
                st.markdown(plant["recipes"])
            if plant.get("nutritional_value"):
                st.markdown("**Voedingswaarden:**")
                st.markdown(plant["nutritional_value"])
        else:
            st.info("Niet eetbaar of niet van toepassing.")

        # Medicinaal
        if plant.get("medicinal_uses"):
            st.subheader("💊 Medicinale toepassingen")
            st.markdown(plant["medicinal_uses"])

        # Overige toepassingen
        if plant.get("other_uses"):
            st.subheader("🔧 Overige toepassingen")
            st.markdown(plant["other_uses"])

    with col2:
        # Giftigheid
        st.subheader("⚠️ Giftigheid")
        if plant.get("toxic"):
            st.error("⚠️ Deze plant is (deels) giftig.")
            if plant.get("toxic_info"):
                st.markdown(plant["toxic_info"])
        else:
            st.success("Niet als giftig bekend.")

        # Verwisselingsgevaar
        lookalikes = plant.get("lookalikes") or []
        if lookalikes:
            st.subheader("👀 Kan verward worden met")
            for item in lookalikes:
                with st.expander(item.get("name", "Onbekende soort")):
                    st.markdown(item.get("difference", ""))
                    if item.get("photo_url"):
                        try:
                            st.image(item["photo_url"], width=250)
                        except Exception:
                            pass

        # Houteigenschappen
        if plant.get("wood_properties"):
            st.subheader("🪵 Houteigenschappen")
            st.markdown(plant["wood_properties"])


# ── Sectie: cultivars ─────────────────────────────────────────────────────────

def _render_cultivars(cultivars: List[Dict]) -> None:
    st.header(f"Cultivars & variëteiten ({len(cultivars)})")
    cols_per_row = 3
    for row_start in range(0, len(cultivars), cols_per_row):
        row_items = cultivars[row_start: row_start + cols_per_row]
        cols = st.columns(cols_per_row)
        for i, cv in enumerate(row_items):
            with cols[i]:
                with st.container(border=True):
                    if cv.get("photo_url"):
                        try:
                            st.image(cv["photo_url"], width="stretch")
                        except Exception:
                            pass
                        if cv.get("photo_source"):
                            st.caption(f"Foto: {cv['photo_source']}")
                    st.markdown(f"**{cv.get('name', 'Onbekend')}**")
                    if cv.get("description"):
                        st.markdown(cv["description"])


# ── Sectie: bronnen ───────────────────────────────────────────────────────────

def _render_sources(sources: List[Dict]) -> None:
    st.header("Bronnen & meer informatie")
    for src in sources:
        title = src.get("title", "Bron")
        url = src.get("url")
        desc = src.get("description", "")
        suffix = f" — {desc}" if desc else ""
        if url:
            st.markdown(f"- [{title}]({url}){suffix}")
        else:
            st.markdown(f"- **{title}**{suffix}")


# ── Sitewijde footer ──────────────────────────────────────────────────────────

def render_footer() -> None:
    """Standaard footer met attributie en contactgegevens. Roep aan als laatste regel van elke pagina."""
    st.divider()
    st.caption(
        "Plantenpedia is een project van Jonathan Meijers. "
        "Alle informatie is bedoeld als leidraad; raadpleeg bij twijfel altijd een expert.  \n"
        "Voor vragen, opmerkingen of suggesties: "
        "[jonathanmeijers2000@gmail.com](mailto:jonathanmeijers2000@gmail.com)"
    )
