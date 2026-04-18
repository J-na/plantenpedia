"""
Plantenpedia — Startpagina
Toont de 'Soort van de dag' en biedt navigatie naar de rest van de app.
"""
from datetime import date

import streamlit as st

from utils.database import get_plant_of_day
from utils.display import (
    CATEGORY_LABELS,
    MONTH_NAMES,
    bloom_label,
    first_photo,
    make_slug,
)

# ── Globale CSS ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer     {visibility: hidden;}

    .hero-banner {
        background: linear-gradient(135deg, #1e5218 0%, #3d7a32 60%, #5aaa4c 100%);
        color: white;
        padding: 2.5rem 2rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    .hero-banner h1 { font-size: 2.8rem; margin: 0 0 0.3rem; }
    .hero-banner p  { font-size: 1.1rem; opacity: 0.9; margin: 0; }

    .pod-badge {
        display: inline-block;
        background: #3d7a32;
        color: white;
        padding: 0.2rem 0.8rem;
        border-radius: 999px;
        font-size: 0.85rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Hero banner ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero-banner">
        <h1>🌿 Plantenpedia</h1>
        <p>Uitgebreide plantengids voor in Nederland voorkomende soorten</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Soort van de dag ──────────────────────────────────────────────────────────
today = date.today()
dag_str = f"{today.day} {MONTH_NAMES[today.month]} {today.year}"

st.markdown(f"## 🌸 Soort van de dag &nbsp;·&nbsp; {dag_str}")

plant = get_plant_of_day(today)

if plant:
    photo = first_photo(plant)
    dutch_names = plant.get("dutch_names") or []
    primary_name = dutch_names[0] if dutch_names else plant["scientific_name"]
    all_dutch = ", ".join(dutch_names) if dutch_names else ""
    cat = plant.get("category", "overig")
    bl = bloom_label(plant.get("bloom_start"), plant.get("bloom_end"))

    col_img, col_info = st.columns([2, 3], gap="large")

    with col_img:
        if photo:
            try:
                st.image(photo["url"], use_container_width=True)
                if photo.get("source"):
                    st.caption(f"Foto: {photo['source']} · {photo.get('license', '')}")
            except Exception:
                st.markdown("*(foto niet beschikbaar)*")
        else:
            st.markdown(
                '<div style="background:#eef4eb;height:220px;border-radius:8px;'
                'display:flex;align-items:center;justify-content:center;color:#6a9e64;">'
                '🌿 Geen foto beschikbaar</div>',
                unsafe_allow_html=True,
            )

    with col_info:
        st.markdown(
            f'<span class="pod-badge">{CATEGORY_LABELS.get(cat, cat)}</span>',
            unsafe_allow_html=True,
        )
        st.markdown(f"## {primary_name}")
        st.markdown(f"*{plant['scientific_name']}*")
        if all_dutch and len(dutch_names) > 1:
            st.caption(f"Ook bekend als: {', '.join(dutch_names[1:])}")

        if bl != "Onbekend":
            st.markdown(f"🌸 **Bloeitijd:** {bl}")

        desc = plant.get("description") or ""
        if desc:
            short = desc[:400].rsplit(" ", 1)[0] + "…" if len(desc) > 400 else desc
            st.markdown(short)

        slug = plant.get("slug") or make_slug(plant["scientific_name"])
        if st.button("Lees het volledige artikel →", type="primary"):
            st.session_state["navigate_to_plant"] = slug
            st.switch_page("pages/1_Planten.py")
else:
    st.info(
        "Nog geen planten in de database. Voeg soorten toe via het beheerpaneel "
        "of voer het seedscript uit."
    )

st.divider()

# ── Navigatiekaarten ──────────────────────────────────────────────────────────
st.markdown("## Verken de gids")

nav1, nav2, nav3, nav4 = st.columns(4, gap="medium")

with nav1:
    with st.container(border=True):
        st.markdown("### 📖 Alle planten")
        st.markdown(
            "Blader door de volledige encyclopedie van ruim 250 plantensoorten. "
            "Klik op een soort voor het volledige artikel."
        )
        st.page_link("pages/1_Planten.py", label="Ga naar plantengids →", icon="📖")

with nav2:
    with st.container(border=True):
        st.markdown("### 🔍 Zoeken & filteren")
        st.markdown(
            "Vind planten op basis van eigenschappen: eetbaarheid, bloeiperiode, "
            "lichtinval, grondsoort en winterhardheid."
        )
        st.page_link("pages/2_Zoeken.py", label="Ga naar zoeken →", icon="🔍")

with nav3:
    with st.container(border=True):
        st.markdown("### 🌿 Plantenfamilies")
        st.markdown(
            "Verken planten per botanische familie. Lees over gemeenschappelijke "
            "kenmerken en ontdek verwante soorten."
        )
        st.page_link("pages/4_Families.py", label="Ga naar families →", icon="🌿")

with nav4:
    with st.container(border=True):
        st.markdown("### ⚙️ Beheer")
        st.markdown(
            "Bewerk plantartikelen, voeg nieuwe soorten toe en plan de soort "
            "van de dag in als administrator."
        )
        st.page_link("pages/3_Beheer.py", label="Ga naar beheer →", icon="⚙️")

st.divider()
st.caption(
    "Plantenpedia is een project van Jonathan. "
    "Alle informatie is bedoeld als leidraad; raadpleeg bij twijfel altijd een expert."
)
