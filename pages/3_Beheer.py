"""
Plantenpedia — Beheerpaneel (admin)
Beheer planten, plan de soort van de dag in en bewerk artikelen.
Toegang beveiligd met wachtwoord uit st.secrets.
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from typing import Any, Dict

import streamlit as st

from utils.database import (
    delete_family,
    delete_plant,
    get_all_families,
    get_all_plants,
    get_family,
    get_plant_by_id,
    get_pod_schedule,
    remove_pod_schedule,
    schedule_plant_of_day,
    upsert_family,
    upsert_plant,
)
from utils.display import (
    CATEGORY_LABELS,
    HARDINESS_LABELS,
    LIGHT_LABELS,
    MONTH_NAMES,
    SOIL_LABELS,
)

st.set_page_config(
    page_title="Beheer — Plantenpedia",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
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

# ── Authenticatie ─────────────────────────────────────────────────────────────

def check_password() -> bool:
    if st.session_state.get("admin_ok"):
        return True

    st.title("🔒 Admin login")
    with st.form("login"):
        pwd = st.text_input("Wachtwoord", type="password")
        if st.form_submit_button("Inloggen", type="primary"):
            expected = st.secrets.get("admin", {}).get("password", "")
            if pwd == expected:
                st.session_state["admin_ok"] = True
                st.rerun()
            else:
                st.error("Onjuist wachtwoord.")
    return False


if not check_password():
    st.stop()

# ── Header ────────────────────────────────────────────────────────────────────
col_h, col_out = st.columns([5, 1])
with col_h:
    st.title("⚙️ Beheerpaneel")
with col_out:
    if st.button("Uitloggen", use_container_width=True):
        st.session_state["admin_ok"] = False
        st.rerun()

# ── Tabbladen ─────────────────────────────────────────────────────────────────
tab_pod, tab_edit, tab_new, tab_del, tab_fam = st.tabs([
    "🌸 Soort van de dag",
    "📝 Plant bewerken",
    "➕ Plant toevoegen",
    "🗑️ Plant verwijderen",
    "🌿 Plantenfamilies",
])

# ════════════════════════════════════════════════════════════════
# TAB 1 — Soort van de dag
# ════════════════════════════════════════════════════════════════
with tab_pod:
    st.header("Soort van de dag beheren")

    today = date.today()
    schedule = get_pod_schedule(days=14)

    st.subheader("Planning komende 14 dagen")
    for i in range(14):
        d = today + timedelta(days=i)
        d_str = d.isoformat()
        label = "Vandaag" if i == 0 else ("Morgen" if i == 1 else d.strftime("%A %d %b"))
        entry = schedule.get(d_str)

        col_lbl, col_plant, col_btn = st.columns([2, 4, 1])
        with col_lbl:
            st.markdown(f"**{label}**")
        with col_plant:
            if entry and entry.get("plants"):
                p = entry["plants"]
                dutch = (p.get("dutch_names") or [""])[0]
                st.markdown(f"📌 {dutch or p['scientific_name']} *(handmatig)*")
            else:
                st.markdown("*Automatisch geselecteerd*")
        with col_btn:
            if entry and st.button("Verwijder", key=f"del_pod_{d_str}"):
                if remove_pod_schedule(d):
                    st.success("Inplanning verwijderd.")
                    st.rerun()

    st.divider()
    st.subheader("Nieuwe inplanning toevoegen")

    all_plants_list = get_all_plants("id, scientific_name, dutch_names")
    plant_opts = {
        p["id"]: f"{p['scientific_name']} ({', '.join(p.get('dutch_names') or [])})"
        for p in all_plants_list
    }

    with st.form("pod_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            sched_date = st.date_input(
                "Datum", value=today + timedelta(days=1), min_value=today
            )
        with col_b:
            selected_id = st.selectbox(
                "Plant",
                options=list(plant_opts.keys()),
                format_func=lambda x: plant_opts.get(x, x),
            )
        notes = st.text_input("Notitie (optioneel)")

        if st.form_submit_button("Inplannen", type="primary"):
            if schedule_plant_of_day(selected_id, sched_date, "admin", notes):
                st.success(f"✅ Ingepland voor {sched_date.strftime('%d %B %Y')}.")
                st.rerun()


# ════════════════════════════════════════════════════════════════
# Gedeelde formulierfunctie
# ════════════════════════════════════════════════════════════════

def _json_field(label: str, value: Any, height: int = 120) -> Any:
    """Toont een JSON-tekstgebied en parseert de inhoud. Geeft None bij parsefout."""
    raw = st.text_area(
        label,
        value=json.dumps(value or [], indent=2, ensure_ascii=False),
        height=height,
        help="Gebruik geldig JSON-formaat.",
    )
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        st.error(f"Ongeldige JSON in '{label}': {e}")
        return None


def render_plant_form(plant: Dict, form_key: str) -> None:
    """Render het bewerkingsformulier voor een plant."""
    with st.form(form_key):
        st.subheader("Identificatie")
        c1, c2 = st.columns(2)
        with c1:
            sci = st.text_input(
                "Wetenschappelijke naam *",
                value=plant.get("scientific_name", ""),
            )
        with c2:
            dutch_raw = st.text_input(
                "Nederlandse namen (kommagescheiden)",
                value=", ".join(plant.get("dutch_names") or []),
            )

        c3, c4 = st.columns(2)
        with c3:
            cat_keys = list(CATEGORY_LABELS.keys())
            current_cat = plant.get("category", "overig")
            cat_idx = cat_keys.index(current_cat) if current_cat in cat_keys else 0
            category = st.selectbox(
                "Categorie *",
                options=cat_keys,
                format_func=lambda x: CATEGORY_LABELS[x],
                index=cat_idx,
            )
        with c4:
            growth_habit = st.text_input(
                "Groeiwijze (vast/eenjarig/tweejarig/…)",
                value=plant.get("growth_habit") or "",
            )

        c_fam1, c_fam2, c_orig = st.columns(3)
        with c_fam1:
            family = st.text_input(
                "Plantenfamilie (wetenschappelijk)",
                value=plant.get("family") or "",
                placeholder="bv. Asteraceae",
            )
        with c_fam2:
            family_common = st.text_input(
                "Plantenfamilie (Nederlands)",
                value=plant.get("family_common") or "",
                placeholder="bv. Composietenfamilie",
            )
        with c_orig:
            origin = st.text_input(
                "Herkomst / verspreidingsgebied",
                value=plant.get("origin") or "",
                placeholder="bv. Europa, West-Azië",
            )

        c_hard, c_eg = st.columns(2)
        with c_hard:
            hard_opts = [""] + list(HARDINESS_LABELS.keys())
            curr_hard = plant.get("hardiness") or ""
            hard_idx = hard_opts.index(curr_hard) if curr_hard in hard_opts else 0
            hardiness = st.selectbox(
                "Winterhardheid",
                options=hard_opts,
                format_func=lambda x: HARDINESS_LABELS.get(x, "— Selecteer —") if x else "— Selecteer —",
                index=hard_idx,
            )
        with c_eg:
            st.markdown("&nbsp;")
            evergreen = st.checkbox(
                "🌲 Wintergroen (behoudt blad het hele jaar)",
                value=bool(plant.get("evergreen")),
            )

        st.subheader("Basisinformatie")
        description = st.text_area(
            "Beschrijving (markdown)", value=plant.get("description") or "", height=180
        )
        distribution = st.text_area(
            "Verspreidingsgebied (markdown)", value=plant.get("distribution") or "", height=100
        )

        c5, c6, c7, c8 = st.columns(4)
        with c5:
            bloom_start = st.number_input(
                "Bloei start (maand 1–12)", min_value=0, max_value=12,
                value=plant.get("bloom_start") or 0,
            )
        with c6:
            bloom_end = st.number_input(
                "Bloei einde (maand 1–12)", min_value=0, max_value=12,
                value=plant.get("bloom_end") or 0,
            )
        with c7:
            height_min = st.number_input(
                "Min. hoogte (cm)", min_value=0, value=plant.get("height_min") or 0
            )
        with c8:
            height_max = st.number_input(
                "Max. hoogte (cm)", min_value=0, value=plant.get("height_max") or 0
            )

        st.subheader("Behoeftes")
        c9, c10 = st.columns(2)
        with c9:
            light_opts = [""] + list(LIGHT_LABELS.keys())
            curr_light = plant.get("light_needs") or ""
            light_idx = light_opts.index(curr_light) if curr_light in light_opts else 0
            light_needs = st.selectbox(
                "Lichtbehoefte",
                options=light_opts,
                format_func=lambda x: LIGHT_LABELS.get(x, "— Selecteer —") if x else "— Selecteer —",
                index=light_idx,
            )
        with c10:
            soil_types = st.multiselect(
                "Grondsoorten",
                options=list(SOIL_LABELS.keys()),
                format_func=lambda x: SOIL_LABELS[x],
                default=plant.get("soil_types") or [],
            )

        fertilizer_needs = st.text_area(
            "Voeding & bemesting (markdown)", value=plant.get("fertilizer_needs") or "", height=100
        )
        pruning_info = st.text_area(
            "Snoeien (markdown)", value=plant.get("pruning_info") or "", height=100
        )
        weed_behavior = st.text_area(
            "Woekerende eigenschappen (markdown)", value=plant.get("weed_behavior") or "", height=100
        )
        pests_diseases = st.text_area(
            "Plagen & ziektes (markdown)", value=plant.get("pests_diseases") or "", height=100
        )
        ecological_value = st.text_area(
            "Ecologische waarde (markdown)", value=plant.get("ecological_value") or "", height=100
        )

        st.subheader("Relatie met de mens")
        c11, c12 = st.columns(2)
        with c11:
            edible = st.checkbox("Eetbaar", value=bool(plant.get("edible")))
        with c12:
            toxic = st.checkbox("Giftig", value=bool(plant.get("toxic")))

        edible_parts = st.text_input(
            "Eetbare delen", value=plant.get("edible_parts") or ""
        )
        taste = st.text_input("Smaak", value=plant.get("taste") or "")
        recipes = st.text_area(
            "Recepten & bereiding (markdown)", value=plant.get("recipes") or "", height=100
        )
        nutritional_value = st.text_area(
            "Voedingswaarden (markdown)", value=plant.get("nutritional_value") or "", height=80
        )
        toxic_info = st.text_area(
            "Giftigheid — toelichting (markdown)", value=plant.get("toxic_info") or "", height=100
        )
        medicinal_uses = st.text_area(
            "Medicinale toepassingen (markdown)", value=plant.get("medicinal_uses") or "", height=100
        )
        wood_properties = st.text_area(
            "Houteigenschappen (markdown)", value=plant.get("wood_properties") or "", height=80
        )
        other_uses = st.text_area(
            "Overige toepassingen (markdown)", value=plant.get("other_uses") or "", height=80
        )

        st.subheader("Media & metadata (JSON)")
        st.markdown(
            "Foto's, cultivars, verwisselingen en bronnen worden opgeslagen als JSON. "
            "Klik op de help-iconen voor het verwachte formaat."
        )

        with st.expander("📷 Foto's — JSON"):
            st.caption(
                'Formaat: `[{"type": "bloeiwijze", "url": "https://...", '
                '"source": "Wikimedia Commons", "license": "CC BY-SA 4.0", "caption": "..."}]`\n\n'
                'Typen: `jonge_plant` · `bloeiwijze` · `zaad` · `habitus` · `blad` · `stam` · `vrucht` · `algemeen`'
            )
            photos_val = _json_field("Foto's", plant.get("photos"), height=200)

        with st.expander("🌱 Cultivars — JSON"):
            st.caption(
                'Formaat: `[{"name": "\'Atropurpureum\'", "description": "...", '
                '"photo_url": "https://...", "photo_source": "..."}]`'
            )
            cultivars_val = _json_field("Cultivars", plant.get("cultivars"), height=150)

        with st.expander("👀 Verwisselingen — JSON"):
            st.caption(
                'Formaat: `[{"name": "Gevlekte scheerling", '
                '"difference": "...", "photo_url": "..."}]`'
            )
            lookalikes_val = _json_field("Verwisselingen", plant.get("lookalikes"), height=120)

        with st.expander("🦋 Insecten & dieren — JSON"):
            st.caption(
                'Formaat: `[{"name": "Honingbij", "type": "insect", '
                '"desirable": true, "description": "..."}]`'
            )
            insects_val = _json_field("Insecten & dieren", plant.get("insects_animals"), height=120)

        with st.expander("📚 Bronnen — JSON"):
            st.caption(
                'Formaat: `[{"title": "Flora van Nederland", '
                '"url": "https://...", "description": "..."}]`'
            )
            sources_val = _json_field("Bronnen", plant.get("sources"), height=150)

        submitted = st.form_submit_button("💾 Opslaan", type="primary")

    if submitted:
        if not sci.strip():
            st.error("Wetenschappelijke naam is verplicht.")
            return

        # Controleer of JSON-velden correct zijn geparsed
        json_fields = {
            "photos": photos_val,
            "cultivars": cultivars_val,
            "lookalikes": lookalikes_val,
            "insects_animals": insects_val,
            "sources": sources_val,
        }
        if any(v is None for v in json_fields.values()):
            st.error("Herstel de JSON-fouten hierboven voordat je opslaat.")
            return

        data: Dict = {
            "scientific_name": sci.strip(),
            "dutch_names": [n.strip() for n in dutch_raw.split(",") if n.strip()],
            "category": category,
            "family": family.strip() or None,
            "family_common": family_common.strip() or None,
            "origin": origin.strip() or None,
            "hardiness": hardiness or None,
            "evergreen": evergreen,
            "growth_habit": growth_habit.strip() or None,
            "description": description.strip() or None,
            "distribution": distribution.strip() or None,
            "bloom_start": int(bloom_start) or None,
            "bloom_end": int(bloom_end) or None,
            "height_min": int(height_min) or None,
            "height_max": int(height_max) or None,
            "light_needs": light_needs or None,
            "soil_types": soil_types,
            "fertilizer_needs": fertilizer_needs.strip() or None,
            "pruning_info": pruning_info.strip() or None,
            "weed_behavior": weed_behavior.strip() or None,
            "pests_diseases": pests_diseases.strip() or None,
            "ecological_value": ecological_value.strip() or None,
            "edible": edible,
            "toxic": toxic,
            "edible_parts": edible_parts.strip() or None,
            "taste": taste.strip() or None,
            "recipes": recipes.strip() or None,
            "nutritional_value": nutritional_value.strip() or None,
            "toxic_info": toxic_info.strip() or None,
            "medicinal_uses": medicinal_uses.strip() or None,
            "wood_properties": wood_properties.strip() or None,
            "other_uses": other_uses.strip() or None,
            **json_fields,
        }

        # Bewaar het bestaande ID als we een bestaande plant bijwerken
        if plant.get("id"):
            data["id"] = plant["id"]

        result = upsert_plant(data)
        if result:
            st.success(f"✅ **{sci}** succesvol opgeslagen!")
        else:
            st.error("Opslaan mislukt. Controleer de foutmelding hierboven.")


# ════════════════════════════════════════════════════════════════
# TAB 2 — Plant bewerken
# ════════════════════════════════════════════════════════════════
with tab_edit:
    st.header("Bestaande plant bewerken")

    all_p = get_all_plants("id, scientific_name, dutch_names, category")
    edit_opts: Dict[str, str] = {
        p["id"]: f"{p['scientific_name']}  ({', '.join(p.get('dutch_names') or [])})"
        for p in all_p
    }

    selected = st.selectbox(
        "Selecteer een plant",
        options=[""] + list(edit_opts.keys()),
        format_func=lambda x: edit_opts.get(x, "— Selecteer een plant —"),
    )

    if selected:
        plant_data = get_plant_by_id(selected)
        if plant_data:
            render_plant_form(plant_data, form_key=f"edit_{selected}")
        else:
            st.warning("Plant niet gevonden.")


# ════════════════════════════════════════════════════════════════
# TAB 3 — Plant toevoegen
# ════════════════════════════════════════════════════════════════
with tab_new:
    st.header("Nieuwe plant toevoegen")
    render_plant_form({}, form_key="new_plant")


# ════════════════════════════════════════════════════════════════
# TAB 4 — Plant verwijderen
# ════════════════════════════════════════════════════════════════
with tab_del:
    st.header("Plant verwijderen")
    st.warning(
        "⚠️ **Let op:** verwijderen is onomkeerbaar. "
        "Alle gegevens van de plant worden permanent gewist."
    )

    all_p2 = get_all_plants("id, scientific_name, dutch_names")
    del_opts: Dict[str, str] = {
        p["id"]: f"{p['scientific_name']}  ({', '.join(p.get('dutch_names') or [])})"
        for p in all_p2
    }

    del_id = st.selectbox(
        "Selecteer de te verwijderen plant",
        options=[""] + list(del_opts.keys()),
        format_func=lambda x: del_opts.get(x, "— Selecteer een plant —"),
    )

    if del_id:
        st.error(f"Je staat op het punt **{del_opts[del_id]}** te verwijderen.")
        confirm = st.checkbox("Ik begrijp dat dit onomkeerbaar is.")
        if confirm:
            if st.button("🗑️ Definitief verwijderen", type="primary"):
                if delete_plant(del_id):
                    st.success("Plant verwijderd.")
                    st.rerun()


# ════════════════════════════════════════════════════════════════
# TAB 5 — Plantenfamilies beheren
# ════════════════════════════════════════════════════════════════
with tab_fam:
    st.header("Plantenfamilies beheren")
    st.markdown(
        "Voeg hier beschrijvingen toe aan plantenfamilies. "
        "De familienaam koppelt automatisch aan planten die dezelfde waarde hebben in het veld 'Plantenfamilie'."
    )

    all_families = get_all_families()

    # ── Bestaande families bewerken ──────────────────────────────
    if all_families:
        st.subheader("Bestaande families")
        fam_opts: Dict[str, str] = {
            f["id"]: f"{f['name']}" + (f" — {f['dutch_name']}" if f.get("dutch_name") else "")
            for f in all_families
        }
        sel_fam = st.selectbox(
            "Selecteer een familie",
            options=[""] + list(fam_opts.keys()),
            format_func=lambda x: fam_opts.get(x, "— Selecteer —"),
            key="sel_fam_edit",
        )

        if sel_fam:
            fam = next((f for f in all_families if f["id"] == sel_fam), {})
            with st.form("fam_edit_form"):
                fn = st.text_input("Familienaam (wetenschappelijk)", value=fam.get("name", ""))
                fd = st.text_input("Familienaam (Nederlands)", value=fam.get("dutch_name") or "")
                fd_desc = st.text_area(
                    "Beschrijving (markdown)", value=fam.get("description") or "", height=200
                )
                c_save, c_del = st.columns(2)
                save_fam = c_save.form_submit_button("💾 Opslaan", type="primary")
                del_fam = c_del.form_submit_button("🗑️ Verwijderen")

            if save_fam:
                result = upsert_family({
                    "id": fam["id"],
                    "name": fn.strip(),
                    "dutch_name": fd.strip() or None,
                    "description": fd_desc.strip() or None,
                })
                if result:
                    st.success(f"✅ Familie **{fn}** opgeslagen!")
                    st.rerun()

            if del_fam:
                if delete_family(fam["id"]):
                    st.success("Familie verwijderd.")
                    st.rerun()

    st.divider()

    # ── Nieuwe familie toevoegen ─────────────────────────────────
    st.subheader("Nieuwe familie toevoegen")
    with st.form("fam_new_form"):
        new_fn = st.text_input("Familienaam (wetenschappelijk) *", placeholder="bv. Asteraceae")
        new_fd = st.text_input("Familienaam (Nederlands)", placeholder="bv. Composietenfamilie")
        new_desc = st.text_area("Beschrijving (markdown)", height=200)
        if st.form_submit_button("➕ Familie aanmaken", type="primary"):
            if not new_fn.strip():
                st.error("Familienaam is verplicht.")
            else:
                result = upsert_family({
                    "name": new_fn.strip(),
                    "dutch_name": new_fd.strip() or None,
                    "description": new_desc.strip() or None,
                })
                if result:
                    st.success(f"✅ Familie **{new_fn}** aangemaakt!")
                    st.rerun()
