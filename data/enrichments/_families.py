"""
Plantenpedia — Plantenfamilie-beschrijvingen
Upload met: python data/upload.py --families
"""

FAMILIES: dict = {

    "Asteraceae": {
        "dutch_name": "Composietenfamilie",
        "description": (
            "De composietenfamilie is met meer dan 32.000 soorten één van de grootste bloemplantefamilies ter wereld. "
            "Kenmerkend is de samengestelde bloemhoofdjes: wat eruitziet als één bloem, is in werkelijkheid een cluster "
            "van tientallen kleine buisbloemen (in het midden) omringd door lintvormige straalbloemen (aan de rand). "
            "Dit bouwplan maakt de bloemen bijzonder aantrekkelijk voor insecten: bijen, hommels, zweefvliegen en "
            "vlinders vinden er nectar en stuifmeel in grote hoeveelheden.\n\n"
            "Ecologisch zijn composieten onmisbaar: veel soorten produceren zaadpluizen (zoals paardenbloem en distel) "
            "die kleine zangvogels voeden in de herfst. Bekende vertegenwoordigers in de Nederlandse tuin zijn "
            "duizendblad (*Achillea*), zonnehoed (*Echinacea*), margriet (*Leucanthemum*), goudsbloem (*Calendula*), "
            "zonnebloem (*Helianthus*), paardenbloem (*Taraxacum*) en ridderzuring (*Cichorium*). "
            "De familie omvat ook belangrijke voedselgewassen zoals sla, artisjok en zonnebloempitten."
        ),
    },

    "Lamiaceae": {
        "dutch_name": "Lipbloemenfamilie",
        "description": (
            "De lipbloemenfamilie dankt haar naam aan de karakteristieke tweelippige bloemvorm: de bloemkroon is "
            "gesplitst in een bovenste lip (meestal twee kelkblaadjes) en een onderste lip (drie kelkblaadjes). "
            "De stengels zijn vierkant in doorsnede — een vrijwel onfeilbaar herkenningsteken in het veld. "
            "Vrijwel alle soorten bevatten aromatische etherische oliën in klierharen op blad en stengel, "
            "wat ze zowel geurig als beschermend tegen vraat maakt.\n\n"
            "De familie telt een indrukwekkende rij keukenkruiden: tijm (*Thymus*), lavendel (*Lavandula*), "
            "rozemarijn (*Salvia rosmarinus*), munt (*Mentha*), basilicum (*Ocimum*), oregano (*Origanum*) en "
            "citroenmelisse (*Melissa*). Ecologisch zijn lipbloemen topplanten voor bijen en hommels: de "
            "bloemvorm loodst insecten precies langs de meeldraden. Salie (*Salvia nemorosa*), vlindervlier "
            "(*Buddleja*, inmiddels ook hier ingedeeld) en kattenkruid (*Nepeta*) zijn populaire tuinplanten "
            "met een hoge bijenwaarde."
        ),
    },

    "Rosaceae": {
        "dutch_name": "Rozenfamilie",
        "description": (
            "De rozenfamilie is een van de meest economisch en ecologisch waardevolle plantenfamilies. "
            "Ze omvat niet alleen de sierrozen (*Rosa*), maar ook vrijwel alle bekende fruitsoorten: appel "
            "(*Malus*), peer (*Pyrus*), kers (*Prunus*), aardbei (*Fragaria*), framboos en braam (*Rubus*). "
            "Kenmerkend zijn de vijf afzonderlijke kroonblaadjes, talrijke meeldraden en de typische "
            "hypanthium — een bekervormige structuur waar kelk- en kroonblaadjes aan vastzetten.\n\n"
            "Ecologisch biedt de rozenfamilie het hele seizoen waarde: vroege bloei van sleedoorn (*Prunus spinosa*) "
            "en meidoorn (*Crataegus*) is een reddingslijn voor vroege bijen, terwijl de bessen en pitten in de herfst "
            "en winter essentieel voedsel zijn voor lijsters, spreeuwen, merels en vinken. Meidoorn en sleedoorn "
            "zijn ook belangrijke nestelplanten voor kleine zangvogels door hun doornige takstructuur."
        ),
    },

    "Ranunculaceae": {
        "dutch_name": "Ranonkelfamilie",
        "description": (
            "De ranonkelfamilie bestaat voornamelijk uit kruidachtige planten met sterk variabele bloemvormen "
            "— van de eenvoudige vijfbladige bloem van de boterbloem (*Ranunculus*) tot de gespoorde bloemen "
            "van ridderspoor (*Delphinium*) en akelei (*Aquilegia*) en de gehandschoende bloemen van monnikskap "
            "(*Aconitum*). Veel soorten bevatten giftige alkaloïden of glycosiden en zijn voor mensen en dieren "
            "gevaarlijk bij inname.\n\n"
            "Ondanks hun giftigheid zijn ranonkelachtigen waardevol voor het ecosysteem: akelei is een "
            "sleutelplant voor hommels met lange tongen, en de vroege boterbloemen bieden nectar voor "
            "voorjaarsvliegers. Winterakoniet (*Eranthis*) en Hepatica bloemen als een van de eerste "
            "planten in het jaar en zijn daarmee onmisbaar voor koninginnen bijen na de winter. "
            "Let op: monnikskap (*Aconitum*) behoort tot de giftigste planten van Europa."
        ),
    },

    "Apiaceae": {
        "dutch_name": "Schermbloemenfamilie",
        "description": (
            "De schermbloemenfamilie kenmerkt zich door samengestelde schermen: kleine bloempjes gegroepeerd "
            "in platte of gewelfde schermpjes, die samen een groter scherm vormen. De bloemen zijn open en "
            "vlak toegankelijk — ideaal voor een brede waaier aan insecten, van zweefvliegen en sluipwespen "
            "tot kleine bijsoorten die geen lange tong bezitten. Daarmee zijn schermbloemen een sleutelgroep "
            "voor biologische plaagbeheersing in de tuin.\n\n"
            "De familie omvat zowel onmisbare keuken- en geneeskruiden (wortel, peterselie, dille, venkel, "
            "angelica) als gevaarlijk giftige soorten. De gevlekte scheerling (*Conium maculatum*) en de "
            "gevlekte watereppe (*Cicuta virosa*) behoren tot de dodelijkste planten in Europa en kunnen "
            "verward worden met eetbare soorten. Fluitenkruid (*Anthriscus sylvestris*) is de belangrijkste "
            "vroege nectarplant voor sluipwespen en lieveheersbeestjes."
        ),
    },

    "Scrophulariaceae": {
        "dutch_name": "Helmkruidfamilie",
        "description": (
            "De helmkruidfamilie (in brede zin, tegenwoordig deels opgesplitst) omvat een gevarieerde groep "
            "kruidachtige planten en kleine heesters met buisvormige, vaak tweelippige bloemen. "
            "Vingerhoedskruid (*Digitalis*), ereprijs (*Veronica*), leeuwenbek (*Antirrhinum*) en "
            "helmkruid (*Scrophularia*) zijn kenmerkende vertegenwoordigers. "
            "Veel soorten zijn halfparasiet: hun wortels kunnen verbinding maken met de wortels van grassen "
            "en andere planten om water en mineralen op te nemen — dit maakt ze moeilijk in cultuur te brengen "
            "maar ecologisch interessant als structuurplant in soortenrijke graslanden.\n\n"
            "Vingerhoedskruid (*Digitalis purpurea*) bevat hartglycosiden en is giftig, maar levert "
            "aantrekkelijke buisvormige bloemen die bij uitstek geschikt zijn voor hommels. "
            "Ereprijs (*Veronica*) is een van de vroegste bloeiers en waardevol voor insecten in het voorjaar."
        ),
    },

    "Liliaceae": {
        "dutch_name": "Leliefamilie",
        "description": (
            "De leliefamilie in strikte zin omvat de lelies (*Lilium*), tulpen (*Tulipa*), hyacinten "
            "(*Hyacinthus*) en fritillaria's. In bredere interpretatie worden ook andere bolgewassen "
            "zoals narcissen, krokussen en alliums hier traditioneel bij gerekend, hoewel die tegenwoordig "
            "in aparte families zijn geplaatst. Kenmerkend zijn de zes bloemdekblaadjes (drie kelk- en "
            "drie kroonblaadjes die op elkaar lijken), zes meeldraden en een bovenstandig vruchtbeginsel.\n\n"
            "Ecologisch zijn leliefamilieleden waardevol als vroege bloeiers (krokussen, sneeuwklokjes) "
            "voor bijen na de winter. Wilde tulpen en kievitsbloemen (*Fritillaria meleagris*) zijn "
            "inheemse soorten die in vochtrijke uiterwaarden groeien. Veel bolgewassen zijn "
            "toxisch voor huisdieren, met name voor katten (lelie) en honden (ui-familie)."
        ),
    },

    "Poaceae": {
        "dutch_name": "Grassenfamilie",
        "description": (
            "De grassenfamilie is met meer dan 10.000 soorten een van de grootste plantenfamilies en "
            "ecologisch de belangrijkste: grassen bedekken zo'n veertig procent van het aardoppervlak "
            "en vormen de basis van vrijwel alle terrestrische voedselketens. Ze bloeien windbestuivend "
            "met kleine, onopvallende bloempjes in aren of pluimen. Halmen zijn hol tussen de knopen, "
            "bladen hebben een typisch ligula (tongetje) op de overgang van bladschede naar bladschijf.\n\n"
            "In de tuin leveren siergrassen het hele jaar structuur: de pluimen van rietgras "
            "(*Calamagrostis*), blauwgras (*Helictotrichon*) en parelgras (*Melica*) bewegen prachtig "
            "in de wind en bieden zaad voor muizen, mezen en vinken. Inheemse grassen zoals beemdlangbloem "
            "(*Festuca pratensis*) en knoopkruid vormen de voedingsbodem voor meer dan honderd soorten "
            "dagvlinders en nachtvlinders waarvan de rupsen op grassen leven."
        ),
    },

    "Fabaceae": {
        "dutch_name": "Vlinderbloemenfamilie",
        "description": (
            "De vlinderbloemenfamilie dankt haar naam aan de karakteristieke vlindervormige bloem, "
            "opgebouwd uit een vlag (bovenste kroonblad), twee vleugels (zijkanten) en een kiel "
            "(onderste twee vergroeide kroonblaadjes). Kenmerkend is ook de peulvrucht. "
            "Vrijwel alle soorten leven in symbiose met stikstofbindende bacteriën (*Rhizobium*) "
            "in wortelknolletjes — daardoor verbeteren ze de bodemvruchtbaarheid en hebben ze weinig "
            "extra bemesting nodig.\n\n"
            "De ecologische en economische waarde is enorm: erwt, boon, linze, soja, pinda en klaver "
            "behoren tot de belangrijkste voedselgewassen ter wereld. In de tuin zijn rode klaver "
            "(*Trifolium pratense*), rolklaver (*Lotus corniculatus*) en tuinwikke (*Vicia sativa*) "
            "topplanten voor hommels en vlinders. Lupines (*Lupinus*) zijn de waardplant voor de rups "
            "van het zeldzame blauwtje. Vlinderbloemigen zijn ook essentieel in kruidenmengsels "
            "voor akkerrandenbeheer."
        ),
    },

    "Betulaceae": {
        "dutch_name": "Berkenfamilie",
        "description": (
            "De berkenfamilie omvat loofbomen en -struiken met windbestuivende katjes: berk (*Betula*), "
            "els (*Alnus*), hazelaar (*Corylus*), haagbeuk (*Carpinus*) en zwarte els. "
            "Mannetjeskatjes produceren grote hoeveelheden stuifmeel vroeg in het voorjaar — "
            "voor bijenvolken die na de winter hun stuifmeelvoorraden moeten aanvullen is dit "
            "van levensbelang. Hazelaar bloeit al in januari–februari, ver voor de meeste andere planten.\n\n"
            "Ecologisch zijn berken en elzen sleutelsoorten: de berk is waardplant voor meer dan "
            "300 soorten insecten in Nederland. Elzen (*Alnus glutinosa*) groeien bij voorkeur langs "
            "waterkanten en zijn in staat stikstof te binden via workelknolletjes met *Frankia*-bacteriën. "
            "De zaden van els en berk zijn wintervoedsel voor sijsjes, barmsijsjes en putters."
        ),
    },

    "Salicaceae": {
        "dutch_name": "Wilgenfamilie",
        "description": (
            "De wilgenfamilie omvat wilgen (*Salix*) en populieren (*Populus*) — snel groeiende pioniers "
            "van vochtige en natte standplaatsen. Wilgen bloeien in pollen en als katjes vroeg in het "
            "voorjaar en zijn daarmee een van de meest waardevolle stuifmeel- en nectarbronnen voor "
            "bijen en hommels na de winter. Mannelijke en vrouwelijke bloemen zitten op aparte planten.\n\n"
            "Wilgen (*Salix*) zijn de waardplant voor meer dan 400 soorten insecten in Nederland — "
            "daarmee behoren ze tot de ecologisch rijkste bomen van ons land. Ze groeien snel, "
            "verdragen periodieke wateroverlast en zijn eenvoudig te vermeerderen via stekken. "
            "Knotwilgen vormen kenmerkende elementen in het Nederlandse landschap en bieden "
            "nestelmogelijkheden voor kerkuil, torenvalk en holenduif. Schietwilg en grauwe wilg "
            "zijn inheemse soorten met de hoogste insectenwaarde."
        ),
    },

    "Ericaceae": {
        "dutch_name": "Heidefamilie",
        "description": (
            "De heidefamilie omvat planten van zure, voedselarme bodems: struikhei (*Calluna vulgaris*), "
            "dophei (*Erica tetralix*), bosbes (*Vaccinium myrtillus*), rode bosbes, cranberry en "
            "rododendron. Kenmerkend zijn de urnvormige of klokvormige bloemen en de voorkeur voor "
            "zure, venige of humeuze grond met een lage pH. Veel soorten leven in symbiose met "
            "mycorrhizaschimmels die hen helpen voedingsstoffen op te nemen in de arme bodems.\n\n"
            "Heide is een van de rijkste habitats van Nederland voor insecten en reptielen: "
            "struikhei biedt van augustus tot oktober nectar aan hommels en honingbijen, "
            "terwijl de dichte structuur warmte vasthoudt voor hagedissen en adders. "
            "Bosbes is de waardplant voor de rupsen van het bosblauwtje en de heidelibel. "
            "Heidebeheer (plaggen en branden) is essentieel om de successie naar struweel te voorkomen."
        ),
    },

    "Caprifoliaceae": {
        "dutch_name": "Kamperfoeliefamilie",
        "description": (
            "De kamperfoeliefamilie omvat klimplanten, heesters en kruidachtige planten met "
            "overwegend buisvormige of trechtervormige bloemen in gecombineerde trossen of "
            "schermen. Bekende vertegenwoordigers zijn kamperfoelie (*Lonicera*), vlierbes "
            "(*Sambucus*), sneeuwbal (*Viburnum*), weigela en geitenbaard (*Aruncus*). "
            "De nectar zit diep in de bloembuis, waardoor veel soorten bij uitstek geschikt "
            "zijn voor langtonge hommels en nachtvlinders.\n\n"
            "Ecologisch zijn vlierbes (*Sambucus nigra*) en sneeuwbal (*Viburnum opulus*) "
            "bijzonder waardevol: de bessen zijn essentieel voedsel voor doortrekkende "
            "lijsters en spreeuwen in de herfst. Kamperfoelie (*Lonicera periclymenum*) "
            "geurt 's nachts het sterkst en trekt nachtvlinders aan, die op hun beurt "
            "voedsel zijn voor vleermuizen. Vlier bloeit vroeg en rijkelijk en biedt "
            "ook stuifmeel voor bijen."
        ),
    },

    "Boraginaceae": {
        "dutch_name": "Ruwbladigenfamilie",
        "description": (
            "De ruwbladigenfamilie kenmerkt zich door ruwbehaarde stengels en bladen (door stijve "
            "haren of stekeltjes) en door bloemen die in een typische schorpioenachtige bijscherm "
            "staan — de bloemen ontluiken van binnen naar buiten als een uitrolled veer. "
            "De bloemen zijn radiair symmetrisch met vijf vergroeide kroonblaadjes, vaak in "
            "helder blauw of paars — een kleur die bijzonder aantrekkelijk is voor bijen.\n\n"
            "Bernagie (*Borago officinalis*) is een van de rijkste nectarproducenten in de "
            "moestuin en trekt de hele zomer hommels aan. Slangenkruid (*Echium vulgare*) "
            "staat bekend als de beste éénjarige nectarplant voor wilde bijen in Nederland. "
            "Vergeet-mij-nietje (*Myosotis*) bloeit vroeg in het voorjaar en overbrugt het "
            "nectartekort. Ossentong (*Anchusa*) en smeerwortel (*Symphytum*) zijn waardevolle "
            "vaste planten voor bommeltuinen. Smeerwortel heeft ook een lange geschiedenis "
            "als medicinale plant."
        ),
    },

    "Geraniaceae": {
        "dutch_name": "Ooievaarsbekfamilie",
        "description": (
            "De ooievaarsbekfamilie dankt haar naam aan de lange snavelachtige vrucht die "
            "lijkt op de snavel van een ooievaar. Bij rijpheid krult deze vrucht krachtig "
            "open en slingert de zaden weg — een effectief zaadverspreidingsmechanisme. "
            "De bloemen zijn stervormig met vijf kroonblaadjes in tinten van wit, roze, "
            "paars tot diepblauw. Bladen zijn vaak gelobd of samengesteld en ruiken "
            "bij sommige soorten aromatisch.\n\n"
            "Ooievaarsbekken (*Geranium*) zijn uiterst veelzijdige tuinplanten: ze groeien "
            "in zon en schaduw, zijn winterhard en bloeien lang. Bloedooievaarsbek "
            "(*Geranium sanguineum*) en bosooievaarsbek (*G. sylvaticum*) zijn inheemse soorten "
            "die hoge ecologische waarde hebben voor wilde bijen en hommels. "
            "De kalkooievaarsbek (*G. rotundifolium*) is een pionier van droge, warme plekken "
            "en daarmee interessant voor droogtebestendig tuinieren. "
            "Tuingeraniums (*Pelargonium*) behoren tot een verwant geslacht en zijn oorspronkelijk "
            "afkomstig uit Zuid-Afrika."
        ),
    },

}
