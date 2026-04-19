"""
Plantenpedia — Plantenfamilies
Blader door de plantenfamilies en bekijk welke soorten daartoe behoren.
"""
import streamlit as st

from utils.database import (
    get_all_families,
    get_families_with_counts,
    get_family,
    get_plants_by_family,
)
from utils.display import (
    CATEGORY_LABELS,
    bloom_label,
    first_photo,
    make_slug,
    render_footer,
)

# ── Routing op basis van query param ─────────────────────────────────────────
selected_family = st.query_params.get("family")

if selected_family:
    # ── DETAILPAGINA VAN ÉÉN FAMILIE ────────────────────────────────────────

    # Terug-knop
    if st.button("← Alle families"):
        st.query_params.clear()
        st.rerun()

    family_info = get_family(selected_family)
    plants_in_family = get_plants_by_family(selected_family)

    # Header
    if family_info:
        dutch = family_info.get("dutch_name")
        st.title(f"🌿 {selected_family}" + (f" — {dutch}" if dutch else ""))
        if family_info.get("description"):
            st.markdown(family_info["description"])
        else:
            st.info(
                "Nog geen beschrijving beschikbaar voor deze familie. "
                "Een beheerder kan dit toevoegen via het beheerpaneel."
            )
    else:
        st.title(f"🌿 {selected_family}")
        st.info(
            "Deze familie heeft nog geen aparte pagina. "
            "Een beheerder kan een beschrijving toevoegen via het beheerpaneel."
        )

    st.divider()

    n = len(plants_in_family)
    st.markdown(f"### {n} soort{'en' if n != 1 else ''} in deze familie")

    if not plants_in_family:
        st.warning(
            "Geen planten gevonden in deze familie. "
            "Controleer of de familienaam exact overeenkomt met de waarde in de plantgegevens."
        )
        st.stop()

    # Raster van plantkaarten
    CARDS_PER_ROW = 4
    for row_start in range(0, len(plants_in_family), CARDS_PER_ROW):
        row = plants_in_family[row_start : row_start + CARDS_PER_ROW]
        cols = st.columns(CARDS_PER_ROW)

        for i, plant in enumerate(row):
            with cols[i]:
                photo = first_photo(plant, preferred=["habitus", "algemeen", "bloeiwijze", "blad"])
                dutch_names = plant.get("dutch_names") or []
                primary = dutch_names[0] if dutch_names else plant["scientific_name"]
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

                    badges = []
                    if plant.get("edible"):
                        badges.append("✅ Eetbaar")
                    if plant.get("toxic"):
                        badges.append("⚠️ Giftig")
                    if plant.get("evergreen"):
                        badges.append("🌲 Wintergroen")
                    if badges:
                        st.caption(" · ".join(badges))

                    if st.button(
                        "Bekijk →",
                        key=f"fam_plant_{slug}_{row_start}_{i}",
                        width="stretch",
                    ):
                        st.session_state["navigate_to_plant"] = slug
                        st.switch_page("pages/1_Planten.py")

else:
    # ── OVERZICHTSPAGINA VAN ALLE FAMILIES ──────────────────────────────────

    st.title("🌿 Plantenfamilies")
    st.markdown(
        "Planten zijn ingedeeld in families op basis van gemeenschappelijke kenmerken. "
        "Klik op een familie om alle soorten te bekijken en meer te leren over de gemeenschappelijke eigenschappen."
    )

    families_with_counts = get_families_with_counts()

    if not families_with_counts:
        st.info(
            "Nog geen plantenfamilies beschikbaar. Zorg ervoor dat planten een familie-waarde hebben "
            "en voeg familie-beschrijvingen toe via het beheerpaneel."
        )
        st.stop()

    st.divider()
    st.markdown(f"**{len(families_with_counts)} families** met planten in de encyclopedie")

    # Families per 3 kolommen tonen
    COLS = 3
    for row_start in range(0, len(families_with_counts), COLS):
        row = families_with_counts[row_start : row_start + COLS]
        cols = st.columns(COLS)

        for i, fam in enumerate(row):
            with cols[i]:
                with st.container(border=True):
                    name = fam["name"]
                    dutch = fam.get("dutch_name")
                    count = fam.get("plant_count", 0)
                    desc = fam.get("description") or ""

                    st.markdown(f"### {name}")
                    if dutch:
                        st.caption(dutch)
                    st.caption(f"🌱 {count} soort{'en' if count != 1 else ''}")

                    if desc:
                        # Toon eerste 200 tekens van de beschrijving als preview
                        preview = desc[:200].rsplit(" ", 1)[0] + "…" if len(desc) > 200 else desc
                        st.markdown(preview)

                    if st.button(
                        "Bekijk →",
                        key=f"fam_card_{name}_{row_start}_{i}",
                        width="stretch",
                    ):
                        st.query_params["family"] = name
                        st.rerun()

    st.caption(
        "Families zonder planten in de encyclopedie worden hier niet getoond. "
        "Familie-beschrijvingen kunnen worden toegevoegd via het beheerpaneel."
    )

render_footer()
