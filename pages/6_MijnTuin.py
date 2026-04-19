"""
Plantenpedia — Mijn Tuinlijst
Persoonlijk overzicht van opgeslagen planten (opgeslagen in sessie).
"""
import streamlit as st

from utils.database import get_plant_by_slug
from utils.display import CATEGORY_LABELS, MONTH_NAMES, bloom_label, first_photo

st.title("🌻 Mijn Tuinlijst")
st.caption("Sla planten op vanuit de detailpagina. Je lijst blijft bewaard zolang je browser-tab open is.")

if "mijn_tuin" not in st.session_state:
    st.session_state["mijn_tuin"] = []

slugs = list(st.session_state["mijn_tuin"])

if not slugs:
    st.info(
        "Je lijst is leeg. Open een plant en klik op **♥ Voeg toe aan mijn tuin** om hem hier te bewaren.",
        icon="🌿",
    )
    st.stop()

# Fetch plants from DB
plants = []
for slug in slugs:
    p = get_plant_by_slug(slug)
    if p:
        plants.append(p)

# Sort by bloom_start
plants.sort(key=lambda p: (p.get("bloom_start") or 13, p.get("scientific_name", "")))

# Header row
col_count, col_clear = st.columns([5, 1])
with col_count:
    st.markdown(f"**{len(plants)} plant{'en' if len(plants) != 1 else ''}** opgeslagen in je lijst")
with col_clear:
    if st.button("🗑️ Alles wissen", type="secondary"):
        st.session_state["mijn_tuin"] = []
        st.rerun()

# Bloom summary
bloom_groups: dict = {}
for p in plants:
    bs = p.get("bloom_start")
    be = p.get("bloom_end")
    if bs and be:
        for m in range(bs, be + 1):
            bloom_groups.setdefault(m, []).append(p)

if bloom_groups:
    earliest = min(bloom_groups)
    latest = max(bloom_groups)
    peak_month = max(bloom_groups, key=lambda m: len(bloom_groups[m]))
    st.info(
        f"🌸 Je tuin bloeit van **{MONTH_NAMES[earliest]}** tot **{MONTH_NAMES[latest]}** "
        f"— piek in **{MONTH_NAMES[peak_month]}** ({len(bloom_groups[peak_month])} planten tegelijk bloeiend)",
        icon="🌸",
    )

st.markdown("---")

# Plant cards
for p in plants:
    slug = p.get("slug", "")
    dutch = p.get("dutch_names") or []
    name = dutch[0] if dutch else p["scientific_name"]
    photo = first_photo(p)
    cat = p.get("category", "overig")
    bl = bloom_label(p.get("bloom_start"), p.get("bloom_end"))
    native = p.get("native_nl")
    score_ins = p.get("score_insects")

    with st.container(border=True):
        img_col, info_col, act_col = st.columns([1, 5, 1])
        with img_col:
            if photo:
                try:
                    st.image(photo["url"], width="stretch")
                except Exception:
                    pass
        with info_col:
            native_badge = " 🌿" if native else ""
            st.markdown(f"**{name}**{native_badge}")
            st.markdown(f"*{p['scientific_name']}*")
            meta_parts = [CATEGORY_LABELS.get(cat, cat)]
            if bl != "Onbekend":
                meta_parts.append(f"🌸 {bl}")
            if score_ins is not None:
                meta_parts.append(f"🐝 {'★' * score_ins}{'☆' * (5 - score_ins)}")
            st.caption(" · ".join(meta_parts))
        with act_col:
            if st.button("Bekijk →", key=f"view_{slug}"):
                st.session_state["navigate_to_plant"] = slug
                st.switch_page("pages/1_Planten.py")
            if st.button("✕", key=f"remove_{slug}", help="Verwijder uit lijst"):
                st.session_state["mijn_tuin"].remove(slug)
                st.rerun()
