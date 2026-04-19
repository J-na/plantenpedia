"""
Plantenpedia — Verrijkingsdata: Kuipplanten

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

"Agapanthus hybriden": {
    "description": "De Afrikaanse lelie is een imposante kuipplant met bolronde bloemschermen vol stralend blauwe of witte bloemen op stevige stelen van 60–100 cm. Van juli tot september bloeit hij onvermoeibaar in potten op het terras.",
    "distribution": "Inheems in Zuid-Afrika; in Nederland alleen te houden als kuipplant die vorstvrij overwintert.",
    "growth_habit": "Vaste plant in een pot van 60–100 cm; bloeit in juli–september.",
    "ecological_value": "Hommels en bijen bezoeken de bloemen; interessant voor grote bestuivers.",
    "toxic_info": "Alle plantendelen zijn licht giftig; huidcontact met sap kan irritatie veroorzaken.",
    "fertilizer_needs": "Regelmatig met kaliumrijke meststof voeden tijdens de groei voor maximale bloei.",
    "pruning_info": "Na de bloei de stengels verwijderen; in oktober naar een vorstvrije ruimte brengen.",
    "maintenance_level": "midden",
    "native_nl": False, "drought_tolerant": True, "water_needs": "normaal",
    "family": "Amaryllidaceae", "family_common": "Amaryllifamilie",
    "origin": "Zuid-Afrika",
    "hardiness": "vorstgevoelig", "evergreen": True,
    "photos": [wiki("Agapanthus_praecox,_fruit_0052_02.jpg", "Afrikaanse lelie")],
},

"Laurus nobilis": {
    "description": "De laurier is een nobele immergroene kuipplant die al in de Oudheid symbool stond voor roem en overwinning — laurierkransen sierden de hoofden van Griekse helden en Olympische winnaars. In de keuken zijn de geurige blaadjes onmisbaar.",
    "distribution": "Inheems in het Mediterrane kustgebied; in Nederland als kuipplant die vorstvrij overwintert.",
    "growth_habit": "Wintergroene heester/kleine boom van 100–400 cm (in pot begrensd); langzaam groeiend.",
    "ecological_value": "De bloemetjes in april–mei zijn een vroege nectarbron voor bijen.",
    "edible_parts": "Blaadjes worden gebruikt als specerij in soepen, stoofgerechten en sauzen.",
    "taste": "Aromatisch, kruidig, licht bitter",
    "recipes": "Voeg een of twee blaadjes toe aan stoofgerechten, bouillons en marinades. Verwijder voor het serveren.",
    "medicinal_uses": "Laurierblaadjes hebben antiseptische eigenschappen; worden ook gebruikt in massageolie voor gewrichten.",
    "fertilizer_needs": "Jaarlijks in het voorjaar verpotten en bemesten; kalkrijke grond.",
    "pruning_info": "In het voorjaar naar wens in vorm knippen; verdraagt forse snoei goed.",
    "maintenance_level": "midden",
    "native_nl": False, "drought_tolerant": True, "water_needs": "normaal",
    "family": "Lauraceae", "family_common": "Laurierfamilie",
    "origin": "Mediterraan kustgebied",
    "hardiness": "matig_winterhard", "evergreen": True,
    "photos": [wiki("Laurus-nobilis-Sitia-Crete-Greece.jpg", "Laurierbladeren")],
},

"Olea europaea": {
    "description": "De olijf is een tijdloze Mediterrane kuipplant met zilvergrijze, lancetvormige blaadjes die het hele jaar aanwezig zijn. In de zomer verschijnen kleine witte bloemetjes die bij gunstig weer olijven vormen — een uniek stukje Mediterraan leven op je terras.",
    "distribution": "Inheems in het Mediterrane bekken; in Nederland als kuipplant die koud maar vorstvrij overwintert.",
    "growth_habit": "Wintergroene boom/heester van 100–300 cm (in pot begrensd); traag groeiend, wordt oud.",
    "ecological_value": "Bloemen voeden bijen; de vruchten worden gegeten door merels als ze rijpen.",
    "edible_parts": "Olijven zijn eetbaar na fermentatie (rauwe zijn bittere oneetbare); de olie is veelzijdig in de keuken.",
    "taste": "Bitter (rauw), fruitig-nootachtig (ingelegd of als olie)",
    "fertilizer_needs": "Weinig voeding in de zomer; potgrond met perliet voor droge omstandigheden.",
    "pruning_info": "In het voorjaar licht snoeien voor een mooie kroon; verdraagt forse snoei.",
    "maintenance_level": "midden",
    "native_nl": False, "drought_tolerant": True, "water_needs": "droog",
    "family": "Oleaceae", "family_common": "Olijffamilie",
    "origin": "Mediterraan bekken",
    "hardiness": "matig_winterhard", "evergreen": True,
    "photos": [wiki("Olea_europaea,Velilla_de_San_Antonio.jpg", "Olijfboom")],
},

"Fuchsia hybriden": {
    "description": "Fuchsia is de flamboyante kuipplant bij uitstek: van juli tot oktober hangen de zweefbloeiers als kleine lampenoortjes aan de takken in rood, roze, paars of wit. In beschutte gebieden kan fuchsia overwinteren in de tuin.",
    "distribution": "Tuinhybride van Zuid-Amerikaanse soorten; in Nederland populair als pot- en hangplant.",
    "growth_habit": "Heester van 30–150 cm; bloeit onvermoeibaar van juli tot de eerste nachtvorst.",
    "ecological_value": "Hommels met lange tong bereiken de nectar in de diep hangende bloemen.",
    "edible_parts": "Bessen en bloemen zijn eetbaar en hebben een mild zoet-zure smaak.",
    "fertilizer_needs": "Regelmatig vloeibare meststof in de zomer voor een rijke bloei.",
    "maintenance_level": "midden",
    "native_nl": False, "drought_tolerant": False, "water_needs": "normaal",
    "family": "Onagraceae", "family_common": "Teunisbloemfamilie",
    "origin": "Zuid-Amerika (hybride)",
    "hardiness": "vorstgevoelig", "evergreen": False,
    "photos": [wiki("Fuchsia's,_RP-T-1969-555.jpg", "Fuchsia in bloei")],
},

"Mandevilla": {
    "description": "Braziliaanse jasmijn is een tropische klimmer met grote, trompetvormige bloemen in roze, rood of wit die van juni tot september bloeien. De glanzende, donkergroene bladeren zijn het hele zomer decoratief op het terras.",
    "distribution": "Inheems in Brazilië en andere tropische landen; in Nederland als terras-klimplant.",
    "growth_habit": "Klimmer van 100–300 cm (in pot); bloeit van juni tot oktober.",
    "toxic_info": "Alle plantendelen zijn giftig; niet eten.",
    "fertilizer_needs": "Wekelijks vloeibare meststof in de groeiperiode voor maximale bloei.",
    "maintenance_level": "midden",
    "native_nl": False, "drought_tolerant": False, "water_needs": "normaal",
    "family": "Apocynaceae", "family_common": "Maagdenpalfamilie",
    "origin": "Brazilië",
    "hardiness": "niet_winterhard", "evergreen": True,
    "photos": [wiki("Mandevilla_splendens.jpg", "Braziliaanse jasmijn")],
},

"Pelargonium zonale": {
    "description": "Geranium (eigenlijk pelargonium) is de volkse balkon- en terrasplant bij uitstek: van mei tot oktober bloeien de dichte trossen in rood, roze, wit of zalm onophoudelijk in bakken, potten en vensterbanken. Eenvoudig te stekken voor hergebruik.",
    "distribution": "Inheems in Zuid-Afrika; in Nederland een klassieke balkon- en kuipplant.",
    "growth_habit": "Heesterachtig van 20–50 cm; bloeit van mei tot de eerste vorst.",
    "ecological_value": "Zweefvliegen bezoeken de bloemen voor nectar.",
    "fertilizer_needs": "Wekelijks vloeibare meststof in de bloeiperiode voor continue bloei.",
    "maintenance_level": "midden",
    "native_nl": False, "drought_tolerant": True, "water_needs": "normaal",
    "family": "Geraniaceae", "family_common": "Ooievaarsbekfamilie",
    "origin": "Zuid-Afrika",
    "hardiness": "niet_winterhard", "evergreen": True,
    "photos": [wiki("Pelargonium_zonale.jpg", "Geranium/Pelargonium")],
},

"Cordyline australis": {
    "description": "Koolpalm is een indrukwekkende kuipplant met lange, lancetvormige bladeren in een rozet die een tropisch gevoel geeft op het terras. In warme zomers verschijnen witte pluimachtige bloemtrossen met een heerlijke geur.",
    "distribution": "Inheems in Nieuw-Zeeland; in Nederland populair als terras-kuipplant.",
    "growth_habit": "Heesterachtig van 100–200 cm (in pot); langzaam groeiend.",
    "fertilizer_needs": "Matige bemesting; vochtige maar goed doorlatende grond.",
    "maintenance_level": "laag",
    "native_nl": False, "drought_tolerant": False, "water_needs": "normaal",
    "family": "Asparagaceae", "family_common": "Aspergefamilie",
    "origin": "Nieuw-Zeeland",
    "hardiness": "matig_winterhard", "evergreen": True,
    "photos": [wiki("Cordyline_australis,_Anderson_Shelter_and_Copse_-_geograph.org.uk_-_126026.jpg", "Koolpalm")],
},

"Petunia surfinia cultivars": {
    "description": "Hangpetunia is de koningin van het zomerterras: van mei tot oktober stromen de grote, rijkbloeiende hangertjes over potrandjes in roze, paars, wit of rood. De Surfinia-soorten zijn bijzonder rijk vertakt en langbloeiers.",
    "distribution": "Tuinhybriden van Zuid-Amerikaanse soorten; in Nederland een van de meest verkochte terrasplanten.",
    "growth_habit": "Hangend van 40–80 cm; bloeit van mei tot de eerste vorst.",
    "fertilizer_needs": "Wekelijks vloeibare meststof; regelmatig water geven.",
    "maintenance_level": "midden",
    "native_nl": False, "drought_tolerant": False, "water_needs": "normaal",
    "family": "Solanaceae", "family_common": "Nachtschadefamilie",
    "origin": "Zuid-Amerika (hybride)",
    "hardiness": "niet_winterhard", "evergreen": False,
    "photos": [wiki("Petunia_Surfinia_Hot_Pink_Flower.jpg", "Hangpetunia")],
},

}
