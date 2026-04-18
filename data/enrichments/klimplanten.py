"""
Plantenpedia — Verrijkingsdata: Klimplanten & Rozen

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

"Wisteria sinensis": {
    "description": "Blauwe regen is een van de meest spectaculaire klimplanten: in mei–juni hangen de lange, lila-blauwe bloemtrossen als sieraden aan de stengels en vullen de lucht met een betoverende geur. De plant kan tientallen jaren oud worden en enorm groot worden.",
    "distribution": "Inheems in China; in Nederland populair op pergola's, muren en pergola-constructies.",
    "growth_habit": "Krachtige klimplant van 10–30 m; bloeit in mei–juni.",
    "ecological_value": "De geurende bloemen trekken hommels en bijen; vlinders bezoeken de bloemen ook.",
    "toxic_info": "Zaden en peulen zijn giftig, met name voor kinderen.",
    "fertilizer_needs": "Weinig stikstof — teveel geeft blad ten koste van bloei; kaliumrijke meststof.",
    "pruning_info": "2× per jaar snoeien: in augustus de zomerscheuten tot 5 bladeren, in februari terug tot 2–3 knoppen.",
    "maintenance_level": "hoog",
    "family": "Fabaceae", "family_common": "Vlinderbloemenfamilie",
    "origin": "China",
    "hardiness": "winterhard", "evergreen": False,
    "photos": [wiki("Wisteria_sinensis_kz01.jpg", "Blauwe regen in bloei")],
},

"Lonicera periclymenum": {
    "description": "Wilde kamperfoelie is een inheemse klimmer met geurige, crème-gele bloemen die 's avonds het sterkst geuren om nachtvlinders aan te trekken. In de herfst rijpen rode bessen die door vogels worden gegeten. Een must voor de inheemse tuin.",
    "distribution": "Inheems in struwelen en bosranden door heel Europa; in Nederland langs heggen en in loofbossen.",
    "growth_habit": "Klimplant of ranker van 300–600 cm; bloeit in juni–september.",
    "ecological_value": "Nachtvlinders bezoeken de geurende bloemen; bessen voeden merels en vliegenvanger.",
    "insects_animals": [
        {"name": "Nachtpauwoog", "type": "vlinder", "desirable": True, "description": "Nachtvlinder die aangetrokken wordt door de avondgeur."},
    ],
    "toxic_info": "Bessen zijn giftig voor mensen; niet eten.",
    "maintenance_level": "laag",
    "family": "Caprifoliaceae", "family_common": "Kamperfoeliefamilie",
    "origin": "Europa",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Lonicera_periclymenum_kz02.jpg", "Wilde kamperfoelie")],
},

"Clematis jackmanii": {
    "description": "De grote clematis of bosdruif is de koningin van de klimplanten: van juni tot september bedekt de plant pergola's en muren met grote paarse, roze of witte bloemen. Er zijn honderden cultivars in alle kleuren en bloeiperiodes.",
    "distribution": "Tuinhybride van Aziatische en Europese soorten; in Nederland een van de populairste klimplanten.",
    "growth_habit": "Klimplant van 200–400 cm; bloeit van juni tot september.",
    "ecological_value": "Bijen en hommels bezoeken de bloemen; de pluimende vruchten zijn een winterdecor.",
    "toxic_info": "Alle plantendelen zijn licht giftig bij inname; huidcontact kan irritatie geven.",
    "pruning_info": "Groep 3 (laat bloeiend): in februari/maart terugknippen tot 30 cm. Groep 2: alleen dood hout verwijderen.",
    "maintenance_level": "laag",
    "family": "Ranunculaceae", "family_common": "Boterbloemfamilie",
    "origin": "Hybride (Aziatisch/Europees)",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Clematis_jackmanii_(1).jpg", "Clematis 'Jackmanii'")],
},

"Parthenocissus tricuspidata": {
    "description": "Oosterse wingerd is de klimplant die in de herfst huizen in een gloed van vuurrood zet: de drielobbige bladeren kleuren in oktober scharlaken, karmijn en oranje voordat ze vallen. De plant hecht zichzelf met kleine hechtkussens aan elke ondergrond.",
    "distribution": "Inheems in China, Korea en Japan; in Nederland de meest geziene klimplant op historische gebouwen.",
    "growth_habit": "Klimplant van 10–20 m; bloeit onopvallend in juni–juli, spectaculaire herfstkleur.",
    "ecological_value": "Bessen zijn voedsel voor spreeuwen en merels; de dichte structuur biedt nestgelegenheid.",
    "maintenance_level": "laag",
    "family": "Vitaceae", "family_common": "Wingerdsfamilie",
    "origin": "China, Korea en Japan",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Parthenocissus_tricuspidata's_fruits.JPG", "Wingerd in herfstkleur")],
},

"Rosa rugosa": {
    "description": "Rimpelroos is een robuuste, inheems-aandoende roos met enkelvoudige roze of witte bloemen van mei tot september en grote, vlezige rozenbottels in de herfst. De plant is droogtebestendig, zoutbestendig en bloeit onophoudelijk zonder bestrijding.",
    "distribution": "Inheems in Japan en Korea; in Nederland verwilderd in duinen en op droge, zandige standplaatsen.",
    "growth_habit": "Struik van 100–200 cm; bloeit van mei tot september.",
    "ecological_value": "Bijen bezoeken de open enkelvoudige bloemen voor stuifmeel; rozenbottels zijn voedsel voor merels en vliegenvanger.",
    "edible_parts": "Rozenblaadjes zijn eetbaar in thee; rozenbottels zijn rijk aan vitamine C voor jam en stroop.",
    "taste": "Bloemig, licht zoet (bloemblaadjes); zuur-fruitig (rozenbottels)",
    "recipes": "Rozenbottelthee (vitamine C); rozenbottelstroop; rooswater van bloemblaadjes.",
    "maintenance_level": "laag",
    "family": "Rosaceae", "family_common": "Rozenfamilie",
    "origin": "Japan en Korea",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Rosa_rugosa_kz02.jpg", "Rimpelroos")],
},

"Rosa glauca": {
    "description": "Bergroos is een sierlijke wilde roos met blauwgrijs blad, kleine enkelvoudige roze bloemen in juni en felrode rozenbottels in de herfst. Het is een van de weinige rozen met decoratief blad het hele seizoen — ook zonder bloemen al de moeite waard.",
    "distribution": "Inheems op berghellingen in Centraal- en Zuidoost-Europa; in Nederland populair als solitaire sierstruik.",
    "growth_habit": "Struik van 150–250 cm; bloeit in juni, bottels rijpen in september.",
    "ecological_value": "Bloemen voeden bijen; bottels zijn wintervoedsel voor vogels.",
    "edible_parts": "Rozenbottels zijn eetbaar voor jam, thee en stroop.",
    "pruning_info": "Weinig snoei; verwijder dood hout en dunne scheuten in het voorjaar.",
    "maintenance_level": "laag",
    "family": "Rosaceae", "family_common": "Rozenfamilie",
    "origin": "Centraal- en Zuidoost-Europa",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Rosa_glauca,_Claremore_-_geograph.org.uk_-_8075856.jpg", "Bergroos")],
},

"Clematis vitalba": {
    "description": "Bosrank is een krachtige inheemse wilde klimmer met kleine witte sterretjesbloemen van juli tot september die in de herfst pluimachtige vruchten vormen — de 'oudemansbaard'. De plant is licht giftig maar ecologisch waardevol als ruigtevormer.",
    "distribution": "Inheems in kalkrijke struwelen en bosranden door Europa; in Nederland op kalkrijke, warme plaatsen.",
    "growth_habit": "Klimplant van 5–30 m; bloeit in juli–september, pluimen sieren de winter.",
    "ecological_value": "Bloemen voeden bijen; de pluimvormige vruchten bieden nestmateriaal voor vogels.",
    "toxic_info": "Alle plantendelen zijn licht giftig bij inname; niet eten.",
    "maintenance_level": "laag",
    "family": "Ranunculaceae", "family_common": "Boterbloemfamilie",
    "origin": "Europa",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Clematis_vitalba_kz01.jpg", "Bosrank met pluimen")],
},

"Rosa arvensis": {
    "description": "Bosroos is een sierlijke inheemse wilde roos met kleine, witte enkelvoudige bloemen van juni tot juli en kleine, ronde rode rozenbottels in de herfst. Ze klimt langs heggen en door struwelen met behulp van haken.",
    "distribution": "Inheems in bosranden en struwelen van Europa; in Nederland op kalkrijke grond.",
    "growth_habit": "Klimroosje of struik van 100–200 cm; bloeit in juni–juli.",
    "ecological_value": "Bloemen voeden bijen; bottels zijn voedsel voor vogels.",
    "edible_parts": "Rozenbottels eetbaar voor thee en jam.",
    "maintenance_level": "laag",
    "family": "Rosaceae", "family_common": "Rozenfamilie",
    "origin": "Europa",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Rosa_arvensis_kz02.jpg", "Bosroos")],
},

"Clematis armandii": {
    "description": "Wintergroene clematis is de enige immergroene clematis die in Nederland kan overwinteren: de grote, glanzende bladeren zijn het hele jaar aanwezig en in maart–april verschijnen de grote, vanille-geurende witte bloemen vroeg in het seizoen.",
    "distribution": "Inheems in China; in Nederland populair op beschutte, warme, zonnige muren.",
    "growth_habit": "Wintergroene klimplant van 400–600 cm; bloeit vroeg in maart–mei.",
    "ecological_value": "De vroege geurende bloemen voeden vroege bijen en hommels.",
    "toxic_info": "Alle plantendelen zijn licht giftig bij inname.",
    "maintenance_level": "midden",
    "family": "Ranunculaceae", "family_common": "Boterbloemfamilie",
    "origin": "China",
    "hardiness": "matig_winterhard", "evergreen": True,
    "photos": [wiki("Clematis_armandii.jpg", "Wintergroene clematis")],
},

"Fallopia baldschuanica": {
    "description": "Bruidssluier is de snelst groeiende klimplant van Nederland: hij groeit tot 6 meter per jaar en bedekt in no-time schuren, heggen en pergola's. Van juli tot september staat de plant overdadig in bloei met kleine witte bloempjes.",
    "distribution": "Inheems in Centraal-Azië; in Nederland een populaire en snel-groeiende klimmer.",
    "growth_habit": "Klimplant van 10–15 m; bloeit van juli tot september.",
    "ecological_value": "Zweefvliegen en kleine bijen bezoeken de bloemwolken.",
    "weed_behavior": "Extreem woekerig; plant alleen waar je ruimte voor hebt en beheers jaarlijks.",
    "maintenance_level": "hoog",
    "family": "Polygonaceae", "family_common": "Duizendknoopfamilie",
    "origin": "Centraal-Azië",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Fallopia_baldschuanica1_ies.jpg", "Bruidssluier in bloei")],
},

"Hydrangea anomala petiolaris": {
    "description": "Klimhortensia is een langzaam groeiende maar eenmaal gevestigd indrukwekkende klimplant met vlakke witte bloemschermen van juni tot juli. De plant hecht zichzelf met luchtwortels aan muren en boomstammen zonder steun nodig te hebben.",
    "distribution": "Inheems in Japan en Korea; in Nederland populair op noordmuren en beschaduwde gevels.",
    "growth_habit": "Klimplant of bodembedekker van 200–1500 cm; bloeit in juni–juli.",
    "ecological_value": "Bijen en zweefvliegen bezoeken de witte bloemschermen.",
    "maintenance_level": "laag",
    "family": "Hydrangeaceae", "family_common": "Hortensiafamilie",
    "origin": "Japan en Korea",
    "hardiness": "winterhard", "evergreen": False,
    "photos": [wiki("Hydrangea_anomala,_May_2016.jpg", "Klimhortensia")],
},

"Rosa nitida": {
    "description": "Glansroos is een compacte, inheems-aandoende wilde roos met glanzend blad, kleine roze enkelvoudige bloemen in juni–juli en felrode rozenbottels. Het blad kleurt in het najaar prachtig rood-oranje. Ideaal voor kleinere tuinen.",
    "distribution": "Inheems in Noord-Amerika; in Nederland een compacte sierroosstruik.",
    "growth_habit": "Struik van 60–100 cm; bloeit in juni–juli.",
    "ecological_value": "Bloemen voor bijen; bottels voor vogels.",
    "edible_parts": "Rozenbottels voor thee en jam.",
    "maintenance_level": "laag",
    "family": "Rosaceae", "family_common": "Rozenfamilie",
    "origin": "Noord-Amerika",
    "hardiness": "volledig_winterhard", "evergreen": False,
    "photos": [wiki("Rosa_nitida.jpg", "Glansroos")],
},

}
