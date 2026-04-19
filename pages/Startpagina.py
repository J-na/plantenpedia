"""
Plantenpedia — Startpagina
Toont de 'Soort van de dag' en biedt navigatie naar de rest van de app.
"""
from datetime import date

import streamlit as st

from utils.database import get_plant_of_day, get_top_insects_this_month
from utils.display import (
    CATEGORY_LABELS,
    MONTH_NAMES,
    bloom_label,
    first_photo,
    make_slug,
    render_footer,
)

MONTHLY_TASKS: dict = {
    1: {
        "emoji": "📋",
        "taken": [
            "Bestel zaden voor het nieuwe seizoen via een ecologische zaadleverancier",
            "Snoei fruitbomen en klimrozen op droge, vorstvrije dagen",
            "Houd vogelvoer aangevuld — behangselpapier, meizenbolletjes en ongebrande noten",
            "Controleer opgeslagen knollen (dahlia, gladiool) op rot",
        ],
    },
    2: {
        "emoji": "🌱",
        "taken": [
            "Zaai tomaten, paprika en aubergine binnen op een warme vensterbank (>18 °C)",
            "Snoei Clematis groep 2 en 3 voor de knoppen uitlopen",
            "Voeg materiaal toe aan de composthoop en keer hem om",
            "Bewonder vroege bloemen: sneeuwklokjes, helleborus en kornoelje",
        ],
    },
    3: {
        "emoji": "🌿",
        "taken": [
            "Snoei vaste planten terug — laat dood materiaal staan tot je nieuwe scheuten ziet",
            "Zaai kruiden en eenjarigen onder glas of op een warme vensterbank",
            "Mulch borders om bodemvocht vast te houden en onkruid te remmen",
            "Plant nieuwe vaste planten — de grond is actief maar nog niet te droog",
        ],
    },
    4: {
        "emoji": "🌸",
        "taken": [
            "Zaai eenjarigen direct buiten na de laatste nachtvorst (let op lokale weersvoorspelling)",
            "Verdeel en herplant vaste planten die te groot zijn geworden",
            "Leg een insectenhotel aan of vernieuw de oude vulling",
            "Geef vroege groeiers een laagje rijpe compost als topdressing",
        ],
    },
    5: {
        "emoji": "🌼",
        "taken": [
            "Na de ijsheiligen (12–15 mei): zet kuipplanten en tropische soorten buiten",
            "Zaai zomerbloemen: zonnebloemen, afrikaantjes, cosmea en tagetes",
            "Controleer op luizen — introduceer lieveheersbeestjes als biologische bestrijding",
            "Mulch de borders voor droge zomerweer",
        ],
    },
    6: {
        "emoji": "🦋",
        "taken": [
            "Laat uitgebloeide planten staan — vlinders en bijen hebben de bloemen nodig",
            "Geef water vroeg in de ochtend, diep en doordringend — liever 1× per week dan dagelijks",
            "Wied onkruid als de grond vochtig is na regen",
            "Oogst vroege kruiden: basilicum, peterselie en dille",
        ],
    },
    7: {
        "emoji": "☀️",
        "taken": [
            "Geef diep water in lange droge periodes — focus op nieuwe aanplant",
            "Verwijder verdroogde bloemen (deadheading) voor aanhoudende bloei",
            "Zomersnoei voor appels en peren: verwijder overtollige scheuten",
            "Oogst en droog of vries kruiden in voor de winter",
        ],
    },
    8: {
        "emoji": "🌾",
        "taken": [
            "Zaai tweejarigen (vingerhoedskruid, stokroos) voor bloei volgend jaar",
            "Snoei heide-soorten licht na de bloei voor compact blijven",
            "Bewaar zaad van wilde planten en inheemse soorten",
            "Oogst appels en peren bij eerste rijpheid — wacht niet te lang",
        ],
    },
    9: {
        "emoji": "🍂",
        "taken": [
            "Plant voorjaarsbloeiers: narcissen, tulpen, krokussen en sneeuwklokjes",
            "Verdeel en herplant vaste planten die te dicht op elkaar staan",
            "Laat zaadhoofden staan voor mezen, sijsjes en vinken",
            "Begin een nieuwe composthoop met bladeren en snoeihout",
        ],
    },
    10: {
        "emoji": "🍁",
        "taken": [
            "Laatste kans voor bollenplanting voor de vorst erin zit",
            "Gebruik gevallen bladeren als mulch of verwerk ze tot bladcompost",
            "Haal gevoelige kuipplanten voor de vorst naar binnen (boven 5 °C)",
            "Maai gras kort om schimmel in de winter te voorkomen",
        ],
    },
    11: {
        "emoji": "❄️",
        "taken": [
            "Bescherm gevoelige vaste planten met vliesdoek of een dikke laag bladeren",
            "Snoei besdragende struiken nog niet — vogels eten de bessen graag",
            "Reinig en conserveer gereedschap voor de winteropslag",
            "Blader door catalogi en plan aankopen voor komend voorjaar",
        ],
    },
    12: {
        "emoji": "🐦",
        "taken": [
            "Leg extra vogelvoer uit — bessen, noten en meizenbolletjes voor wintervogels",
            "Controleer overwinterende planten op vorst- of muizenschade",
            "Laat bloemstelen staan: de structuur is decoratief en dieren overwinteren erin",
            "Maak een tuinplan voor het nieuwe jaar",
        ],
    },
}

# ── Globale CSS ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
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
                st.image(photo["url"], width="stretch")
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

# ── Wat te doen deze maand? ───────────────────────────────────────────────────
month_data = MONTHLY_TASKS[today.month]
st.markdown(f"## {month_data['emoji']} Wat te doen in {MONTH_NAMES[today.month].capitalize()}?")

task_cols = st.columns(2)
tasks = month_data["taken"]
half = (len(tasks) + 1) // 2
with task_cols[0]:
    for task in tasks[:half]:
        st.markdown(f"- {task}")
with task_cols[1]:
    for task in tasks[half:]:
        st.markdown(f"- {task}")

st.divider()

# ── Top 5 voor bijen ──────────────────────────────────────────────────────────
st.markdown(f"## 🐝 Top 5 voor bijen in {MONTH_NAMES[today.month].capitalize()}")
st.caption("Planten die nu bloeien én de meeste waarde hebben voor bijen en insecten.")

top_bijen = get_top_insects_this_month(today.month, limit=5)
if top_bijen:
    bee_cols = st.columns(5)
    for col, p in zip(bee_cols, top_bijen):
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
            score = p.get("score_insects")
            stars = ("★" * score + "☆" * (5 - score)) if score else ""
            native = " 🌿" if p.get("native_nl") else ""
            st.markdown(
                f"**[{name}](/Planten?plant={slug})**{native}  \n"
                f"*{p['scientific_name']}*  \n"
                f"{stars}"
            )
else:
    st.info(f"Geen bloeiende planten gevonden voor {MONTH_NAMES[today.month]}.")

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
        st.markdown("### 📅 Seizoenskalender")
        st.markdown(
            "Bekijk welke planten wanneer bloeien in een visuele 12-maanden "
            "tijdlijn, met per maand een overzicht van tuintaken."
        )
        st.page_link("pages/5_Kalender.py", label="Ga naar kalender →", icon="📅")

with nav4:
    with st.container(border=True):
        st.markdown("### 🌻 Mijn Tuin")
        st.markdown(
            "Sla je favoriete planten op en bekijk wanneer jouw tuin bloeit, "
            "welke maand de piek is en hoeveel bijenwaarde je hebt."
        )
        st.page_link("pages/6_MijnTuin.py", label="Ga naar mijn tuin →", icon="🌻")

nav5, nav6, nav7, _ = st.columns(4, gap="medium")

with nav5:
    with st.container(border=True):
        st.markdown("### ⚖️ Vergelijk")
        st.markdown(
            "Selecteer 2 tot 4 planten en vergelijk ze naast elkaar op hoogte, "
            "bloeitijd, licht, bodem en ecologische waarde."
        )
        st.page_link("pages/7_Vergelijk.py", label="Ga naar vergelijk →", icon="⚖️")

with nav6:
    with st.container(border=True):
        st.markdown("### 🌿 Plantenfamilies")
        st.markdown(
            "Verken planten per botanische familie. Lees over gemeenschappelijke "
            "kenmerken en ontdek verwante soorten."
        )
        st.page_link("pages/4_Families.py", label="Ga naar families →", icon="🌿")

with nav7:
    with st.container(border=True):
        st.markdown("### ⚙️ Beheer")
        st.markdown(
            "Bewerk plantartikelen, voeg nieuwe soorten toe en plan de soort "
            "van de dag in als administrator."
        )
        st.page_link("pages/3_Beheer.py", label="Ga naar beheer →", icon="⚙️")

render_footer()
