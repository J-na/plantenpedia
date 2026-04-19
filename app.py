"""
Plantenpedia — Hoofdingang
Configureert de navigatie en start de app.
"""
import streamlit as st

st.set_page_config(
    page_title="Plantenpedia — Ecologisch Hovenier",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

pg = st.navigation([
    st.Page("pages/Startpagina.py",  title="Startpagina", icon="🌿", default=True),
    st.Page("pages/1_Planten.py",    title="Planten",     icon="📖"),
    st.Page("pages/2_Zoeken.py",     title="Zoeken",      icon="🔍"),
    st.Page("pages/5_Kalender.py",   title="Kalender",    icon="📅"),
    st.Page("pages/4_Families.py",   title="Families",    icon="🌿"),
    st.Page("pages/3_Beheer.py",     title="Beheer",      icon="⚙️"),
])
pg.run()
