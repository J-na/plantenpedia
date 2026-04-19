"""
Plantenpedia — Verrijkingsdata: Keukenkruiden

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

"Allium schoenoprasum": {
    "description": "Bieslook is het meest praktische keukenkruid van de tuin: de dunne, holle stengels smaken naar ui en zijn het hele groeiseizoen beschikbaar. In mei–juli verschijnen bovendien mooie, paarse bolbloemen die ook insecten aantrekken en eetbaar zijn.",
    "distribution": "Inheems in bergweiden door Europa en Azië; in Nederland in elke moestuin als keukenkruid.",
    "growth_habit": "Vaste plant van 20–30 cm; groeit in compacte polletjes en bloeit in mei–juli.",
    "ecological_value": "Bijen en hommels bezoeken de paarse bloemen; de bladeren zijn het hele seizoen te oogsten.",
    "edible_parts": "Holle stengels (blad), bloemen en zaad zijn allen eetbaar.",
    "taste": "Mild uienachtig, fris",
    "recipes": "Fijngesneden over aardappels, ei, sauzen en soepen. Bloemen als salade-garnering.",
    "fertilizer_needs": "Lichte bemesting; humusrijke, goed doorlatende grond is ideaal.",
    "pruning_info": "Regelmatig knippen voor vers blad; na de bloei terugknippen voor nieuwe groei.",
    "maintenance_level": "laag",
    "native_nl": True, "drought_tolerant": False, "water_needs": "normaal",
    "family": "Amaryllidaceae", "family_common": "Amaryllifamilie",
    "origin": "Europa en Azië",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Allium_schoenoprasum(01).jpg", "Bieslook in bloei")],
},

"Mentha x piperita": {
    "description": "Pepermunt is het frisse, verkoelende kruid bij uitstek: de doordringende mentholgeur van de bladeren is onmiskenbaar en in thee, cocktails en desserts onvervangbaar. De plant woekert via ondergrondse uitlopers — teelt het bij voorkeur in een pot.",
    "distribution": "Hybride (M. aquatica × M. spicata); in Nederland wijd verspreid in kruidentuinen en verwilderd langs sloten.",
    "growth_habit": "Vaste plant van 30–60 cm; spreidt snel via worteluitlopers.",
    "ecological_value": "Bijen en zweefvliegen bezoeken de paarse bloempieken in de zomer.",
    "edible_parts": "Blaadjes worden gebruikt in thee, cocktails, desserts en salades.",
    "taste": "Fris, koel, menthol-achtig",
    "recipes": "Pepermuntthee: 3–5 blaadjes 5 minuten in heet water. Mojito: munt, rum, limoensap, suiker en bruiswater.",
    "medicinal_uses": "Pepermunt werkt krampstillend op de darmen; thee helpt bij buikpijn en indigestie.",
    "weed_behavior": "Woekert via ondergrondse uitlopers; plant in een pot of begrensde ruimte.",
    "fertilizer_needs": "Lichte bemesting; vochtige grond is essentieel.",
    "pruning_info": "Regelmatig knippen voor verse groei; na de bloei terugknippen.",
    "maintenance_level": "laag",
    "native_nl": False, "drought_tolerant": False, "water_needs": "vochtig",
    "family": "Lamiaceae", "family_common": "Lipbloemenfamilie",
    "origin": "Hybride (Europa)",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Peppermint_Mentha_×_piperita_IMG_7237.jpg", "Pepermunt")],
},

"Petroselinum crispum": {
    "description": "Peterselie is het meest gebruikte kruid in de Nederlandse keuken: de frisgroene, aromatische blaadjes zijn het hele groeiseizoen te oogsten en passen bij vrijwel elk gerecht. Er zijn krulle en platte variëteiten — de platte smaakt sterker.",
    "distribution": "Inheems in het Mediterraan gebied; wereldwijd een van de meest geteelde keukenkruiden.",
    "growth_habit": "Tweejarige plant van 20–40 cm; in het eerste jaar bladoogst, het tweede jaar bloei en zaad.",
    "ecological_value": "In het tweede jaar trekken de bloemschermen zweefvliegen, sluipwespen en kleine bijen aan.",
    "edible_parts": "Blaadjes (vers en gedroogd), stelen en wortels zijn eetbaar.",
    "taste": "Fris, kruidig, licht bitter",
    "recipes": "Als garnering, in sauzen, soepen, tabbouleh en pesto van peterselie.",
    "nutritional_value": "Peterselie is rijk aan vitamine C, K en ijzer — een van de meest voedzame keukenkruiden.",
    "fertilizer_needs": "Matig rijke, vochtige grond; regelmatig water geven in droge perioden.",
    "pruning_info": "Regelmatig blaadjes oogsten; altijd van buiten naar binnen oogsten.",
    "maintenance_level": "laag",
    "native_nl": False, "drought_tolerant": False, "water_needs": "normaal",
    "family": "Apiaceae", "family_common": "Schermbloemenfamilie",
    "origin": "Mediterraan gebied",
    "hardiness": "winterhard", "evergreen": False,
    "photos": [wiki("Petroselinum_crispum.JPG", "Peterselie")],
},

}
