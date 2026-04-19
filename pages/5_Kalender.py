"""
Plantenpedia — Seizoenskalender & Tuinagenda
Tab 1: Visuele bloei-tijdlijn per plant.
Tab 2: Maand-voor-maand tuinagenda met taken en bloeiende planten.
"""
from datetime import date

import streamlit as st

from utils.database import get_all_plants
from utils.display import CATEGORY_LABELS, MONTH_NAMES, render_footer

st.title("📅 Seizoenskalender")

tab1, tab2 = st.tabs(["🌸 Bloeikalender", "📋 Tuinagenda"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — BLOEIKALENDER
# ══════════════════════════════════════════════════════════════════════════════

with tab1:
    st.caption("Bloeitijden van alle planten in één overzicht. Gebruik de filters om te verfijnen.")

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

    current_month = date.today().month
    MONTHS = list(range(1, 13))
    MONTH_SHORT = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]

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


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — TUINAGENDA
# ══════════════════════════════════════════════════════════════════════════════

AGENDA_TAKEN: dict = {
    1: {
        "emoji": "📋",
        "zaaien_binnen": [],
        "zaaien_buiten": [],
        "planten": [],
        "snoeien": ["Fruitbomen", "Klimrozen", "Heesters (lichtjes)"],
        "overig": [
            "Bestel zaden voor het nieuwe seizoen via een ecologische zaadleverancier",
            "Houd vogelvoer aangevuld — meizenbolletjes, noten en bessen",
            "Controleer opgeslagen knollen (dahlia, gladiool) op rot",
            "Leg een insectenhut aan op een zonnige, droge plek",
        ],
    },
    2: {
        "emoji": "🌱",
        "zaaien_binnen": ["Tomaten", "Paprika", "Aubergine", "Selderij"],
        "zaaien_buiten": [],
        "planten": [],
        "snoeien": ["Clematis (groep 2 & 3)", "Rozen (lichtjes terugzetten)"],
        "overig": [
            "Voeg materiaal toe aan de composthoop en keer hem om",
            "Bewonder vroege bloemen: sneeuwklokjes, helleborus en kornoelje",
            "Controleer overwinterende kuipplanten op waterbehoefte",
        ],
    },
    3: {
        "emoji": "🌿",
        "zaaien_binnen": ["Komkommer", "Courgette", "Basilicum", "Paprika"],
        "zaaien_buiten": ["Spinazie", "Radijs", "Sla (vroeg ras)"],
        "planten": ["Vaste planten", "Heesters", "Bomen (tot half maart)"],
        "snoeien": ["Vaste planten terugsnoeien (voorzichtig)", "Grassen terugknippen"],
        "overig": [
            "Mulch borders om bodemvocht vast te houden en onkruid te remmen",
            "Leg egelbeschutting aan in wilde hoek van de tuin",
            "Voeg composthoop toe met eerste vers materiaal",
        ],
    },
    4: {
        "emoji": "🌸",
        "zaaien_binnen": ["Zonnebloem", "Cosmea", "Afrikaantje"],
        "zaaien_buiten": ["Radijs", "Wortelen", "Bieten", "Peterselie"],
        "planten": ["Vaste planten", "Heesters", "Eenjarigen (na nachtvorst)"],
        "snoeien": ["Forsythia na de bloei", "Rozen licht bijsnijden"],
        "overig": [
            "Zaai eenjarigen direct buiten na de laatste nachtvorst",
            "Leg een insectenhotel aan of vernieuw de oude vulling",
            "Geef vroege groeiers een laagje rijpe compost als topdressing",
        ],
    },
    5: {
        "emoji": "🌼",
        "zaaien_binnen": ["Pompoenen", "Meloenen"],
        "zaaien_buiten": ["Zonnebloemen", "Afrikaantjes", "Cosmea", "Dille", "Koriander"],
        "planten": ["Kuipplanten (na 15 mei)", "Tomaten buiten", "Komkommer"],
        "snoeien": ["Rododendron na de bloei", "Sering na de bloei"],
        "overig": [
            "Na de ijsheiligen (12–15 mei): zet kuipplanten en tropische soorten buiten",
            "Controleer op luizen — introduceer lieveheersbeestjes als bestrijding",
            "Mulch de borders voor droge zomerweer",
        ],
    },
    6: {
        "emoji": "🦋",
        "zaaien_binnen": [],
        "zaaien_buiten": ["Tweejarigen (vingerhoedskruid, stokroos)"],
        "planten": ["Vaste planten (vroeg in de maand, nog met water)"],
        "snoeien": ["Hagen bijknippen (eerste keer)", "Uitgebloeide voorjaarsbloeiers"],
        "overig": [
            "Laat uitgebloeide planten staan — vlinders en bijen hebben de bloemen nodig",
            "Geef water vroeg in de ochtend, diep en doordringend",
            "Wied onkruid als de grond vochtig is na regen",
            "Oogst vroege kruiden: basilicum, peterselie en dille",
        ],
    },
    7: {
        "emoji": "☀️",
        "zaaien_binnen": [],
        "zaaien_buiten": ["Tweejarigen", "Sla (hittebest. ras)", "Spinazie (late zaai)"],
        "planten": [],
        "snoeien": ["Zomersnoei appels & peren", "Hagen (tweede keer)"],
        "overig": [
            "Geef diep water in lange droge periodes — focus op nieuwe aanplant",
            "Verwijder verdroogde bloemen (deadheading) voor aanhoudende bloei",
            "Oogst en droog of vries kruiden in voor de winter",
        ],
    },
    8: {
        "emoji": "🌾",
        "zaaien_binnen": [],
        "zaaien_buiten": ["Tweejarigen (stokroos, vingerhoedskruid)", "Spinazie", "Radijs"],
        "planten": ["Vaste planten (vroeg in maand met voldoende water)"],
        "snoeien": ["Heesters na de bloei", "Lavendel licht terugsnoeien na bloei"],
        "overig": [
            "Bewaar zaad van wilde planten en inheemse soorten",
            "Oogst appels en peren bij eerste rijpheid",
            "Snoei heide-soorten licht voor compact blijven",
        ],
    },
    9: {
        "emoji": "🍂",
        "zaaien_binnen": [],
        "zaaien_buiten": ["Knoflook", "Uien (winterras)"],
        "planten": ["Voorjaarsbloeiers (narcissen, tulpen, krokussen)", "Vaste planten", "Heesters", "Bomen"],
        "snoeien": ["Lichte snoei vaste planten", "Hagen (laatste keer)"],
        "overig": [
            "Verdeel en herplant vaste planten die te dicht op elkaar staan",
            "Laat zaadhoofden staan voor mezen, sijsjes en vinken",
            "Begin een nieuwe composthoop met bladeren en snoeihout",
        ],
    },
    10: {
        "emoji": "🍁",
        "zaaien_binnen": [],
        "zaaien_buiten": ["Knoflook (laatste kans)", "Winterrogge (groenbemester)"],
        "planten": ["Voorjaarsbloeiers (laatste kans)", "Bomen & heesters"],
        "snoeien": ["Fruitbomen (begin herfst)", "Rozen licht terugsnoeien"],
        "overig": [
            "Gebruik gevallen bladeren als mulch of verwerk ze tot bladcompost",
            "Haal gevoelige kuipplanten voor de vorst naar binnen (boven 5 °C)",
            "Maai gras kort om schimmel in de winter te voorkomen",
        ],
    },
    11: {
        "emoji": "❄️",
        "zaaien_binnen": [],
        "zaaien_buiten": [],
        "planten": ["Kale-wortel bomen en heesters (ideale tijd)"],
        "snoeien": ["Fruitbomen", "Rozen (grove snoei)"],
        "overig": [
            "Bescherm gevoelige vaste planten met vliesdoek of bladeren",
            "Snoei besdragende struiken nog niet — vogels eten de bessen graag",
            "Reinig en conserveer gereedschap voor de winteropslag",
        ],
    },
    12: {
        "emoji": "🐦",
        "zaaien_binnen": [],
        "zaaien_buiten": [],
        "planten": [],
        "snoeien": ["Fruitbomen (op vorstvrije dagen)", "Klimrozen"],
        "overig": [
            "Leg extra vogelvoer uit — bessen, noten en meizenbolletjes",
            "Controleer overwinterende planten op vorst- of muizenschade",
            "Laat bloemstelen staan: decoratief én overwinteringsplek voor insecten",
            "Maak een tuinplan voor het nieuwe jaar",
        ],
    },
}

with tab2:
    st.caption("Wat kun je deze maand doen in de tuin?")

    today = date.today()
    month_names_full = [MONTH_NAMES[m].capitalize() for m in range(1, 13)]
    selected_month = st.selectbox(
        "Kies een maand",
        options=list(range(1, 13)),
        index=today.month - 1,
        format_func=lambda m: f"{MONTH_NAMES[m].capitalize()}",
        label_visibility="collapsed",
    )

    agenda = AGENDA_TAKEN[selected_month]

    col_taken, col_bloei = st.columns([1, 1])

    with col_taken:
        st.markdown(f"### {agenda['emoji']} Taken in {MONTH_NAMES[selected_month].capitalize()}")

        if agenda["zaaien_binnen"]:
            st.markdown("**🌱 Zaaien binnen (voorzaaien)**")
            for item in agenda["zaaien_binnen"]:
                st.markdown(f"- {item}")

        if agenda["zaaien_buiten"]:
            st.markdown("**🌾 Zaaien buiten**")
            for item in agenda["zaaien_buiten"]:
                st.markdown(f"- {item}")

        if agenda["planten"]:
            st.markdown("**🌿 Planten & uitplanten**")
            for item in agenda["planten"]:
                st.markdown(f"- {item}")

        if agenda["snoeien"]:
            st.markdown("**✂️ Snoeien**")
            for item in agenda["snoeien"]:
                st.markdown(f"- {item}")

        if agenda["overig"]:
            st.markdown("**📋 Overige taken**")
            for item in agenda["overig"]:
                st.markdown(f"- {item}")

    with col_bloei:
        st.markdown(f"### 🌸 Nu in bloei")
        all_plants = get_all_plants()
        blooming_now = [
            p for p in all_plants
            if (p.get("bloom_start") or 13) <= selected_month <= (p.get("bloom_end") or 0)
        ]
        blooming_now.sort(key=lambda p: (
            -(p.get("score_insects") or 0),
            p.get("scientific_name", ""),
        ))

        if blooming_now:
            st.caption(f"{len(blooming_now)} soorten in bloei")
            for p in blooming_now[:30]:
                dutch = p.get("dutch_names") or []
                name = dutch[0] if dutch else p["scientific_name"]
                slug = p.get("slug", "")
                native = " 🌿" if p.get("native_nl") else ""
                score_ins = p.get("score_insects")
                bee = f" 🐝{'★' * score_ins}" if score_ins and score_ins >= 4 else ""
                st.markdown(
                    f'- <a href="/Planten?plant={slug}" target="_self">{name}</a>{native}{bee}',
                    unsafe_allow_html=True,
                )
            if len(blooming_now) > 30:
                st.caption(f"... en {len(blooming_now) - 30} meer. Zie de Bloeikalender voor het volledige overzicht.")
        else:
            st.info("Geen planten met bekende bloeitijd voor deze maand.")

render_footer()
