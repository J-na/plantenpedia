"""
Plantenpedia — Verrijkingsdata: Grassen

Voeg nieuwe planten toe door een nieuw item aan ENRICHMENTS toe te voegen:

    "Wetenschappelijke naam": {
        "description": "...",
        "photos": [wiki("Bestandsnaam.jpg", "Bijschrift")],
        ...
    },

Zie data/enrichments/__init__.py voor alle beschikbare velden.
Gebruik `python data/upload.py --help` om te uploaden.
"""
from ._helpers import wiki, img  # noqa: F401

ENRICHMENTS: dict = {

"Calamagrostis x acutiflora": {
    "description": "Struisriet is het meest elegante siergras van de tuin: de opgaande, stijve stengels van 120–180 cm met pluimachtige aren bewegen sierlijk in de wind en blijven het hele jaar door decoratief — ook in de winter als ze goudgeel kleuren.",
    "distribution": "Tuinhybride (C. arundinacea × C. stricta); in Nederland populair in moderne border- en prairie-ontwerpen.",
    "growth_habit": "Siersgras van 120–180 cm; bloeit in juni–juli, sierlijk door de winter.",
    "ecological_value": "De aren voeden zangvogels (sijsjes, vinken) in de winter.",
    "fertilizer_needs": "Weinig voeding; groeit op brede range van grondsoorten.",
    "pruning_info": "Pas in het vroege voorjaar (februari–maart) terugknippen voor nieuwe groei.",
    "maintenance_level": "laag",
    "family": "Poaceae", "family_common": "Grassenfamilie",
    "origin": "Hybride (Europa)",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Calamagrostis_x_acutiflora_'Karl_Foerster'.jpg", "Struisriet")],
},

"Festuca glauca": {
    "description": "Blauw schapengras is een compact, bolvormig siersgras van 20–30 cm met opvallend blauwgrijze, naaldachtige halmen. Het groeit in compacte pollen die maandenlang sierlijk zijn en droogtebestendig zijn op zandige, zonnige plekken.",
    "distribution": "Inheems op droge rotshellingen in het Mediterraan gebied en de Alpen; in Nederland populair op droge borders en groene daken.",
    "growth_habit": "Immergroen siergras van 20–30 cm; compacte, bolvormige pollen.",
    "ecological_value": "Biedt schuilplaats voor kleine insecten en spinnen; wintergroen decor.",
    "fertilizer_needs": "Geen bemesting; arme, droge, goed doorlatende grond.",
    "pruning_info": "In het vroege voorjaar licht terugknippen; splits de pol elke 3 jaar.",
    "maintenance_level": "laag",
    "family": "Poaceae", "family_common": "Grassenfamilie",
    "origin": "Mediterraan gebied en Alpen",
    "hardiness": "volledig_winterhard", "evergreen": True,
    "photos": [wiki("Festuca_glauca.jpg", "Blauw schapengras")],
},

"Pennisetum alopecuroides": {
    "description": "Lampenpoetsersgras is een bijzonder siergras met pluizige, paarsgrijze aren die in de zomerwind bewegen als kleine lampenpoetsers. Van augustus tot diep in de winter blijft het gras sierlijk staan met zijn goudkleurig verdroogde pluimen.",
    "distribution": "Inheems in Azië en Australië; in Nederland populair in moderne borders en parkbeplanting.",
    "growth_habit": "Siergras van 60–100 cm; bloeit in augustus–oktober.",
    "ecological_value": "De pluimen bieden zaden voor vogels; de compacte pol biedt schuilplaats voor kleine insecten.",
    "fertilizer_needs": "Weinig voeding; goed doorlatende, zonnige standplaats.",
    "pruning_info": "Pas in het vroege voorjaar terugknippen — de winterpluimen zijn decoratief.",
    "maintenance_level": "laag",
    "family": "Poaceae", "family_common": "Grassenfamilie",
    "origin": "Azië en Australië",
    "hardiness": "winterhard", "evergreen": False,
    "photos": [wiki("Pennisetum_alopecuroides.jpg", "Lampenpoetsersgras")],
},

"Carex buchananii": {
    "description": "Deze zegge valt op door zijn brons-koperkleurige, naaldachtige halmen die het hele jaar door warmte en textuur aan de border geven. Siergrassen als deze New Zealand Hair Sedge brengen een architectonisch, modern element in de tuin.",
    "distribution": "Inheems in Nieuw-Zeeland; in Nederland populair als siergras in borders en potten.",
    "growth_habit": "Immergroen siergras van 30–60 cm; compacte bolvormige pollen.",
    "ecological_value": "Biedt schuilplaats voor kleine insecten; de compacte pol biedt winterstructuur.",
    "fertilizer_needs": "Humusrijke, matig vochtige grond; goed doorlatend.",
    "pruning_info": "Dode halmen in het voorjaar verwijderen; nauwelijks snoei nodig.",
    "maintenance_level": "laag",
    "family": "Cyperaceae", "family_common": "Zeggenfamilie",
    "origin": "Nieuw-Zeeland",
    "hardiness": "winterhard", "evergreen": True,
    "photos": [wiki("Carex_buchananii_-_Botanischer_Garten_München-Nymphenburg_-_DSC07706.JPG", "Bronskleurige zegge")],
},

"Cortaderia selloana": {
    "description": "Pampasgras is een indrukwekkend siergras met reusachtige, zilverwitte pluimen op stelen van 150–300 cm die in augustus–oktober verschijnen en tot diep in de winter decoratief blijven. De messcherpe bladeren zijn gevaarlijk bij snoeien — altijd handschoenen dragen.",
    "distribution": "Inheems in de Zuid-Amerikaanse pampa; in Nederland populair als solitair siergras.",
    "growth_habit": "Immergroen siergras van 150–300 cm; bloeit in augustus–oktober.",
    "ecological_value": "De grote pluimen bieden nestmateriaal voor vogels; insecten gebruiken de holtes in de pol.",
    "maintenance_level": "midden",
    "family": "Poaceae", "family_common": "Grassenfamilie",
    "origin": "Zuid-Amerika",
    "hardiness": "matig_winterhard", "evergreen": True,
    "photos": [wiki("Cortaderia_selloana,_Reynerie_2017.jpg", "Pampasgras")],
},

"Molinia caerulea": {
    "description": "Pijpenstrootje is het siergras van de Nederlandse heidevelden en vennen: sierlijke, opwaartse pluimen van 60–120 cm kleuren in het najaar goudgeel en bewegen zachtjes in de wind. Een must voor natte, zure standplaatsen.",
    "distribution": "Inheems op natte heidevelden, venoevers en venen door Europa; in Nederland een kenmerkende soort.",
    "growth_habit": "Vaste siersgras van 60–120 cm; bloeit in juli–september.",
    "ecological_value": "Waardplant voor enkele vlindersoorten; zaad voedt vogels.",
    "fertilizer_needs": "Zure, voedselarme, natte grond; nooit kalken.",
    "maintenance_level": "laag",
    "family": "Poaceae", "family_common": "Grassenfamilie",
    "origin": "Europa",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Molinia_caerulea.jpeg", "Pijpenstrootje")],
},

}
