"""
Plantenpedia — Encyclopedie
Rasteroverzicht van alle planten + individuele detailpagina's.
De detailpagina wordt geactiveerd via de query-param ?plant=<slug>.
"""
import streamlit as st

from utils.database import get_all_plants, get_plant_by_slug, search_plants
from utils.display import (
    CATEGORY_LABELS,
    bloom_label,
    first_photo,
    make_slug,
    render_footer,
    render_plant_page,
)

# ── Router: detailpagina of overzicht ─────────────────────────────────────────
# Query param heeft voorrang; session_state vangt navigatie vanuit andere pagina's op
plant_slug = st.query_params.get("plant") or st.session_state.pop("navigate_to_plant", None)
if plant_slug and not st.query_params.get("plant"):
    st.query_params["plant"] = plant_slug

# ═══════════════════════════════════════════════════════════════
# DETAILPAGINA
# ═══════════════════════════════════════════════════════════════
if plant_slug:
    plant = get_plant_by_slug(plant_slug)

    if plant:
        if st.button("← Terug naar overzicht"):
            st.query_params.clear()
            st.rerun()

        render_plant_page(plant)

    else:
        st.error(f"Plant met slug **'{plant_slug}'** niet gevonden in de database.")
        if st.button("← Terug naar overzicht"):
            st.query_params.clear()
            st.rerun()

    render_footer()
    st.stop()

# ═══════════════════════════════════════════════════════════════
# OVERZICHTSPAGINA
# ═══════════════════════════════════════════════════════════════
st.title("📖 Plantengids")

# ── Zoek- en filterbalk ───────────────────────────────────────────────────────
col_search, col_cat = st.columns([3, 1])
with col_search:
    query = st.text_input(
        "Zoek op naam",
        placeholder="bijv. paardenbloem, brandnetel, Taraxacum…",
        label_visibility="collapsed",
    )
with col_cat:
    cat_options = ["Alle categorieën"] + list(CATEGORY_LABELS.values())
    cat_choice = st.selectbox("Categorie", cat_options, label_visibility="collapsed")

# ── Planten ophalen ───────────────────────────────────────────────────────────
if query.strip():
    plants = search_plants(query.strip())
else:
    plants = get_all_plants()

# Categoriefilter toepassen
if cat_choice != "Alle categorieën":
    cat_key = next(
        (k for k, v in CATEGORY_LABELS.items() if v == cat_choice), None
    )
    if cat_key:
        plants = [p for p in plants if p.get("category") == cat_key]

# ── Resultaten weergeven ──────────────────────────────────────────────────────
n = len(plants)
st.caption(f"{n} soort{'en' if n != 1 else ''} gevonden")

if not plants:
    st.info("Geen planten gevonden. Probeer een andere zoekterm of categorie.")
    st.stop()

# Groepeer op categorie voor overzichtelijke weergave
cat_order = list(CATEGORY_LABELS.keys())

def sort_key(p):
    cat = p.get("category", "overig")
    idx = cat_order.index(cat) if cat in cat_order else len(cat_order)
    return (idx, p.get("scientific_name", ""))

plants_sorted = sorted(plants, key=sort_key)

# Groepeer alleen als er geen zoekopdracht is (anders: gewoon raster)
if query.strip() or cat_choice != "Alle categorieën":
    _groups = {None: plants_sorted}
else:
    from itertools import groupby
    _groups = {}
    for p in plants_sorted:
        c = p.get("category", "overig")
        _groups.setdefault(c, []).append(p)

CARDS_PER_ROW = 4

for group_key, group_plants in _groups.items():
    if group_key:
        st.subheader(CATEGORY_LABELS.get(group_key, group_key))

    # Rij voor rij renderen
    for row_start in range(0, len(group_plants), CARDS_PER_ROW):
        row = group_plants[row_start: row_start + CARDS_PER_ROW]
        cols = st.columns(CARDS_PER_ROW)

        for i, plant in enumerate(row):
            with cols[i]:
                photo = first_photo(plant, preferred=["habitus", "algemeen", "bloeiwijze", "blad"])
                dutch = plant.get("dutch_names") or []
                primary = dutch[0] if dutch else plant["scientific_name"]
                cat = plant.get("category", "overig")
                slug = plant.get("slug") or make_slug(plant["scientific_name"])
                bl = bloom_label(plant.get("bloom_start"), plant.get("bloom_end"))

                with st.container(border=True):
                    if photo:
                        try:
                            st.image(photo["url"], width="stretch")
                        except Exception:
                            pass

                    st.markdown(f"**{primary}**")
                    st.markdown(f"*{plant['scientific_name']}*")
                    st.caption(CATEGORY_LABELS.get(cat, cat))
                    if bl != "Onbekend":
                        st.caption(f"🌸 {bl}")

                    if st.button(
                        "Bekijk →",
                        key=f"plant_{slug}_{row_start}_{i}",
                        width="stretch",
                    ):
                        st.query_params["plant"] = slug
                        st.rerun()

render_footer()
