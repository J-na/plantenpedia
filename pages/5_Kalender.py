"""
Plantenpedia — Seizoenskalender
Visuele bloei-tijdlijn: welke planten bloeien wanneer?
"""
from datetime import date

import streamlit as st

from utils.database import get_all_plants
from utils.display import CATEGORY_LABELS, MONTH_NAMES

st.set_page_config(page_title="Seizoenskalender · Plantenpedia", page_icon="📅", layout="wide")
st.title("📅 Seizoenskalender")
st.caption("Bloeitijden van alle planten in één overzicht. Gebruik de filters om te verfijnen.")

# ── Filters ──────────────────────────────────────────────────────────────────

all_plants = get_all_plants()
bloeiende = [p for p in all_plants if p.get("bloom_start") and p.get("bloom_end")]

col_f1, col_f2, col_f3 = st.columns([2, 2, 1])

with col_f1:
    category_options = sorted({p["category"] for p in bloeiende if p.get("category")})
    selected_cats = st.multiselect(
        "Categorie",
        options=category_options,
        format_func=lambda c: CATEGORY_LABELS.get(c, c),
        placeholder="Alle categorieën",
    )

with col_f2:
    search = st.text_input("Zoek op naam", placeholder="bijv. Achillea")

with col_f3:
    only_native = st.checkbox("Alleen inheems 🌿")

# Filter
filtered = bloeiende
if selected_cats:
    filtered = [p for p in filtered if p.get("category") in selected_cats]
if search:
    q = search.lower()
    filtered = [
        p for p in filtered
        if q in p.get("scientific_name", "").lower()
        or any(q in n.lower() for n in (p.get("dutch_names") or []))
    ]
if only_native:
    filtered = [p for p in filtered if p.get("native_nl")]

filtered.sort(key=lambda p: (p.get("bloom_start") or 13, p.get("scientific_name", "")))

st.markdown(f"**{len(filtered)}** planten met bekende bloeitijd")

if not filtered:
    st.info("Geen planten gevonden met de huidige filters.")
    st.stop()

# ── Kleurpalet per categorie ──────────────────────────────────────────────────

CATEGORY_COLORS: dict = {
    "vaste_plant":           "#4CAF50",
    "wilde_plant":           "#8BC34A",
    "eenjarige":             "#FF9800",
    "tweejarige":            "#FFC107",
    "bol_knol":              "#9C27B0",
    "kuipplant":             "#00BCD4",
    "waterplant":            "#2196F3",
    "keukenkruid":           "#795548",
    "gras":                  "#CDDC39",
    "heester":               "#F44336",
    "wintergroene_heester":  "#E91E63",
    "boom":                  "#3F51B5",
    "conifeer":              "#607D8B",
    "klimplant":             "#009688",
    "roos":                  "#E91E63",
    "overig":                "#9E9E9E",
}

# ── Legenda ───────────────────────────────────────────────────────────────────

present_cats = sorted({p.get("category") for p in filtered if p.get("category")})
if present_cats:
    leg_cols = st.columns(min(len(present_cats), 6))
    for i, cat in enumerate(present_cats):
        color = CATEGORY_COLORS.get(cat, "#9E9E9E")
        leg_cols[i % len(leg_cols)].markdown(
            f'<span style="background:{color};color:white;padding:2px 8px;'
            f'border-radius:4px;font-size:0.75rem">'
            f'{CATEGORY_LABELS.get(cat, cat)}</span>',
            unsafe_allow_html=True,
        )

st.markdown("---")

# ── Huidige maand markeren ────────────────────────────────────────────────────

current_month = date.today().month
MONTHS = list(range(1, 13))
MONTH_SHORT = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]

# ── Tabel opbouwen als HTML ───────────────────────────────────────────────────

def _plant_link(p: dict) -> str:
    slug = p.get("slug", "")
    dutch = (p.get("dutch_names") or [])
    name = dutch[0] if dutch else p["scientific_name"]
    sci = p["scientific_name"]
    return f'<a href="/Planten?plant={slug}" target="_self" title="{sci}" style="color:inherit;text-decoration:none">{name}</a>'


rows_html = []
for p in filtered:
    bstart = p.get("bloom_start") or 0
    bend   = p.get("bloom_end")   or 0
    cat    = p.get("category", "overig")
    color  = CATEGORY_COLORS.get(cat, "#9E9E9E")

    cells = []
    for m in MONTHS:
        in_bloom = bstart <= m <= bend
        bg = color if in_bloom else "transparent"
        border = "2px solid #FF5722" if m == current_month else "1px solid #ddd"
        cells.append(
            f'<td style="background:{bg};border:{border};width:32px;height:24px"></td>'
        )

    native_badge = ' <span title="Inheems" style="font-size:0.7rem">🌿</span>' if p.get("native_nl") else ""
    name_cell = f'<td style="padding:2px 6px;white-space:nowrap;font-size:0.8rem">{_plant_link(p)}{native_badge}</td>'
    rows_html.append(f"<tr>{name_cell}{''.join(cells)}</tr>")

header_cells = "".join(
    f'<th style="width:32px;text-align:center;font-size:0.75rem;'
    f'{"color:#FF5722;font-weight:bold" if m == current_month else ""}">'
    f'{MONTH_SHORT[m-1]}</th>'
    for m in MONTHS
)

table_html = f"""
<div style="overflow-x:auto">
<table style="border-collapse:collapse;width:100%">
  <thead>
    <tr>
      <th style="text-align:left;padding:2px 6px;min-width:160px">Plant</th>
      {header_cells}
    </tr>
  </thead>
  <tbody>
    {''.join(rows_html)}
  </tbody>
</table>
</div>
<p style="font-size:0.75rem;color:#888;margin-top:8px">
  Rode rand = huidige maand ({MONTH_NAMES[current_month].capitalize()}).
  Klik op een plantnaam om naar de plantpagina te gaan.
</p>
"""

st.markdown(table_html, unsafe_allow_html=True)
