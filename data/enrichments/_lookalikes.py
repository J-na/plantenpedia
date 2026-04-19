"""
Plantenpedia — Verwisselingsgevaar (lookalikes)
Samenvoegen via __init__.py: LOOKALIKES wordt gemerged in ENRICHMENTS.

Upload: python data/upload.py --fields lookalikes
"""

# ⚠️ LETOP: dit bestand bevat veiligheidsrelevante informatie over giftige planten.
# Formaat per item: {"name": "...", "difference": "...", "toxic": True/False}

LOOKALIKES: dict = {

    # ── GEVAARLIJKE VERWISSELINGEN ────────────────────────────────────────────

    "Anthriscus sylvestris": {"lookalikes": [
        {
            "name": "Scheerling (Conium maculatum)",
            "difference": (
                "⚠️ DODELIJK GIFTIG. Scheerling heeft paarse tot roodbruine vlekken "
                "op de gladde, holle stengel. De geur is onaangenaam (naar muizen/petroleum). "
                "Fluitenkruid ruikt zacht anijsachtig en heeft behaarde stengels zonder vlekken. "
                "Nooit proeven: alle delen van scheerling zijn dodelijk giftig."
            ),
        },
        {
            "name": "Hondspeterselie (Aethusa cynapium)",
            "difference": (
                "Giftig. Hondspeterselie heeft langere sliertachtige schermbladen (bracteolen) "
                "die maar aan één kant hangen. De bladeren zijn glanzender dan die van fluitenkruid. "
                "Ruikt onaangenaam wanneer de bladeren worden fijngewreven."
            ),
        },
    ]},

    "Heracleum sphondylium": {"lookalikes": [
        {
            "name": "Reuzenberenklauw (Heracleum mantegazzianum)",
            "difference": (
                "⚠️ GEVAARLIJK. Reuzenberenklauw wordt tot 5 meter hoog (gewone berenklauw max. ~2 m). "
                "Het sap veroorzaakt bij zonlicht ernstige brandwonden en blaren. "
                "De stengel van reuzenberenklauw heeft paarsrode vlekken en wittige haren. "
                "Niet aanraken zonder handschoenen; aanraking onmiddellijk afwassen."
            ),
        },
        {
            "name": "Scheerling (Conium maculatum)",
            "difference": (
                "⚠️ DODELIJK GIFTIG. Scheerling is kleiner, heeft paarse vlekken op de kale stengel "
                "en ruikt naar muizen. Berenklauw heeft behaarde stengels en ruikt minder onaangenaam. "
                "Scheerling heeft meer fijnvertakte bladeren."
            ),
        },
    ]},

    "Digitalis purpurea": {"lookalikes": [
        {
            "name": "Koningskaars (Verbascum cultivars)",
            "difference": (
                "⚠️ GIFTIG. Vingerhoedskruid is dodelijk giftig (hartglycosiden). "
                "Verbascum heeft gele bloemen in een dichte aar; vingerhoedskruid heeft rood-paarse "
                "buisvormige bloemen met vlekken binnenin. De bladrozet van vingerhoedskruid is ook "
                "wollig behaard maar de bladrand is gezaagd; Verbascum heeft een gladde tot wollige bladrand."
            ),
        },
        {
            "name": "Smeerwortel (Symphytum officinale)",
            "difference": (
                "⚠️ GIFTIG (vingerhoedskruid). Jonge rozetten lijken op smeerwortel. "
                "Smeerwortel heeft gladder aanvoelende bladeren (ruw maar niet fijn-viltig). "
                "Vingerhoedskruid ruikt bijna niet; de bladeren zijn opvallend wollig-zacht."
            ),
        },
    ]},

    "Aconitum carmichaelii": {"lookalikes": [
        {
            "name": "Ooievaarsbek / Geranium (jonge planten)",
            "difference": (
                "⚠️ DODELIJK GIFTIG (monnikskap). Alle delen van Aconitum zijn extreem giftig. "
                "Jonge planten lijken op Geranium, maar monnikskap heeft dieper ingesneden, "
                "glanzig donkergroene bladeren. De bloemen zijn uniek helmbloem-vormig (blauw-paars). "
                "Draag altijd handschoenen bij het omgaan met Aconitum."
            ),
        },
        {
            "name": "Ridderspoor (Delphinium)",
            "difference": (
                "Beide hebben diep ingesneden bladeren en blauwe bloemen. Delphinium heeft open "
                "sterbloemige bloemen; Aconitum heeft de kenmerkende helmbloem-vorm. "
                "Beide zijn giftig, maar Aconitum is aanzienlijk gevaarlijker."
            ),
        },
    ]},

    "Solanum nigrum": {"lookalikes": [
        {
            "name": "Wolfskers / Belladonna (Atropa belladonna)",
            "difference": (
                "⚠️ DODELIJK GIFTIG (belladonna). Zwarte nachtschade heeft kleinere bessen in trosjes; "
                "belladonna heeft grotere, enkelvoudige bessen op langere steeltjes en klokbloemige "
                "bruinpaarse bloemen. Belladonna wordt tot 1,5 m hoog. "
                "Zwarte nachtschade-bessen zijn eetbaar als ze rijp zijn; belladonna nooit."
            ),
        },
    ]},

    "Chelidonium majus": {"lookalikes": [
        {
            "name": "Stinkende gouwe — zelfwaarschuwing",
            "difference": (
                "⚠️ GIFTIG (stinkende gouwe zelf). Het oranjegelbe melksap dat vrijkomt bij beschadiging "
                "is giftig en kan huidirritatie veroorzaken. Niet met slijmvliezen in contact brengen. "
                "Lijkt op geen andere gangbare tuinplant, maar de kenmerkende oranje melksap is "
                "een heldere indicator."
            ),
        },
    ]},

    "Aquilegia vulgaris": {"lookalikes": [
        {
            "name": "Speenkruid (Ficaria verna) — als zaailing",
            "difference": (
                "Jonge zaailingen van akelei lijken op speenkruid. Akelei-zaailingen hebben "
                "samengesteld geveerde bladeren (twee niveaus); speenkruid heeft enkelvoudige, "
                "hartgewijze bladeren. Speenkruid heeft gele bloemen; akelei blauw tot rood-paars."
            ),
        },
    ]},

    # ── MILDE VERWISSELINGEN (geen veiligheidsprobleem) ───────────────────────

    "Ficaria verna": {"lookalikes": [
        {
            "name": "Gewone boterbloem (Ranunculus acris)",
            "difference": (
                "Speenkruid heeft glanzende hartgewijze bladeren en bloeit vroeg in het voorjaar; "
                "boterbloem heeft meer vingerig ingesneden bladeren en bloeit later. "
                "De wortels van speenkruid zijn knolvormig; boterbloem heeft gewone wortels. "
                "Beide zijn licht giftig (huid- en slijmvliesirritatie bij rauw eten)."
            ),
        },
    ]},

    "Ranunculus acris": {"lookalikes": [
        {
            "name": "Kruipende boterbloem (Ranunculus repens)",
            "difference": (
                "Kruipende boterbloem heeft uitlopers waarmee hij zich horizontaal verspreidt "
                "(scherpe boterbloem niet). Bladeren van kruipende boterbloem zijn iets lichter "
                "van kleur en de middelste bladslip steekt op een kort steeltje. "
                "Beide zijn licht giftig en verdragen vochtiger, vruchtbaarder bodem."
            ),
        },
    ]},

    "Cardamine pratensis": {"lookalikes": [
        {
            "name": "Kleine veldkers (Cardamine hirsuta)",
            "difference": (
                "Beide tot de waterkers-familie. Kleine veldkers (hirsuta) is kleiner en eenjarig, "
                "bloeit al in vroege lente. Pinksterbloem (pratensis) is groter, meerjarig en "
                "bloeit later (april-mei). Beide zijn eetbaar. Pinksterbloem groeit op vochtige "
                "graslanden; kleine veldkers eerder op tuinpaden en greppels."
            ),
        },
    ]},

    "Cornus alba": {"lookalikes": [
        {
            "name": "Amerikaanse kornoelje (Cornus sericea)",
            "difference": (
                "Beide struiken met rode winterstengels en witte bessen. Cornus sericea heeft "
                "iets gladdere bladeren en wit merg in de oudere stengels (Cornus alba heeft ook wit merg). "
                "In de praktijk nauwelijks te onderscheiden; qua ecologische waarde vergelijkbaar."
            ),
        },
    ]},

    "Lamium maculatum": {"lookalikes": [
        {
            "name": "Gele dovenetel (Lamiastrum galeobdolon)",
            "difference": (
                "Gele dovenetel heeft gele bloemen (gevlekte dovenetel heeft roze-paarse bloemen). "
                "Bladeren van Lamiastrum zijn zilver gevlekt en glanzender. Beide zijn niet giftig. "
                "Gele dovenetel is agressiever als bodembedekker."
            ),
        },
        {
            "name": "Gehelmde dovenetel (Lamium orvala)",
            "difference": (
                "Lamium orvala is groter en robuuster; bloemen zijn dieprose en opvallend groot. "
                "Bladeren zijn minder gevlekt. Lamium maculatum heeft kleinere, wit gevlekte bladeren."
            ),
        },
    ]},

    "Urtica dioica": {"lookalikes": [
        {
            "name": "Kleine brandnetel (Urtica urens)",
            "difference": (
                "Kleine brandnetel (urens) is eenjarig en kleiner (tot 50 cm). Grote brandnetel "
                "(dioica) is meerjarig met wortelstokken en groeit tot 150 cm. Kleine brandnetel "
                "heeft robuustere blaadjes voor zijn formaat. Beide zijn eetbaar en medicinaal bruikbaar."
            ),
        },
    ]},

    "Symphytum officinale": {"lookalikes": [
        {
            "name": "Vingerhoedskruid (Digitalis purpurea) — als rozet",
            "difference": (
                "⚠️ GIFTIG (vingerhoedskruid). Als jonge rozet kan vingerhoedskruid lijken op smeerwortel. "
                "Smeerwortel heeft ruwere, meer leerachtige bladeren met een sterke wortel-geur als je "
                "ze wrijft. Digitalis-bladeren zijn zacht-viltig en hebben een fijn tandige rand; "
                "smeerwortelblad heeft een meer gerimpeld, aderachtig oppervlak."
            ),
        },
    ]},

    "Papaver rhoeas": {"lookalikes": [
        {
            "name": "Slaapbol (Papaver somniferum)",
            "difference": (
                "Slaapbol heeft blauwig-groene, omhelsende bladeren aan de stengel; klaproos heeft "
                "behaarde, gesteelde bladeren. Slaapbol-bloemen zijn groter en vaker licht-paars "
                "of wit. Slaapbol heeft een grotere, bolvormige zaaddoos. "
                "Slaapbol bevat opiumalkaloïden en is wettelijk gereglementeerd."
            ),
        },
    ]},

    "Taraxacum officinale": {"lookalikes": [
        {
            "name": "Gewone biggenkruid (Hypochaeris radicata)",
            "difference": (
                "Biggenkruid heeft behaarde bladeren met minder diepe inkepingen dan paardenbloem. "
                "Biggenkruid heeft vertakte stengels (paardenbloem heeft één stengel per bloem). "
                "Beide zijn eetbaar. Biggenkruid groeit vaker op droge, zandige plaatsen."
            ),
        },
    ]},

    "Malva sylvestris": {"lookalikes": [
        {
            "name": "Kaasjeskruid (Malva neglecta)",
            "difference": (
                "Kaasjeskruid (neglecta) is kleiner en kruipend; wilde kaasjeskruid (sylvestris) "
                "groeit opgericht tot 1 m. Bloemen van Malva sylvestris zijn diep rose-paars met "
                "donkere strepen; M. neglecta heeft bleekroze, kleinere bloemen. "
                "Beide zijn eetbaar en medicinaal."
            ),
        },
    ]},

    "Verbascum cultivars": {"lookalikes": [
        {
            "name": "Vingerhoedskruid (Digitalis purpurea) — als rozet",
            "difference": (
                "⚠️ GIFTIG (vingerhoedskruid). Jonge rozetten van Verbascum (koningskaars) en "
                "Digitalis (vingerhoedskruid) lijken sterk op elkaar: beide hebben grote, "
                "zachte, wollige bladeren. Verbascum heeft gele bloemen in een dichte aren-pluim; "
                "Digitalis heeft rood-paarse buisvormige bloemen met inwendige vlekken."
            ),
        },
    ]},

    "Hypericum perforatum": {"lookalikes": [
        {
            "name": "Geperforeerd hertshooi — zelfnoot",
            "difference": (
                "Sint-janskruid (Hypericum perforatum) heeft kenmerkende doorzichtige oliedruppeltjes "
                "in de bladeren (zichtbaar als je het blad tegen het licht houdt). "
                "Andere Hypericum-soorten (bijv. H. 'Hidcote') zijn tuinvariëteiten die niet medicinaal "
                "actief zijn. Sint-janskruid kan interacties geven met bepaalde medicijnen."
            ),
        },
    ]},

}
