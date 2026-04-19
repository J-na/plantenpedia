"""
Plantenpedia — Vergelijkingspagina
Vergelijk 2 tot 4 planten naast elkaar op alle kenmerken.
"""
import streamlit as st

from utils.database import get_all_plants
from utils.display import (
    CATEGORY_LABELS,
    LIGHT_LABELS,
    MONTH_NAMES,
    bloom_label,
    first_photo,
    make_slug,
)

st.title("⚖️ Vergelijk planten")
st.caption("Selecteer 2 tot 4 planten om ze naast elkaar te vergelijken op bloeitijd, licht, ecologie en meer.")

all_plants = get_all_plants()

# ── Plantopzoek: dutch + wetenschappelijk ────────────────────────────────────

def _display_label(p: dict) -> str:
    dutch = p.get("dutch_names") or []
    first = dutch[0] if dutch else ""
    sci = p["scientific_name"]
    return f"{first} — {sci}" if first else sci

label_to_sci: dict = {}
for p in all_plants:
    label_to_sci[_display_label(p)] = p["scientific_name"]

sci_to_plant: dict = {p["scientific_name"]: p for p in all_plants}

sorted_labels = sorted(label_to_sci.keys())

selected_labels = st.multiselect(
    "Zoek en selecteer planten (max. 4)",
    options=sorted_labels,
    max_selections=4,
    placeholder="Typ een naam…",
)

if len(selected_labels) < 2:
    if selected_labels:
        st.info("Selecteer nog minimaal één plant om te vergelijken.")
    else:
        st.info("Selecteer 2 tot 4 planten om te vergelijken.")
    st.stop()

plants = [sci_to_plant[label_to_sci[lbl]] for lbl in selected_labels]
n = len(plants)

# ── Foto's + namen ───────────────────────────────────────────────────────────

photo_cols = st.columns(n)
for col, p in zip(photo_cols, plants):
    with col:
        photo = first_photo(p)
        if photo:
            try:
                st.image(photo["url"], width="stretch")
            except Exception:
                pass
        dutch = p.get("dutch_names") or []
        name = dutch[0] if dutch else p["scientific_name"]
        slug = p.get("slug") or make_slug(p["scientific_name"])
        st.markdown(
            f'**<a href="/Planten?plant={slug}" target="_self" style="color:inherit">{name}</a>**',
            unsafe_allow_html=True,
        )
        st.caption(f"*{p['scientific_name']}*")

st.divider()

# ── Vergelijkingstabel ───────────────────────────────────────────────────────

WATER_LABELS = {
    "droog":    "💧 Droog",
    "normaal":  "💧💧 Normaal",
    "vochtig":  "💧💧💧 Vochtig",
    "nat":      "💧💧💧💧 Nat",
}

def _score(val) -> str:
    if val is None:
        return "–"
    return "★" * val + "☆" * (5 - val)

def _height(p: dict) -> str:
    h_min = p.get("height_min")
    h_max = p.get("height_max")
    if h_min and h_max:
        return f"{h_min}–{h_max} cm"
    if h_max:
        return f"tot {h_max} cm"
    return "–"

def _soil(p: dict) -> str:
    soils = p.get("soil_types") or []
    return ", ".join(soils[:3]) if soils else "–"

def _status(p: dict) -> str:
    if p.get("toxic"):
        return "⚠️ Giftig"
    if p.get("edible"):
        return "✅ Eetbaar"
    return "–"

def _row(label: str, values: list, emoji: str = "") -> None:
    label_col, *val_cols = st.columns([2] + [3] * n)
    prefix = f"{emoji} " if emoji else ""
    label_col.markdown(f"**{prefix}{label}**")
    for col, val in zip(val_cols, values):
        col.markdown(str(val) if val else "–")

_row("Type",          [CATEGORY_LABELS.get(p.get("category", ""), "–") for p in plants], "🌿")
_row("Bloeitijd",     [bloom_label(p.get("bloom_start"), p.get("bloom_end")) for p in plants], "🌸")
_row("Licht",         [LIGHT_LABELS.get(p.get("light_needs", ""), p.get("light_needs") or "–") for p in plants], "☀️")
_row("Hoogte",        [_height(p) for p in plants], "📏")
_row("Waterbehoeften",[WATER_LABELS.get(p.get("water_needs", ""), p.get("water_needs") or "–") for p in plants], "💧")
_row("Bodemtype",     [_soil(p) for p in plants], "🌱")
_row("Wintergroen",   ["Ja ✓" if p.get("evergreen") else "Nee" for p in plants], "🌲")
_row("Winterhardheid",[p.get("hardiness") or "–" for p in plants], "❄️")
_row("Inheems NL",    ["🌿 Ja" if p.get("native_nl") else "Nee" for p in plants])
_row("Droogtebestendig", ["☀️ Ja" if p.get("drought_tolerant") else "Nee" for p in plants])
_row("Status",        [_status(p) for p in plants])
_row("Familie",       [p.get("family_common") or p.get("family") or "–" for p in plants])

st.divider()
st.markdown("**Ecologische scores** (★ = uitstekend, ☆ = geen waarde)")

_row("🐝 Insecten",   [_score(p.get("score_insects")) for p in plants])
_row("🐦 Vogels",     [_score(p.get("score_birds")) for p in plants])
_row("🌱 Bodem",      [_score(p.get("score_soil")) for p in plants])

# ── Totaalscore ───────────────────────────────────────────────────────────────

totals = [
    (p.get("score_insects") or 0) + (p.get("score_birds") or 0) + (p.get("score_soil") or 0)
    for p in plants
]
if any(t > 0 for t in totals):
    _row("Totaal ecologie", [f"**{t}/15**" for t in totals])
