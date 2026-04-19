"""
Plantenpedia — Zoeken & filteren
Gebruikers kunnen planten zoeken op basis van meerdere eigenschappen.
"""
import streamlit as st

from utils.database import filter_plants, make_slug
from utils.display import (
    CATEGORY_LABELS,
    HARDINESS_LABELS,
    LIGHT_LABELS,
    MONTH_NAMES,
    SOIL_LABELS,
    WATER_NEEDS_LABELS,
    bloom_label,
    first_photo,
    make_slug,
)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer     {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🔍 Zoeken & filteren")

# ── Preset-knoppen ────────────────────────────────────────────────────────────
st.markdown("**Snelfilters**")

PRESETS = {
    "🌿 Inheems":         {"native_nl": True},
    "☀️ Droogtebestendig": {"drought_tolerant": True},
    "🐝 Bijentuin":       {"insect_types": ["insect"]},
    "🦋 Vlindertuin":     {"insect_types": ["vlinder"]},
    "🍽️ Eetbaar":         {"edible": True},
    "🌊 Waterplant":      {"water_needs": ["nat", "vochtig"]},
}

preset_cols = st.columns(len(PRESETS))
for col, (label, preset_filters) in zip(preset_cols, PRESETS.items()):
    with col:
        active = st.session_state.get("active_preset") == label
        if st.button(
            label,
            use_container_width=True,
            type="primary" if active else "secondary",
            key=f"preset_{label}",
        ):
            if active:
                st.session_state.pop("active_preset", None)
                st.session_state.pop("preset_filters", None)
            else:
                st.session_state["active_preset"] = label
                st.session_state["preset_filters"] = preset_filters
            st.rerun()

# ── Filterformulier ───────────────────────────────────────────────────────────
with st.expander("Geavanceerde filters", expanded=not st.session_state.get("active_preset")):
    with st.form("filter_form"):
        col1, col2, col3 = st.columns(3, gap="large")

        with col1:
            st.markdown("**Planttype**")
            selected_categories = st.multiselect(
                "Categorie",
                options=list(CATEGORY_LABELS.keys()),
                format_func=lambda x: CATEGORY_LABELS[x],
                label_visibility="collapsed",
            )

            st.markdown("**Eetbaarheid**")
            edible_choice = st.radio(
                "Eetbaar",
                ["Alle planten", "Alleen eetbare planten", "Alleen niet-eetbare planten"],
                label_visibility="collapsed",
            )

            st.markdown("**Giftigheid**")
            exclude_toxic = st.checkbox("Sluit giftige planten uit")

        with col2:
            st.markdown("**Bloeiperiode**")
            bloom_choice = st.selectbox(
                "Bloeit in maand",
                options=["Alle maanden"] + [
                    f"{m} — {MONTH_NAMES[m].capitalize()}" for m in range(1, 13)
                ],
                label_visibility="collapsed",
            )

            st.markdown("**Lichtbehoefte**")
            selected_light = st.multiselect(
                "Licht",
                options=list(LIGHT_LABELS.keys()),
                format_func=lambda x: LIGHT_LABELS[x],
                label_visibility="collapsed",
            )

            st.markdown("**Waterbehoeften**")
            selected_water = st.multiselect(
                "Water",
                options=list(WATER_NEEDS_LABELS.keys()),
                format_func=lambda x: WATER_NEEDS_LABELS[x],
                label_visibility="collapsed",
            )

        with col3:
            st.markdown("**Grondsoort**")
            selected_soils = st.multiselect(
                "Grond",
                options=list(SOIL_LABELS.keys()),
                format_func=lambda x: SOIL_LABELS[x],
                label_visibility="collapsed",
            )

            st.markdown("**Winterhardheid**")
            selected_hardiness = st.multiselect(
                "Winterhardheid",
                options=list(HARDINESS_LABELS.keys()),
                format_func=lambda x: HARDINESS_LABELS[x],
                label_visibility="collapsed",
            )

            st.markdown("**Overige eigenschappen**")
            only_evergreen    = st.checkbox("Alleen wintergroene planten")
            only_native       = st.checkbox("Alleen inheemse planten (NL/BE)")
            only_drought      = st.checkbox("Alleen droogtebestendige planten")

            st.markdown("&nbsp;")
            submitted = st.form_submit_button(
                "🔍 Zoeken", type="primary", use_container_width=True
            )

# ── Resultaten ────────────────────────────────────────────────────────────────
active_preset  = st.session_state.get("active_preset")
preset_filters = st.session_state.get("preset_filters", {})

show_results = bool(active_preset) or submitted

if show_results:
    if active_preset:
        # Preset-modus: toon actief filter als badge
        st.markdown(f"**Actief snelfilter:** {active_preset} &nbsp; "
                    f"<small>([wis filter](#))</small>",
                    unsafe_allow_html=True)
        results = filter_plants(**preset_filters)
    else:
        # Formuliermodus
        edible: bool | None = None
        if edible_choice == "Alleen eetbare planten":
            edible = True
        elif edible_choice == "Alleen niet-eetbare planten":
            edible = False

        toxic: bool | None = False if exclude_toxic else None

        bloom_month: int | None = None
        if bloom_choice != "Alle maanden":
            bloom_month = int(bloom_choice.split(" —")[0])

        results = filter_plants(
            edible=edible,
            toxic=toxic,
            bloom_month=bloom_month,
            light_needs=selected_light or None,
            soil_types=selected_soils or None,
            categories=selected_categories or None,
            evergreen=True if only_evergreen else None,
            hardiness=selected_hardiness or None,
            native_nl=True if only_native else None,
            drought_tolerant=True if only_drought else None,
            water_needs=selected_water or None,
        )

    st.divider()
    n = len(results)
    st.markdown(f"### {n} soort{'en' if n != 1 else ''} gevonden")

    if not results:
        st.info(
            "Geen planten gevonden met de opgegeven filters. "
            "Probeer minder filters te gebruiken."
        )
        st.stop()

    CARDS_PER_ROW = 4
    for row_start in range(0, len(results), CARDS_PER_ROW):
        row = results[row_start: row_start + CARDS_PER_ROW]
        cols = st.columns(CARDS_PER_ROW)

        for i, plant in enumerate(row):
            with cols[i]:
                photo = first_photo(plant)
                dutch = plant.get("dutch_names") or []
                primary = dutch[0] if dutch else plant["scientific_name"]
                cat = plant.get("category", "overig")
                slug = plant.get("slug") or make_slug(plant["scientific_name"])
                bl = bloom_label(plant.get("bloom_start"), plant.get("bloom_end"))

                with st.container(border=True):
                    if photo:
                        try:
                            st.image(photo["url"], use_container_width=True)
                        except Exception:
                            pass

                    st.markdown(f"**{primary}**")
                    st.markdown(f"*{plant['scientific_name']}*")
                    st.caption(CATEGORY_LABELS.get(cat, cat))
                    if bl != "Onbekend":
                        st.caption(f"🌸 {bl}")

                    badges = []
                    if plant.get("native_nl"):
                        badges.append("🌿 Inheems")
                    if plant.get("edible"):
                        badges.append("✅ Eetbaar")
                    if plant.get("toxic"):
                        badges.append("⚠️ Giftig")
                    if plant.get("drought_tolerant"):
                        badges.append("☀️ Droogtebestendig")
                    if badges:
                        st.caption(" · ".join(badges))

                    if st.button(
                        "Bekijk →",
                        key=f"res_{slug}_{row_start}_{i}",
                        use_container_width=True,
                    ):
                        st.query_params["plant"] = slug
                        st.switch_page("pages/1_Planten.py")

else:
    # Lege toestand — toon uitleg
    st.markdown("---")
    st.markdown(
        """
        #### Filteropties

        | Filter | Beschrijving |
        |--------|--------------|
        | **Snelfilters** | Klik een preset-knop om direct te filteren |
        | **Planttype** | Vaste plant, bol, boom, klimplant, wilde plant, etc. |
        | **Eetbaarheid** | Alleen planten waarvan (delen) eetbaar zijn |
        | **Giftigheid** | Sluit planten uit die giftig zijn |
        | **Bloeiperiode** | Welke maand wil je bloei zien? |
        | **Lichtbehoefte** | Vol zon, halfschaduw of schaduw |
        | **Waterbehoeften** | Droog, normaal, vochtig of nat |
        | **Grondsoort** | Zand, klei, leem, veen, humusrijk, etc. |
        | **Winterhardheid** | Van volledig winterhard tot vorstgevoelig |
        | **Wintergroen** | Plant behoudt zijn blad het hele jaar door |
        | **Inheems** | Inheemse soorten voor Nederland en België |
        | **Droogtebestendig** | Geschikt voor droge zomers |

        Je kunt meerdere waarden binnen een filter selecteren — dan worden alle
        planten getoond die aan *één of meer* van die waarden voldoen.
        Filters onderling worden gecombineerd met **EN**: een plant moet aan
        álle actieve filters voldoen.
        """
    )
