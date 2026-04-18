"""
Plantenpedia — Verrijkingsdata: Bollen & Knollen

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

"Allium aflatunense": {
    "description": "Sierui is een architectonische bollenplant met perfecte, paarse kogelbloemen op rechte stelen van 60–90 cm die in mei–juni bloeien. De grote bollen van 10–15 cm doorsnede zijn een eye-catcher in de border en ook als gedroogde bloem te gebruiken.",
    "distribution": "Inheems in Centraal-Azië; in Nederland populair als decoratieve bollenplant in borders.",
    "growth_habit": "Bolgewas van 60–90 cm; bloeit in mei–juni.",
    "ecological_value": "Bijen en hommels bezoeken de kleine bloempjes in de bol; de gedroogde bollen voeden sijsjes.",
    "edible_parts": "Alle delen zijn eetbaar (verwant aan ui en knoflook): blad, bloemen en knol.",
    "fertilizer_needs": "Goed doorlatende grond; bollen rotten bij natte, zware grond.",
    "pruning_info": "Blad laten afsterven; de bollen kunnen in de grond blijven of worden opgegraven.",
    "maintenance_level": "laag",
    "family": "Amaryllidaceae", "family_common": "Amaryllifamilie",
    "origin": "Centraal-Azië",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Allium_aflatunense.jpg", "Sierui in bloei")],
},

"Galanthus nivalis": {
    "description": "Sneeuwklokje is het eerste teken van de lente: de witte druppeltjes met een groene vlek verschijnen al in januari–maart soms door de sneeuw heen. De plant is giftig maar symbolisch van groot belang als vroege bestuiverbron.",
    "distribution": "Inheems in bergweiden en loofbossen van Europa; in Nederland verwilderd in parken en bossen.",
    "growth_habit": "Bolgewas van 10–15 cm; bloeit in januari–maart en verdwijnt dan volledig.",
    "ecological_value": "Één van de weinige winterbloeiers: koninginnehommels en vroege honingbijen zijn dol op de nectar.",
    "toxic_info": "Alle plantendelen zijn giftig (galanthamine en gerelateerde alkaloïden); niet eten.",
    "fertilizer_needs": "Geen speciale voeding; vochtige, humusrijke grond onder bomen is ideaal.",
    "pruning_info": "Nooit het groen verwijderen voordat het volledig geel is; de bol heeft het blad nodig voor het volgende jaar.",
    "maintenance_level": "laag",
    "family": "Amaryllidaceae", "family_common": "Amaryllifamilie",
    "origin": "Europa",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Galanthus_nivalis-IMG_2963.jpg", "Sneeuwklokjes")],
},

"Narcissus": {
    "description": "Narcissen zijn de herauten van de lente: van februari tot mei verschijnen de bekende gele, witte of tweekleurige bloemen met hun typische trompet. Er zijn honderden cultivars, van kleine miniatuursoorten tot grote dubbele bloemen, allemaal giftig maar prachtig.",
    "distribution": "Inheems in Mediterraan gebied en West-Europa; in Nederland wijd verwilderd in parken en op landgoederen.",
    "growth_habit": "Bolgewas van 15–60 cm; bloeit in februari–april, trekt daarna terug.",
    "ecological_value": "Vroege nectarplant voor koninginnehommels en vroege vlinders.",
    "toxic_info": "Alle plantendelen zijn giftig — ook de bollen. Narcissensap kan huidirritatie veroorzaken.",
    "fertilizer_needs": "Bolvoeding na de bloei of compost in het najaar voor krachtige bol-aanmaak.",
    "pruning_info": "Blad pas verwijderen als het volledig vergeeld is; dit is essentieel voor een goede bol.",
    "maintenance_level": "laag",
    "family": "Amaryllidaceae", "family_common": "Amaryllifamilie",
    "origin": "Mediterraan gebied",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Narcissus_February_Gold.jpg", "Narcis")],
},

"Tulipa hybriden": {
    "description": "Tulpen zijn het icoon van de Nederlandse tuincultuur: in april–mei bloeien de sierlijke kelken in vrijwel elke denkbare kleur en vorm, van enkelvoudig tot gevuld, van pioenachtig tot papegaaienachtig. Ze zijn onmisbaar in de lentetuin.",
    "distribution": "Tuinhybriden van soorten uit Centraal-Azië; in Nederland de beroemdste bollenplant ter wereld.",
    "growth_habit": "Bolgewas van 20–70 cm; bloeit in april–mei, bol raakt uitgeput na 1–3 jaar.",
    "ecological_value": "Hommels en bijen bezoeken de vroege bloemen; de open kelk is toegankelijk voor veel soorten.",
    "fertilizer_needs": "Bolvoeding in het najaar of compost; goed doorlatende grond is essentieel.",
    "pruning_info": "Blad pas verwijderen na vergeling. Bollen jaarlijks opgegraven voor beste resultaten.",
    "maintenance_level": "midden",
    "family": "Liliaceae", "family_common": "Leliesfamilie",
    "origin": "Centraal-Azië",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Tulipa_suaveolens._Reader.jpg", "Tulpen in bloei")],
},

"Dahlia hybriden": {
    "description": "Dahlia's zijn de grote showplanten van de herfst: van juli tot de eerste vorst bloeien de indrukwekkende bloemen in alle denkbare kleuren, maten en vormen — van kleine pompon-dahlia's tot reusachtige kaktus- en dekoratifdahlia's. De knol overwintert binnen.",
    "distribution": "Inheems in de berggebieden van Mexico; in Nederland een geliefde knollenplant voor borders en potten.",
    "growth_habit": "Knolgewas van 30–150 cm; bloeit van juli tot de eerste nachtvorst.",
    "ecological_value": "Enkelvoudige dahlia's zijn uitstekend voor bijen en hommels; gevulde vormen minder toegankelijk.",
    "fertilizer_needs": "Regelmatig voeden met kaliumrijke meststof voor rijke bloei; humusrijke grond.",
    "pruning_info": "Na de eerste vorst de knollen opgraven en vorstvrij bewaren; in mei opnieuw planten.",
    "maintenance_level": "hoog",
    "family": "Asteraceae", "family_common": "Composietenfamilie",
    "origin": "Mexico",
    "hardiness": "vorstgevoelig", "evergreen": False,
    "photos": [wiki("Dahlia's,_RP-T-1916-42.jpg", "Dahlia in bloei")],
},

"Crocus chrysanthus": {
    "description": "De goudkrokus is een van de eerste lentebolletjes: al in februari–maart verschijnen de kleine geel-oranje, witte of paarse kelkjes uit de koude grond — een optimistisch teken dat de winter voorbij is. Ze naturaliseren prachtig in gras.",
    "distribution": "Inheems op kalkhellingen van de Balkan; in Nederland wijd verspreid als naturaliseerder in gazons en parken.",
    "growth_habit": "Bolgewas van 5–10 cm; bloeit in februari–maart, verdwijnt dan volledig.",
    "ecological_value": "Koninginnehommels en vroege bijen zijn dankbaar voor deze vroege nectarbron na de winter.",
    "fertilizer_needs": "Geen bemesting nodig; goed doorlatende, matig voedselarme grond.",
    "pruning_info": "Nooit het blad verwijderen voor vergeling; laat de bol rusten.",
    "maintenance_level": "laag",
    "family": "Iridaceae", "family_common": "Irissensfamilie",
    "origin": "Balkan",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Crocus_chrysanthus,_Berlin-Charlottenburg,_160319,_ako.jpg", "Goudkrokus")],
},

"Muscari armeniacum": {
    "description": "Blauwdruifjes zijn kleine bollenplantjes met compacte, kobaltblauwe druifvormige bloemen op stelen van 10–20 cm die in maart–mei bloeien. Ze naturaliseren moeiteloos en vormen na verloop van jaren een paars-blauwe bloeiende tapijt.",
    "distribution": "Inheems in de Kaukasus en Zuidoost-Europa; in Nederland wijd verwilderd in tuinen en parkgebieden.",
    "growth_habit": "Bolgewas van 10–20 cm; bloeit in maart–mei.",
    "ecological_value": "Vroege nectarplant voor bijen en hommels direct na de winter.",
    "fertilizer_needs": "Geen speciale voeding; verdraagt vrijwel alle grondsoorten.",
    "pruning_info": "Blad laten afsterven; bollen hoeven niet te worden opgegraven.",
    "maintenance_level": "laag",
    "family": "Asparagaceae", "family_common": "Aspergefamilie",
    "origin": "Kaukasus en Zuidoost-Europa",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Muscari_armeniacum_kz01.jpg", "Blauwdruifjes")],
},

"Allium giganteum": {
    "description": "Reuzenui is de grote broer van sierui: op stelen van 100–130 cm dragen de paarse kogelbollen van 10–15 cm doorsnede in juni–juli een architectonische pracht. De gedroogde bollen zijn ook sierlijk en voeden sijsjes.",
    "distribution": "Inheems in Centraal-Azië; in Nederland een spectaculaire bolginsectenbloem.",
    "growth_habit": "Bolgewas van 100–130 cm; bloeit in juni–juli.",
    "ecological_value": "Bijen, hommels en vlinders bezoeken de kleine bloempjes in de bol.",
    "edible_parts": "Eetbaar zoals andere Allium-soorten.",
    "maintenance_level": "laag",
    "family": "Amaryllidaceae", "family_common": "Amaryllifamilie",
    "origin": "Centraal-Azië",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Allium_giganteum,_Giant_Onion._Chapeltoun,_North_Ayrshire.jpg", "Reuzenui")],
},

"Hyacinthus orientalis": {
    "description": "Hyacint is het meest geurende bolgewas van de lente: de compacte, dichte bloempieken in blauw, roze, wit, geel of rood bloeien in april en verspreiden een ongelooflijk intense, zoete geur die de tuin en het huis vult.",
    "distribution": "Inheems in het Oosten Mediterrane gebied; in Nederland een klassieke lentebol.",
    "growth_habit": "Bolgewas van 20–30 cm; bloeit in april.",
    "ecological_value": "Vroege nectarplant voor hommels en bijen.",
    "toxic_info": "De bol bevat calcium-oxalaatkristallen die huidirritatie veroorzaken; altijd handschoenen bij planten.",
    "maintenance_level": "laag",
    "family": "Asparagaceae", "family_common": "Aspergefamilie",
    "origin": "Oost-Mediterraan gebied",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Hyacinthus_orientalis,_1_-_geograph.org.uk_-_6088043.jpg", "Hyacint")],
},

"Fritillaria meleagris": {
    "description": "Kievitsbloem is een delicate, inheemse bol met paarsbruine, schaakbord-gemusterde hangende bloemen in april–mei. Het is een karakteristieke plant van vochtige Nederlandse uiterwaarden en rijkelijk beschermd in het wild.",
    "distribution": "Inheems in vochtige graslanden en uiterwaarden van Europa; in Nederland zeldzaam in het wild, populair als tuinbol.",
    "growth_habit": "Bolgewas van 25–40 cm; bloeit in april–mei.",
    "ecological_value": "Vroege nectarplant voor hommels en honingbijen.",
    "toxic_info": "Alle plantendelen zijn giftig; niet eten.",
    "maintenance_level": "laag",
    "family": "Liliaceae", "family_common": "Leliesfamilie",
    "origin": "Europa",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Fritillaria_meleagris_kz01.jpg", "Kievitsbloem")],
},

"Anemone blanda": {
    "description": "Blauwe anemoon is een charmant vroeglentebolletje: de stralend blauwe, roze of witte sterretjesbloemen bloeien in maart–april op een tapijt van fijngesneden blad. Ze naturaliseren prachtig onder bomen en struiken.",
    "distribution": "Inheems in kalkachtige bergbossen van Zuidoost-Europa en Turkije; in Nederland populair als vroeglentebolletje.",
    "growth_habit": "Bolgewas van 10–15 cm; bloeit in maart–april, verdwijnt dan volledig.",
    "ecological_value": "Vroege nectarplant voor koninginnehommels en bijen.",
    "toxic_info": "Alle plantendelen zijn licht giftig (protoanemonine).",
    "maintenance_level": "laag",
    "family": "Ranunculaceae", "family_common": "Boterbloemfamilie",
    "origin": "Zuidoost-Europa en Turkije",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Anemone_blanda,_Jardín_Botánico_de_Múnich,_Alemania,_2013-05-04,_DD_01.jpg", "Blauwe anemoon")],
},

"Scilla siberica": {
    "description": "Sterhyacint is een van de vroegste bollenplantjes: de intensief blauwe sterretjesbloemen steken al in maart boven de grond en zijn een dankbaar signaal na de donkere wintermaanden. Ze naturaliseren gemakkelijk in gras.",
    "distribution": "Inheems in bergbossen van Kaukasus en Turkije; in Nederland wijd verwilderd in parken.",
    "growth_habit": "Bolgewas van 10–15 cm; bloeit vroeg in maart–april.",
    "ecological_value": "Vroege nectarplant voor bijen en hommels.",
    "toxic_info": "Alle plantendelen zijn giftig; niet eten.",
    "maintenance_level": "laag",
    "family": "Asparagaceae", "family_common": "Aspergefamilie",
    "origin": "Kaukasus en Turkije",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Scilla_siberica,_Siberian_squill.jpg", "Sterhyacint")],
},

"Fritillaria imperialis": {
    "description": "Keizerskroon is een imposant bolgewas met een kroontje van glanzend groen blad bovenop een krans van oranje, rode of gele hangende klokbloemen op stelen van 60–90 cm in april–mei. De plant ruikt naar vos — en dat houdt muizen weg.",
    "distribution": "Inheems in berggebieden van Turkije en Iran; in Nederland een klassieke, uitbundige lentebol.",
    "growth_habit": "Bolgewas van 60–90 cm; bloeit in april–mei.",
    "ecological_value": "Hommels bezoeken de hangende klokken voor nectar.",
    "toxic_info": "Alle plantendelen zijn giftig; de geur en giftigheid weren muizen en mollen.",
    "maintenance_level": "laag",
    "family": "Liliaceae", "family_common": "Leliesfamilie",
    "origin": "Turkije en Iran",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Fritillaria_imperialis,.jpg", "Keizerskroon")],
},

"Anemone coronaria": {
    "description": "Anemoon (Kroonanemoon) is een prachtige mediterrane bol met grote, felgekleurde bloemen in rood, blauw, paars of wit met een zwart hart — een echte eyecatcher in de lentetuin van maart tot mei.",
    "distribution": "Inheems in het Mediterraan gebied; in Nederland als lentebol in borders en snijbloemen.",
    "growth_habit": "Bolgewas van 20–40 cm; bloeit in maart–mei.",
    "ecological_value": "Bijen en hommels bezoeken de heldere bloemen.",
    "toxic_info": "Alle plantendelen zijn licht giftig; niet eten.",
    "maintenance_level": "laag",
    "family": "Ranunculaceae", "family_common": "Boterbloemfamilie",
    "origin": "Mediterraan gebied",
    "hardiness": "matig_winterhard", "evergreen": False,
    "photos": [wiki("Anemone_coronaria,_Chouf,_Lebanon_(52260833549).jpg", "Kroonanemoon")],
},

}
