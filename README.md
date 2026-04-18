# Plantenpedia 🌿

Een Nederlandse plantenencyclopedie voor ecologisch hoveniers, gebouwd met [Streamlit](https://streamlit.io) en [Supabase](https://supabase.com).

**260 soorten** · vaste planten, bomen, wilde planten, bollen, kruiden, grassen en meer — elk met beschrijvingen, foto's (Wikimedia Commons), ecologische informatie en tuinadviezen.

---

## Inhoudsopgave

- [Lokaal draaien](#lokaal-draaien)
- [Projectstructuur](#projectstructuur)
- [Database opzetten](#database-opzetten)
- [Data uploaden](#data-uploaden)
- [Een plant toevoegen of bewerken](#een-plant-toevoegen-of-bewerken)
- [Bijdragen](#bijdragen)

---

## Lokaal draaien

```bash
# 1. Kloon de repository
git clone <repo-url>
cd Plantenpedia

# 2. Installeer dependencies
pip install -r requirements.txt

# 3. Maak .streamlit/secrets.toml aan (zie voorbeeld hieronder)

# 4. Start de app
streamlit run app.py
```

**`.streamlit/secrets.toml`** (niet in version control):
```toml
[supabase]
url = "https://<jouw-project>.supabase.co"
key = "<anon-key>"
service_key = "<service-role-key>"

[admin]
password = "<beheerderswachtwoord>"
```

---

## Projectstructuur

```
Plantenpedia/
├── app.py                    # App-entry: navigatie & pagina-routing
├── requirements.txt
├── schema.sql                # Volledig databaseschema (idempotent)
│
├── pages/
│   ├── Startpagina.py        # Homepage met "Soort van de dag"
│   ├── 1_Planten.py          # Encyclopedie: rasteroverzicht + detailpagina
│   ├── 2_Zoeken.py           # Geavanceerde zoek- en filterpagina
│   ├── 3_Beheer.py           # Beheerderspaneel (wachtwoord beveiligd)
│   └── 4_Families.py         # Plantenfamilies overzicht
│
├── utils/
│   ├── database.py           # Alle databasefuncties (lezen + schrijven)
│   └── display.py            # UI-helpers: labels, icons, renderfuncties
│
└── data/
    ├── upload.py             # CLI voor uploaden naar de database
    ├── seed_plants.py        # Basisgegevens (naam, categorie, bloeitijd, etc.)
    └── enrichments/          # Uitgebreide plantdata, gesplitst per categorie
        ├── _helpers.py       # wiki() en img() hulpfuncties
        ├── __init__.py       # Samenvoegen van alle categorieën
        ├── vaste_planten.py  # 60 soorten
        ├── eenjarigen.py     # 13 soorten (incl. tweejarigen)
        ├── bollen_knollen.py # 14 soorten
        ├── kuipplanten.py    #  8 soorten
        ├── wilde_planten.py  # 71 soorten (incl. waterplanten)
        ├── keukenkruiden.py  #  3 soorten
        ├── grassen.py        #  6 soorten
        ├── heesters.py       # 44 soorten (incl. wintergroene)
        ├── klimplanten.py    # 12 soorten (incl. rozen)
        └── bomen.py          # 29 soorten (incl. coniferen)
```

---

## Database opzetten

1. Maak een project aan op [supabase.com](https://supabase.com)
2. Ga naar **SQL Editor** en voer `schema.sql` uit
3. Kopieer de `anon`-key en `service_role`-key naar `secrets.toml`

Het schema is idempotent (`CREATE IF NOT EXISTS`, `ADD COLUMN IF NOT EXISTS`) — veilig om opnieuw uit te voeren op een bestaande database.

### Basisdata uploaden (nieuw project)

```bash
cd Plantenpedia

# Stap 1: Basis plantgegevens (naam, categorie, bloeitijd, licht, etc.)
SUPABASE_URL="..." SUPABASE_SERVICE_KEY="..." python data/seed_plants.py

# Stap 2: Uitgebreide informatie (beschrijvingen, foto's, ecologie)
SUPABASE_URL="..." SUPABASE_SERVICE_KEY="..." python data/upload.py
```

---

## Data uploaden

`data/upload.py` is de centrale CLI voor het uploaden van verrijkingsdata.

```bash
# Alle planten, alle velden uploaden
python data/upload.py

# Alleen foto's bijwerken voor alle planten
python data/upload.py --fields photos

# Één plant volledig bijwerken
python data/upload.py --plant "Taxus baccata"

# Alle bomen uploaden
python data/upload.py --category bomen

# Veilige modus: sla velden over die al ingevuld zijn in de DB
# (beschermt handmatige aanpassingen via het beheerderspaneel)
python data/upload.py --safe

# Toon wat er bijgewerkt zou worden zonder te schrijven
python data/upload.py --dry-run

# Combineren van opties
python data/upload.py --category wilde_planten --fields photos,ecological_value
python data/upload.py --plant "Rosa canina" --safe
```

### Beschikbare velden per plant

| Veld | Type | Beschrijving |
|------|------|-------------|
| `description` | tekst (markdown) | Uiterlijk en kenmerkende eigenschappen |
| `distribution` | tekst (markdown) | Verspreidingsgebied |
| `growth_habit` | tekst (markdown) | Groeiwijze, hoogte, spreiding |
| `family` / `family_common` | tekst | Wetenschappelijke / Nederlandse familienaam |
| `origin` | tekst | Geografische herkomst |
| `hardiness` | enum | Winterhardheid |
| `evergreen` | boolean | Wintergroen? |
| `maintenance_level` | enum | `laag` / `midden` / `hoog` |
| `ecological_value` | tekst (markdown) | Ecologische waarde |
| `insects_animals` | JSONB-lijst | Insecten en dieren die de plant bezoeken |
| `pruning_info` | tekst (markdown) | Snoeiadviezen |
| `fertilizer_needs` | tekst (markdown) | Bemestingsadvies |
| `pests_diseases` | tekst (markdown) | Plagen en ziektes |
| `weed_behavior` | tekst (markdown) | Woekerende eigenschappen |
| `photos` | JSONB-lijst | Foto's met URL, bron en bijschrift |
| `edible_parts` | tekst | Eetbare delen |
| `recipes` | tekst (markdown) | Receptideeën |
| `medicinal_uses` | tekst (markdown) | Medicinale toepassingen |
| `toxic_info` | tekst (markdown) | Giftige delen en symptomen |
| `cultivars` | JSONB-lijst | Bekende variëteiten |
| `sources` | JSONB-lijst | Literatuurverwijzingen |

---

## Een plant toevoegen of bewerken

### Via het beheerderspaneel (aanbevolen voor kleine wijzigingen)

Ga naar de app → **Beheer** → voer het wachtwoord in → gebruik de formulieren.

### Via de enrichments-bestanden (voor uitgebreide toevoegingen)

1. Open het juiste bestand in `data/enrichments/` op basis van de categorie:
   - Vaste plant → `vaste_planten.py`
   - Boom of conifeer → `bomen.py`
   - Wilde plant → `wilde_planten.py`
   - enz.

2. Voeg een nieuw item toe aan de `ENRICHMENTS`-dict:

```python
"Rosa canina": {
    "description": "De wilde roos is...",
    "growth_habit": "Breed uitgroeiende struik van 100–250 cm...",
    "family": "Rosaceae", "family_common": "Rozenfamilie",
    "origin": "Europa",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "maintenance_level": "laag",
    "ecological_value": "Bessen voeden in de herfst vogels...",
    "insects_animals": [
        {"name": "Honingbij", "type": "insect", "desirable": True,
         "description": "Bezoekt de bloemen voor nectar en stuifmeel."},
    ],
    "photos": [wiki("Rosa_canina_003.jpg", "Hondsroos in bloei")],
},
```

3. Upload de wijziging:

```bash
python data/upload.py --plant "Rosa canina"
```

### Een foto vervangen

```bash
# Alleen de foto van één plant bijwerken
python data/upload.py --plant "Rosa canina" --fields photos
```

Gebruik [Wikimedia Commons](https://commons.wikimedia.org) om een geschikte foto te vinden.
Het bestandsnaam gaat in `wiki("Bestandsnaam.jpg", "Bijschrift")`.

---

## Bijdragen

Pull requests zijn welkom! Houd bij het toevoegen van planten rekening met:

- **Wetenschappelijke naam** als sleutel (met hoofdletter genus, kleine letters species)
- **Beschrijvingen** in het Nederlands, gericht op ecologisch bewuste tuiniers
- **Foto's** uitsluitend van Wikimedia Commons (CC-licentie)
- **`insects_animals`**: gebruik `"type": "insect"` / `"vlinder"` / `"vogel"` / `"zoogdier"`
- **`hardiness`**: kies uit `volledig_winterhard` / `winterhard` / `matig_winterhard` / `vorstgevoelig` / `niet_winterhard`
- **`maintenance_level`**: kies `laag` / `midden` / `hoog`
