"""
Plantenpedia — Cultivars & variëteiten
Samenvoegen via __init__.py: CULTIVARS wordt gemerged in ENRICHMENTS.

Upload: python data/upload.py --fields cultivars
"""

# Formaat per cultivar: {"name": "'Naam'", "description": "...", "photo_url": "...", "photo_source": "..."}

CULTIVARS: dict = {

    # ── Vaste planten ────────────────────────────────────────────────────────

    "Lavandula angustifolia": {"cultivars": [
        {"name": "'Hidcote'",
         "description": "De meest geteelde lavendel: compact (40 cm), donkerpaarse bloemen, zeer aromatisch. Ideaal voor lage hagen en borders."},
        {"name": "'Munstead'",
         "description": "Vroeg bloeiende, compacte cultivar (35–40 cm) met lavendelblauw. Goed winterhard en betrouwbaar."},
        {"name": "'Vera'",
         "description": "Grotere plant (60–70 cm) met brede bloempluimen. Populair voor potpourri vanwege het hoge etherische-oliegehalte."},
        {"name": "'Rosea'",
         "description": "Zeldzamere cultivar met roze bloemen in plaats van paars. Charmante afwisseling in de border."},
    ]},

    "Salvia nemorosa": {"cultivars": [
        {"name": "'Caradonna'",
         "description": "Opvallende donkere (bijna zwarte) stengels met dieppaarse bloemen. Bijzonder decoratief en zeer geliefde cultivar voor bijen."},
        {"name": "'Mainacht'",
         "description": "Vroeg bloeiend (mei–juni) met donkerblauwpaarse aren. Compact (50 cm) en winterhard."},
        {"name": "'Blue Hill'",
         "description": "Helder lichtblauwe aren, iets later bloeiend dan andere cultivars. Elegant en lang bloeiend."},
        {"name": "'Amethyst'",
         "description": "Warm roze-lila bloemen — een zeldzamere kleur bij salie. Mooi contrast met blauwpaarse soortgenoten."},
    ]},

    "Achillea millefolium": {"cultivars": [
        {"name": "'Cerise Queen'",
         "description": "Felroze bloemen die geleidelijk vervagen naar lichtroze en crème. Klassieke tuin-cultivar voor gemengde borders."},
        {"name": "'Terracotta'",
         "description": "Warme oranjebruin-gele bloemen die verbleken tot zalmroze. Prachtige combinatie met paarse vaste planten."},
        {"name": "'Coronation Gold'",
         "description": "Krachtige plant (80–90 cm) met grote, goudgele bloemplaten. Standvastig en lang bloeiend van juni tot augustus."},
        {"name": "'Paprika'",
         "description": "Levendig rood met gele kern, verblekend naar oranje. Opvallende kleur voor de zomerborder."},
    ]},

    "Echinacea purpurea": {"cultivars": [
        {"name": "'Magnus'",
         "description": "Grote, horizontaal uitstaande bloemblaadjes (roze-paars) zonder de typische neerhangende stand. Veelgeprezen voor bijentuinen."},
        {"name": "'White Swan'",
         "description": "Witte bloemblaadjes met oranje kegel. Elegant alternatief voor de roze standaardvorm; ook geliefd bij insecten."},
        {"name": "'PowWow Wild Berry'",
         "description": "Compact (40–50 cm), diep roze-paars. Ideaal voor kleine tuinen en potten. Rijkelijk bloeiend."},
        {"name": "'Vintage Wine'",
         "description": "Donker wijnrode bloemen, sterk geurend. Bijzondere kleur in de border en uitstekend voor insecten."},
    ]},

    "Nepeta faassenii": {"cultivars": [
        {"name": "'Six Hills Giant'",
         "description": "Groot en krachtig (70–80 cm) met overvloedige lavendelblauw-paarse bloemen. Ideaal als solitair of hoge randplant."},
        {"name": "'Walker's Low'",
         "description": "Lang bloeiend (mei tot september met terugsnoeien), soepele habitus. Misschien wel de meest populaire catmint-cultivar."},
        {"name": "'Kit Cat'",
         "description": "Compact (30 cm), ideaal voor kleine borders en voorrijen. Zelfde blauwe bloemen als de grote cultivars."},
    ]},

    "Geranium sanguineum": {"cultivars": [
        {"name": "'Album'",
         "description": "Sneeuwwitte bloemen op donkergroen blad. Verlichtte versie van de fuchsiaroze standaard; mooi in schaduwrijke hoeken."},
        {"name": "'Max Frei'",
         "description": "Compact (20–25 cm), overvloedige magenta bloemen. Uitstekende bodembedekker voor randen en voorrijen."},
        {"name": "'Striatum'",
         "description": "Wit met roze adering — een delicaat vlekkenpatroon. Zeldzamer maar bijzonder decoratief."},
    ]},

    "Hosta tardiana": {"cultivars": [
        {"name": "'Halcyon'",
         "description": "Prachtig blauwgrijs blad, gemiddelde grootte (50 cm breed). Eén van de meest aanbevolen hosta's voor schaduwtuinen."},
        {"name": "'Blue Angel'",
         "description": "Groot blad (tot 90 cm breed), diep blauwgroen. Indrukwekkende solitair voor vochtrijke schaduwplaatsen."},
        {"name": "'Tardiana'",
         "description": "De soorttype: compacte blauwgroene plant met lavendelkleurige bloemen laat in het seizoen."},
    ]},

    "Heuchera micrantha": {"cultivars": [
        {"name": "'Palace Purple'",
         "description": "Klassieke tuincultivaar met donker roodpaars blad het hele seizoen. Goed voor schaduwplekken en kleurcontrasten."},
        {"name": "'Caramel'",
         "description": "Warm karamelbruin blad met roze onderkant — bijzondere kleur voor de schaduwborder."},
        {"name": "'Obsidian'",
         "description": "Bijna zwart glanzend blad, het donkerste van de soort. Indrukwekkend kleurcontrast met lichte buren."},
        {"name": "'Lime Rickey'",
         "description": "Helder kalkgroen blad — een fris alternatief op de donkere cultivars. Goed voor lichte schaduwplekken."},
    ]},

    "Paeonia": {"cultivars": [
        {"name": "'Sarah Bernhardt'",
         "description": "Grote, volle dubbelroze bloemen met een zoete geur. De bekendste snijbloem-pioen; sterk en betrouwbaar."},
        {"name": "'Festiva Maxima'",
         "description": "Witte bloemen met rode spikkels op de binnenste bloemblaadjes. Historisch ras (1851) met uitstekende geur."},
        {"name": "'Karl Rosenfield'",
         "description": "Dieprood, volledig gevuld. Opvallende kleur in de border en goed voor de snijbloemenvaas."},
        {"name": "'Shirley Temple'",
         "description": "Zacht roze bloemen die vervagen naar roomwit. Verfijnd en geurig; ideaal voor romantische tuinstijlen."},
    ]},

    "Lupinus hybriden": {"cultivars": [
        {"name": "'The Governor'",
         "description": "Prachtig blauw-witte bi-kleur bloemen. Klassieke 'Russell Lupin'; krachtig en lang bloeiseizoen."},
        {"name": "'My Castle'",
         "description": "Brik-rood met een iets blekere vlag. Warme kleur die mooi combineert met blauw en geel."},
        {"name": "'Noble Maiden'",
         "description": "Elegant wit met een subtiele crème tint. Verfijnd in een witte-plantentuin of als lichtpunt."},
        {"name": "'The Page'",
         "description": "Carmine-rood, één van de donkerste lupines. Indrukwekkend in combinatie met zilveren planten."},
    ]},

    "Verbena bonariensis": {"cultivars": [
        {"name": "'Lollipop'",
         "description": "Compactere vorm (60–80 cm vs 120 cm) met dezelfde paars-roze bloemen. Ideaal voor kleinere tuinen en potten."},
        {"name": "'Vanity'",
         "description": "Iets kortere stengels, maar met grotere bloempluimen. Rijkelijk bloeiend en aantrekkelijk voor vlinders."},
    ]},

    "Solidago": {"cultivars": [
        {"name": "'Goldenmosa'",
         "description": "Compact (75 cm), geurige gele pluimen. Minder invasief dan de wilde soort; goed voor kleinere tuinen."},
        {"name": "'Strahlenkrone'",
         "description": "Grote gele bloempluimen op stevige stengels. Lang bloeiseizoen van augustus tot oktober."},
    ]},

    # ── Heesters ────────────────────────────────────────────────────────────

    "Buddleja davidii": {"cultivars": [
        {"name": "'Black Knight'",
         "description": "De donkerste vlinderstruik: bijna zwart-paarse bloempluimen. Spectaculair contrast en hoog vlindernectar-gehalte."},
        {"name": "'White Profusion'",
         "description": "Grote witte bloempluimen met gele kern. Sterk groeiend en uitstekend voor witte tuinthema's."},
        {"name": "'Royal Red'",
         "description": "Donkerrood-paarse pluimen, krachtig groeiend. Uitstekende nectar-cultivar voor dagvlinders."},
        {"name": "'Nanho Purple'",
         "description": "Compacter (150 cm), smaller blad, paarse bloemen. Ideaal voor kleinere tuinen of als haagelement."},
    ]},

    "Hydrangea macrophylla": {"cultivars": [
        {"name": "'Nikko Blue'",
         "description": "Grote bolvormige bloemschermen, blauw op zure grond, roze op alkalische grond. Klassieke tuincultivaar."},
        {"name": "'Endless Summer'",
         "description": "Bloeien op zowel oud als nieuw hout — geeft langere bloei, ook na laat-voorjaarsvorst. Blauw of roze afhankelijk van pH."},
        {"name": "'Annabelle'",
         "description": "Technisch Hydrangea arborescens, maar veelverkocht: grote witte bolvormige bloemschermen. Winterhard en op nieuw hout bloeiend."},
    ]},

    "Calluna vulgaris": {"cultivars": [
        {"name": "'Dark Beauty'",
         "description": "Robijnrode bloemen, compact (20–25 cm). Één van de rijkelijks bloeiende zomerheide-cultivars."},
        {"name": "'Robert Chapman'",
         "description": "Bijzonder: goudgeel-oranje blad in de zomer, rood-oranje in de winter. De bloemen zijn paars."},
        {"name": "'Boskoop'",
         "description": "Koperkleurig winterblad, roze bloemen in de zomer. Aantrekkelijk jaarrond door de bladkleur."},
    ]},

    "Cornus alba": {"cultivars": [
        {"name": "'Elegantissima'",
         "description": "Bontbladig: groen blad met brede witte rand. Rode winterstengels én decoratief zomers blad — dubbele sierwaarde."},
        {"name": "'Sibirica'",
         "description": "De felste rode winterstengels van alle Cornus-cultivars. Onmisbaar in een winterborder."},
        {"name": "'Kesselringii'",
         "description": "Bijna zwart-paarse stengels in de winter — zeldzame kleur die bijzonder is in combinatie met witte sneeuw."},
    ]},

    "Mahonia aquifolium": {"cultivars": [
        {"name": "'Apollo'",
         "description": "Compact (60–80 cm), rijkelijk gele bloemen in het vroege voorjaar. Uitstekende bordplant voor schaduw."},
        {"name": "'Smaragd'",
         "description": "Helder wintergroen glanzend blad (verdriet minder dan de standaardvorm). Gele bloemen en blauwe bessen."},
    ]},

    "Viburnum opulus": {"cultivars": [
        {"name": "'Roseum' (Sneeuwbal)",
         "description": "Gevulde witte bloemschermen zonder bessen — de klassieke 'sneeuwbal'. Spectaculaire mei-bloei maar geen vruchten voor vogels."},
        {"name": "'Compactum'",
         "description": "Compactere versie (150 cm) met dezelfde witte bloemen en rode herfstbessen. Ideaal voor kleinere tuinen."},
        {"name": "'Xanthocarpum'",
         "description": "Geelgekleurde bessen in de herfst in plaats van rood — een bijzonder zeldzame variëteit."},
    ]},

    # ── Klimplanten ────────────────────────────────────────────────────────

    "Clematis jackmanii": {"cultivars": [
        {"name": "'Jackmanii'",
         "description": "De standaard grote-bloeiende clematis: dieppaarse bloemen van juli tot september. Betrouwbaar en krachtig."},
        {"name": "'Ville de Lyon'",
         "description": "Karminrode bloemen met gele meeldraden. Warm en opvallend; bloeit van juni tot september."},
        {"name": "'Nelly Moser'",
         "description": "Lichtroze bloemblaadjes met donkerroze strepen. Bloeit tweemaal per jaar. Vervaagt in volle zon."},
        {"name": "'The President'",
         "description": "Dieppaarse bloemen met een zilverachtige glans. Compact groeiend en lang bloeiend."},
    ]},

    "Rosa rugosa": {"cultivars": [
        {"name": "'Roseraie de l'Haÿ'",
         "description": "Grote, gevulde donkerroze bloemen met sterke geur. Geen rozenbottels maar continue bloei tot in de herfst."},
        {"name": "'Blanc Double de Coubert'",
         "description": "Sneeuwwitte, gevulde bloemen met een zijdeachtige glans. Sterk geurend, zeer winterhard."},
        {"name": "'Hansa'",
         "description": "Donkerrood-paarse gevulde bloemen met sterke geur, gevolgd door grote oranjerode rozenbottels."},
        {"name": "'Fru Dagmar Hastrup'",
         "description": "Sierlijk lichtroze, enkelvoudige bloemen. Compactere groeiwijze (100 cm) met grote decoratieve rozenbottels."},
    ]},

    "Wisteria sinensis": {"cultivars": [
        {"name": "'Alba'",
         "description": "Witte bloemen in lange druiventrosachtige trossen. Zelfde krachtige groei als de paarse standaard."},
        {"name": "'Prolific'",
         "description": "Rijkelijker bloeiend dan de standaardvorm, ook al op jonge leeftijd. Lila-paarse bloemen."},
    ]},

}
