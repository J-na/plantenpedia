"""
Plantenpedia — Combinatieplanten (companion planting)
Samenvoegen via __init__.py: COMPANIONS wordt gemerged in ENRICHMENTS.

Upload: python data/upload.py --fields companion_plants
Schema: ALTER TABLE plants ADD COLUMN IF NOT EXISTS companion_plants JSONB DEFAULT '[]';
"""

# Formaat per item: {"scientific_name": "...", "dutch_name": "...", "reason": "..."}

COMPANIONS: dict = {

    # ── Vaste planten ────────────────────────────────────────────────────────

    "Achillea millefolium": {"companion_plants": [
        {"scientific_name": "Salvia nemorosa", "dutch_name": "Salie",
         "reason": "Complementaire bloeitijden en dezelfde bestuivers; samen een kleurrijke prairie-combinatie."},
        {"scientific_name": "Echinacea purpurea", "dutch_name": "Rode zonnehoed",
         "reason": "Klassieke prairie-duo dat zowel bijen als vlinders trekt van juni tot september."},
        {"scientific_name": "Knautia arvensis", "dutch_name": "Beemdknoopkruid",
         "reason": "Bloeien samen in zomer-weides en trekken overlappers als zweefvliegen en hommels."},
        {"scientific_name": "Rosa rugosa", "dutch_name": "Rimpelroos",
         "reason": "Duizendblad trekt sluipwespen aan die bladluizen op naburige rozen bestrijden."},
    ]},

    "Echinacea purpurea": {"companion_plants": [
        {"scientific_name": "Solidago", "dutch_name": "Guldenroede",
         "reason": "Naadloos aansluitende laat-zomerbloei; samen de perfecte nectar-brug voor bijen richting de herfst."},
        {"scientific_name": "Achillea millefolium", "dutch_name": "Duizendblad",
         "reason": "Complementaire textuur (breed vs. pluimig) met vergelijkbaar ecologisch profiel."},
        {"scientific_name": "Nepeta faassenii", "dutch_name": "Kattenkruid",
         "reason": "Langer bloeiseizoen door twee bloeipieken van kattenkruid rond de echinacea-bloei."},
    ]},

    "Solidago": {"companion_plants": [
        {"scientific_name": "Echinacea purpurea", "dutch_name": "Rode zonnehoed",
         "reason": "Guldenroede neemt de staak over als de zonnehoed uitbloeit — samen een ononderbroken nectarbron."},
        {"scientific_name": "Aster frikartii", "dutch_name": "Aster",
         "reason": "Beide herfstbloeiers vormen een blauw-geel contrast en trekken laat-vliegende hommels."},
        {"scientific_name": "Sanguisorba officinalis", "dutch_name": "Grote pimpernel",
         "reason": "Sierlijke herfst-combinatie met complementaire silhouetten; beide geliefde waardplanten."},
    ]},

    "Salvia nemorosa": {"companion_plants": [
        {"scientific_name": "Nepeta faassenii", "dutch_name": "Kattenkruid",
         "reason": "Beide laagblijvend en paars-blauw; samen een hummende voorrij voor bijentuinen."},
        {"scientific_name": "Achillea millefolium", "dutch_name": "Duizendblad",
         "reason": "Hoogteverschil en textuurcontrast; duizendblad vult de ruimte tussen de saliepluimen."},
        {"scientific_name": "Lavandula angustifolia", "dutch_name": "Lavendel",
         "reason": "Vergelijkbare bodem- en lichtbehoefte; beide trekt hommels en vlinders aan."},
    ]},

    "Nepeta faassenii": {"companion_plants": [
        {"scientific_name": "Lavandula angustifolia", "dutch_name": "Lavendel",
         "reason": "Beide houden van droge, zonnige plekken; samen een zilvergrijze, geurige rand."},
        {"scientific_name": "Rosa rugosa", "dutch_name": "Rimpelroos",
         "reason": "Kattenkruid maskeert de voet van rozen en houdt bladluizen op afstand via de geur."},
        {"scientific_name": "Salvia nemorosa", "dutch_name": "Salie",
         "reason": "Klassieke combinatie voor droge borders; twee bloeipieken door terugsnoeien na eerste bloei."},
    ]},

    "Lupinus hybriden": {"companion_plants": [
        {"scientific_name": "Achillea millefolium", "dutch_name": "Duizendblad",
         "reason": "Lupine fixeert stikstof; duizendblad profiteert van de verbeterde bodem."},
        {"scientific_name": "Fragaria vesca", "dutch_name": "Bosaardbei",
         "reason": "Lupine beschut de aardbeiplanten in het begin van het seizoen."},
    ]},

    "Filipendula ulmaria": {"companion_plants": [
        {"scientific_name": "Iris pseudacorus", "dutch_name": "Gele lis",
         "reason": "Beide houden van natte grond; samen een klassieke oeverbeplanting met lang bloeiseizoen."},
        {"scientific_name": "Lythrum salicaria", "dutch_name": "Kattenstaart",
         "reason": "Geel en paars naast elkaar langs de waterkant; beide magneten voor libellen en vlinders."},
        {"scientific_name": "Caltha palustris", "dutch_name": "Dotterbloem",
         "reason": "Dotterbloem bloeit vroeg; moerasspirea neemt de fakkel over in de zomer."},
    ]},

    "Foeniculum vulgare": {"companion_plants": [
        {"scientific_name": "Achillea millefolium", "dutch_name": "Duizendblad",
         "reason": "Beide trekken zweefvliegen en sluipwespen; venkel hoort apart (remt andere schermbloemigen)."},
        {"scientific_name": "Calendula officinalis", "dutch_name": "Goudsbloem",
         "reason": "Goudsbloem trekt gunstige insecten aan; venkel geeft hoogte in de border."},
    ]},

    "Galium odoratum": {"companion_plants": [
        {"scientific_name": "Hosta tardiana", "dutch_name": "Hosta",
         "reason": "Beide houden van schaduw; lief-der-bedstro vormt een elegant wit tapijt onder de hostas."},
        {"scientific_name": "Vinca minor", "dutch_name": "Kleine maagdenpalm",
         "reason": "Twee bodembedekkers voor schaduw; lieve-bedstro bloeit wit in het voorjaar, vinca blauw."},
        {"scientific_name": "Pulmonaria officinalis", "dutch_name": "Longkruid",
         "reason": "Vroege bloeiers in de schaduw; longkruid geeft kleur voor het lieve-bedstro uitloopt."},
    ]},

    "Pulmonaria officinalis": {"companion_plants": [
        {"scientific_name": "Helleborus niger", "dutch_name": "Kerstroosje",
         "reason": "Helleborus bloeit eerder; longkruid neemt het bloeistokje over; samen maanden kleur in de schaduw."},
        {"scientific_name": "Galium odoratum", "dutch_name": "Lieve-bedstro",
         "reason": "Longkruid als vroeg accent, lieve-bedstro als zomergrond — perfecte schaduw-laagbeplanting."},
    ]},

    "Sanguisorba officinalis": {"companion_plants": [
        {"scientific_name": "Solidago", "dutch_name": "Guldenroede",
         "reason": "Sierlijke herfst-combinatie; de donkere knopjes van pimpernel tussen het gele schuim van guldenroede."},
        {"scientific_name": "Achillea millefolium", "dutch_name": "Duizendblad",
         "reason": "Complementaire structuur in een weide-stijl border; beide houden van normale tot droge grond."},
    ]},

    # ── Wilde planten ────────────────────────────────────────────────────────

    "Trifolium repens": {"companion_plants": [
        {"scientific_name": "Achillea millefolium", "dutch_name": "Duizendblad",
         "reason": "Witte klaver fixeert stikstof in de bodem ten voordele van naburige planten."},
        {"scientific_name": "Prunella vulgaris", "dutch_name": "Gewone brunel",
         "reason": "Beide laagblijvende weide-planten die bijen trekken; ideaal in een bloemenmengsel."},
    ]},

    "Symphytum officinale": {"companion_plants": [
        {"scientific_name": "Alnus glutinosa", "dutch_name": "Zwarte els",
         "reason": "Smeerwortel als dynamische accumulator — zijn bladen als mulch verrijken de bodem rond bomen."},
        {"scientific_name": "Sorbus aucuparia", "dutch_name": "Lijsterbes",
         "reason": "Smeerwortel als bodembedekker en gratis stikstofbron onder vruchtdragende bomen en struiken."},
    ]},

    "Tanacetum vulgare": {"companion_plants": [
        {"scientific_name": "Rosa rugosa", "dutch_name": "Rimpelroos",
         "reason": "Boerenwormkruid houdt bladluizen en mieren op afstand — de geur is een natuurlijk afweermiddel."},
        {"scientific_name": "Sorbus aucuparia", "dutch_name": "Lijsterbes",
         "reason": "Beschermt vruchtdragende bomen tegen plagen; zelf waardplant voor diverse insecten."},
    ]},

    "Urtica dioica": {"companion_plants": [
        {"scientific_name": "Ribes sanguineum", "dutch_name": "Bloeikraal",
         "reason": "Brandnetelhoek vlakbij bessenstruiken trekt bladluisparasieten aan die ook de struiken beschermen."},
        {"scientific_name": "Filipendula ulmaria", "dutch_name": "Moerasspirea",
         "reason": "Beide houden van vochtige grond; brandnetel als waardplant voor dagpauwoog en gehakkelde aurelia."},
    ]},

    "Achillea ptarmica": {"companion_plants": [
        {"scientific_name": "Filipendula ulmaria", "dutch_name": "Moerasspirea",
         "reason": "Beide houden van vochtige bodem; nieskruid geeft sierlijk wit contrast bij de moerasspirea."},
        {"scientific_name": "Lythrum salicaria", "dutch_name": "Kattenstaart",
         "reason": "Wit-roze oevercombinatie met een lang gecombineerd bloeiseizoen."},
    ]},

    "Hypericum perforatum": {"companion_plants": [
        {"scientific_name": "Achillea millefolium", "dutch_name": "Duizendblad",
         "reason": "Droge, zonnige plekken; sint-janskruid en duizendblad vormen samen een gele zomerbloei."},
        {"scientific_name": "Thymus pulegioides", "dutch_name": "Grote tijm",
         "reason": "Beide houden van mager, goed doorlatend substraat; aanvullende bloeitijden."},
    ]},

    # ── Heesters ────────────────────────────────────────────────────────────

    "Lavandula angustifolia": {"companion_plants": [
        {"scientific_name": "Nepeta faassenii", "dutch_name": "Kattenkruid",
         "reason": "Beide lavendelblauw, geurig en droogtebestendig — samen onweerstaanbaar voor hommels."},
        {"scientific_name": "Salvia nemorosa", "dutch_name": "Salie",
         "reason": "Vergelijkbare ecologie; salie bloeit vroeger en kattenkruid vult de late zomer."},
        {"scientific_name": "Rosa rugosa", "dutch_name": "Rimpelroos",
         "reason": "Lavendel houdt bladluizen op afstand via geur en trekt bestuivers naar de roos."},
        {"scientific_name": "Allium schoenoprasum", "dutch_name": "Bieslook",
         "reason": "Beide beschermen naburige rozen: lavendel via geur, bieslook via workelexudate."},
    ]},

    "Buddleja davidii": {"companion_plants": [
        {"scientific_name": "Echinacea purpurea", "dutch_name": "Rode zonnehoed",
         "reason": "Vlindertuin-duo: buddleja trekt vlinders aan, zonnehoed biedt ook zaadvoeding voor vogels."},
        {"scientific_name": "Solidago", "dutch_name": "Guldenroede",
         "reason": "Late zomer: buddleja en guldenroede samen een ononderbroken nectarfeest voor dagvlinders."},
    ]},

    "Corylus avellana": {"companion_plants": [
        {"scientific_name": "Crataegus laevigata", "dutch_name": "Tweestijlige meidoorn",
         "reason": "Inheems heggenduet met topwaarde voor vogels en insecten; hazelaar geeft vroeg stuifmeel."},
        {"scientific_name": "Sorbus aucuparia", "dutch_name": "Lijsterbes",
         "reason": "Aanvullende vruchttijden; hazelaar in herfst, lijsterbes eerder — vogels profiteren het hele seizoen."},
    ]},

    "Viburnum opulus": {"companion_plants": [
        {"scientific_name": "Crataegus laevigata", "dutch_name": "Tweestijlige meidoorn",
         "reason": "Beide inheemse struiken met witte bloemen en kleurrijke bessen; perfect voor wildhagen."},
        {"scientific_name": "Corylus avellana", "dutch_name": "Hazelaar",
         "reason": "Inheemse haag-combinatie met maximale waarde voor vogels, vlinders en kleine zoogdieren."},
    ]},

    # ── Klimplanten ────────────────────────────────────────────────────────

    "Rosa rugosa": {"companion_plants": [
        {"scientific_name": "Allium schoenoprasum", "dutch_name": "Bieslook",
         "reason": "Bieslookwortels scheiden stoffen uit die schimmelziekten bij rozen remmen; bloeien gelijktijdig."},
        {"scientific_name": "Lavandula angustifolia", "dutch_name": "Lavendel",
         "reason": "Klassieke combinatie: lavendel houdt bladluizen op afstand en trekt nuttige insecten."},
        {"scientific_name": "Nepeta faassenii", "dutch_name": "Kattenkruid",
         "reason": "Kattenkruid bedekt de voet van de roos, houdt onkruid weg en trekt bijen aan."},
        {"scientific_name": "Tanacetum vulgare", "dutch_name": "Boerenwormkruid",
         "reason": "Sterke geur houdt mieren en bladluizen op afstand — ideaal als bodembedekker bij rozen."},
    ]},

    "Lonicera periclymenum": {"companion_plants": [
        {"scientific_name": "Clematis jackmanii", "dutch_name": "Bosrank / Clematis",
         "reason": "Wilde kamperfoelie en clematis wisselen elkaar af op een muur of pergola met lang gecombineerd bloeiseizoen."},
        {"scientific_name": "Hedera helix", "dutch_name": "Klimop",
         "reason": "Klimop als wintergroene basis, kamperfoelie als zomerbloei — samen het hele jaar interessant."},
    ]},

    "Clematis jackmanii": {"companion_plants": [
        {"scientific_name": "Rosa rugosa", "dutch_name": "Rimpelroos",
         "reason": "Roos als steunstructuur, clematis klautert erdoorheen — klassieke combinatie voor een erfafscheiding."},
        {"scientific_name": "Lonicera periclymenum", "dutch_name": "Wilde kamperfoelie",
         "reason": "Aanvullende bloeitijden op een muur of pergola; samen weken lang bloei en geuren."},
    ]},

    # ── Eenjarigen ────────────────────────────────────────────────────────

    "Calendula officinalis": {"companion_plants": [
        {"scientific_name": "Tagetes", "dutch_name": "Afrikaantje",
         "reason": "Goudsbloem en afrikaantje vormen samen een kleurrijke val voor bladluizen en werven zweefvliegen."},
        {"scientific_name": "Achillea millefolium", "dutch_name": "Duizendblad",
         "reason": "Goudsbloem als jaarlijkse aanvulling; duizendblad en goudsbloem trekken dezelfde nuttige insecten."},
        {"scientific_name": "Centaurea cyanus", "dutch_name": "Korenbloem",
         "reason": "Korenbloem-goudsbloem combo: blauw-geel, lang bloeiend, uitstekend voor wilde bijen."},
    ]},

    "Tagetes": {"companion_plants": [
        {"scientific_name": "Calendula officinalis", "dutch_name": "Goudsbloem",
         "reason": "Complementaire traplanten voor bladluizen; samen een effectief scherm voor het moestuinbed."},
        {"scientific_name": "Helianthus annuus", "dutch_name": "Zonnebloem",
         "reason": "Afrikaantje als lage rand bij zonnebloemen; de geur houdt schade-insecten weg."},
    ]},

    "Centaurea cyanus": {"companion_plants": [
        {"scientific_name": "Papaver rhoeas", "dutch_name": "Klaproos",
         "reason": "Klassiek akkerbloemen-duo; samen een hummend blauw-rood mengsel dat bijen en vlinders lokt."},
        {"scientific_name": "Leucanthemum vulgare", "dutch_name": "Gewone margriet",
         "reason": "Akkerbloemenweidemengsel met aanvullende kleuren; samen een levend schilderij voor insecten."},
        {"scientific_name": "Calendula officinalis", "dutch_name": "Goudsbloem",
         "reason": "Blauw-geel contrast; beide eenjarig en beide topbronnen voor pollen."},
    ]},

    "Helianthus annuus": {"companion_plants": [
        {"scientific_name": "Centaurea cyanus", "dutch_name": "Korenbloem",
         "reason": "Klassieke hoogte-contrast combinatie; korenbloem als lage rand bij hoge zonnebloemen."},
        {"scientific_name": "Cosmos bipinnatus", "dutch_name": "Cosmea",
         "reason": "Beide luchtige zomerbloemen die worden gewaardeerd door solitaire bijen en zweefvliegen."},
        {"scientific_name": "Tagetes", "dutch_name": "Afrikaantje",
         "reason": "Afrikaantje houdt onkruid en plaaginsecten weg aan de voet van de zonnebloem."},
    ]},

    "Cosmos bipinnatus": {"companion_plants": [
        {"scientific_name": "Helianthus annuus", "dutch_name": "Zonnebloem",
         "reason": "Luchtige cosmea als wandtegenwicht voor de massieve zonnebloem — samen een kleurrijke snijbloemenborder."},
        {"scientific_name": "Zinnia elegans", "dutch_name": "Zinnia",
         "reason": "Aanvullende vormen en kleuren; beide trekken dagvlinders en hommels over de hele zomer."},
    ]},

    # ── Keukenkruiden ────────────────────────────────────────────────────────

    "Allium schoenoprasum": {"companion_plants": [
        {"scientific_name": "Rosa rugosa", "dutch_name": "Rimpelroos",
         "reason": "Bieslook als klassieke voetroos: wortelexudate remmen schimmelziekten en luizen bij de roos."},
        {"scientific_name": "Lavandula angustifolia", "dutch_name": "Lavendel",
         "reason": "Twee aromatische randplanten die samen bladluizen afschrikken en bestuivers aantrekken."},
        {"scientific_name": "Calendula officinalis", "dutch_name": "Goudsbloem",
         "reason": "Bieslook en goudsbloem naast de groentebedden: een dubbel beschermend scherm."},
    ]},

    "Mentha x piperita": {"companion_plants": [
        {"scientific_name": "Allium schoenoprasum", "dutch_name": "Bieslook",
         "reason": "Beide sterk geurend; samen de ideale rand tegen bladluizen en koolvliegen in de groentetuin."},
        {"scientific_name": "Tagetes", "dutch_name": "Afrikaantje",
         "reason": "Drievoudige bescherming: munt, bieslook en afrikaantje als geurende barrière voor plaaginsecten."},
    ]},

    # ── Bomen ────────────────────────────────────────────────────────────────

    "Alnus glutinosa": {"companion_plants": [
        {"scientific_name": "Salix aurita", "dutch_name": "Geoorde wilg",
         "reason": "Beide pioniers op natte grond; els fixeert stikstof, wilg geeft structuur — samen een natte zoom."},
        {"scientific_name": "Symphytum officinale", "dutch_name": "Smeerwortel",
         "reason": "Smeerwortel als bodembedekker onder de els; zijn bladmulch versterkt de stikstofgift van de els."},
        {"scientific_name": "Filipendula ulmaria", "dutch_name": "Moerasspirea",
         "reason": "Beide van natte standplaatsen; moerasspirea vult de onderlaag van jonge elzenbosjes."},
    ]},

    "Quercus robur": {"companion_plants": [
        {"scientific_name": "Sorbus aucuparia", "dutch_name": "Lijsterbes",
         "reason": "Lijsterbes als onderboom in het voorzomerlicht naast de eik — aanvullende waarde voor vogels."},
        {"scientific_name": "Corylus avellana", "dutch_name": "Hazelaar",
         "reason": "Hazelaar als mantelvegetatie bij de eik; samen de kern van een inheems eikenbos."},
        {"scientific_name": "Viburnum opulus", "dutch_name": "Gelderse roos",
         "reason": "Gelderse roos als zoomstruik bij de eik; beide toptieren voor biodiversiteit."},
    ]},

    "Sorbus aucuparia": {"companion_plants": [
        {"scientific_name": "Crataegus laevigata", "dutch_name": "Tweestijlige meidoorn",
         "reason": "Aanvullende vruchttijden: meidoorn in vroege zomer, lijsterbes in herfst — optimale voedselketen voor vogels."},
        {"scientific_name": "Ilex aquifolium", "dutch_name": "Hulst",
         "reason": "Lijsterbes geeft zomerbessen, hulst geeft winterbessen — samen jaarrond voedsel voor lijsters."},
        {"scientific_name": "Corylus avellana", "dutch_name": "Hazelaar",
         "reason": "Klassieke inheemse randbegroeiing; hazelaarnoten voor vogels en zoogdieren naast de bessen van lijsterbes."},
    ]},

    "Betula pubescens": {"companion_plants": [
        {"scientific_name": "Alnus glutinosa", "dutch_name": "Zwarte els",
         "reason": "Beide pioniersbomen op natte, zure grond; els fixeert stikstof ten voordele van de berk."},
        {"scientific_name": "Sorbus aucuparia", "dutch_name": "Lijsterbes",
         "reason": "Lijsterbes als onderboom in het dunne berkenlicht — samen een licht boreaal bosje."},
    ]},

}
