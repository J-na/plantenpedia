"""
Ecologische scores per plant: score_insects, score_birds, score_soil

  score_insects : 0–5  waarde voor bijen, hommels, vlinders, zweefvliegen
  score_birds   : 0–5  waarde voor vogels (bessen, zaden, nesten, rupsen)
  score_soil    : 0–5  bodemverbeterend (stikstofbinding, diepe wortels, bodembedekking)

Scoregids:
  5 = uitzonderlijk (top-10 in zijn klasse)
  4 = uitstekend
  3 = goed / bovengemiddeld
  2 = matig / gemiddeld
  1 = beperkt
  0 = verwaarloosbaar / geen

Upload met:
    python data/upload.py --fields score_insects,score_birds,score_soil
"""

SCORES: dict = {

# ──────────────────────────────────────────────────────────────────────────────
# VASTE PLANTEN
# ──────────────────────────────────────────────────────────────────────────────

# Achillea — open bloemschermen, honderden insectensoorten
"Achillea millefolium":     {"score_insects": 5, "score_birds": 1, "score_soil": 2},
"Achillea ptarmica":        {"score_insects": 4, "score_birds": 1, "score_soil": 1},

# Acaena — kleine bloemen, beperkte waarde
"Acaena buchananii":        {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Acanthus — buisvormige bloemen enkel voor hommels
"Acanthus mollis":          {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Aconitum — speciaal voor langtonge hommels
"Aconitum carmichaelii":    {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Aegopodium — uitstekend voor zweefvliegen, ook bodembedekker
"Aegopodium podagraria":    {"score_insects": 3, "score_birds": 0, "score_soil": 2},

# Ajuga — vroege nectarplant, bodembedekker
"Ajuga reptans":            {"score_insects": 3, "score_birds": 1, "score_soil": 3},

# Alcea — bijen en hommels bezoeken de open bloemen
"Alcea rosea":              {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Alchemilla — bodembedekker, zweefvliegen
"Alchemilla mollis":        {"score_insects": 2, "score_birds": 0, "score_soil": 2},

# Aquilegia — hommels met lange tong
"Aquilegia vulgaris":       {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Arabis — vroege vlindernectarplant
"Arabis caucasica":         {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Armeria — bolvormige bloemen voor vlinders en bijen
"Armeria maritima":         {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Aster — topplant voor late insecten, vlinders
"Aster frikartii":          {"score_insects": 4, "score_birds": 1, "score_soil": 1},

# Astrantia — zweefvliegen, solitaire bijen
"Astrantia major":          {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Aubrieta — vroege vlindernectarplant
"Aubrieta":                 {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Aurinia — vroege vlindernectarplant
"Aurinia saxatilis":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Anemone — vroege nectarplant voor koninginnehommels
"Anemone blanda":           {"score_insects": 2, "score_birds": 0, "score_soil": 1},
"Anemone coronaria":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Anthriscus — topplant voor zweefvliegen en sluipwespen
"Anthriscus sylvestris":    {"score_insects": 4, "score_birds": 1, "score_soil": 2},

# Brunnera — vroege nectarplant, bodembedekker
"Brunnera macrophylla":     {"score_insects": 2, "score_birds": 0, "score_soil": 2},

# Campanula — bijen en hommels
"Campanula carpatica":      {"score_insects": 3, "score_birds": 0, "score_soil": 1},
"Campanula portenschlagiana": {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Centaurea — topplant voor bijen, hommels, vlinders
"Centaurea montana":        {"score_insects": 4, "score_birds": 1, "score_soil": 1},

# Cerastium — bodembedekker, beperkte insectenwaarde
"Cerastium tomentosum":     {"score_insects": 2, "score_birds": 0, "score_soil": 2},

# Coreopsis — zweefvliegen en kleine bijen
"Coreopsis verticillata":   {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Dianthus — vlinders en hommels
"Dianthus barbatus":        {"score_insects": 3, "score_birds": 1, "score_soil": 1},
"Dianthus deltoides":       {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Dicentra — hommels met lange tong
"Dicentra spectabilis":     {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Doronicum — vroege nectarplant
"Doronicum orientale":      {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Echinacea — topplant voor insecten
"Echinacea purpurea":       {"score_insects": 5, "score_birds": 2, "score_soil": 1},

# Echinops — bijen, hommels, vlinders op kogelbloemen
"Echinops bannaticus":      {"score_insects": 4, "score_birds": 1, "score_soil": 1},

# Euphorbia — vroege zweefvliegen
"Euphorbia epithymoides":   {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Filipendula — massa's zweefvliegen, bijen
"Filipendula ulmaria":      {"score_insects": 4, "score_birds": 1, "score_soil": 3},

# Fragaria — bijen, vruchten voor vogels
"Fragaria vesca":           {"score_insects": 3, "score_birds": 2, "score_soil": 2},

# Geranium — bijen en hommels, dichte bodembedekking
"Geranium endressii":       {"score_insects": 3, "score_birds": 0, "score_soil": 2},
"Geranium phaeum":          {"score_insects": 2, "score_birds": 0, "score_soil": 2},
"Geranium pratense":        {"score_insects": 4, "score_birds": 1, "score_soil": 2},
"Geranium sanguineum":      {"score_insects": 3, "score_birds": 0, "score_soil": 2},

# Geum — bijen en hommels
"Geum rivale":              {"score_insects": 2, "score_birds": 1, "score_soil": 2},
"Geum urbanum":             {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Gypsophila — zweefvliegen, kleine wilde bijen
"Gypsophila paniculata":    {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Helianthemum — stuifmeel voor bijen
"Helianthemum":             {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Helleborus — zeldzame winterbloei voor hommels
"Helleborus niger":         {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Heracleum — topplant voor insecten (schermbloeier)
"Heracleum sphondylium":    {"score_insects": 5, "score_birds": 1, "score_soil": 2},

# Hesperis — nachtvlinders, overdag vlinders en hommels
"Hesperis matronalis":      {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Heuchera — zweefvliegen, kleine bijen
"Heuchera micrantha":       {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Hosta — hommels en bijen bezoeken de bloemen
"Hosta tardiana":           {"score_insects": 2, "score_birds": 0, "score_soil": 2},

# Hypericum — zweefvliegen en kleine bijen
"Hypericum perforatum":     {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Iberis — vroege vlinder- en bijennectarplant
"Iberis sempervirens":      {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Iris pseudacorus — libellenhabitat, bijen
"Iris pseudacorus":         {"score_insects": 2, "score_birds": 1, "score_soil": 2},

# Knautia — topplant voor bijen, hommels, vlinders
"Knautia arvensis":         {"score_insects": 5, "score_birds": 1, "score_soil": 2},

# Lamiastrum / Lamium — hommels, bodembedekkers in schaduw
"Lamiastrum galeobdolon":   {"score_insects": 3, "score_birds": 0, "score_soil": 3},
"Lamium maculatum":         {"score_insects": 3, "score_birds": 0, "score_soil": 3},
"Lamium orvala":            {"score_insects": 3, "score_birds": 0, "score_soil": 2},

# Lavandula — topplant voor bijen, wereldberoemd
"Lavandula angustifolia":   {"score_insects": 5, "score_birds": 1, "score_soil": 1},

# Leucanthemum — zweefvliegen, bijen, vlinders
"Leucanthemum hybriden":    {"score_insects": 3, "score_birds": 1, "score_soil": 1},
"Leucanthemum vulgare":     {"score_insects": 4, "score_birds": 1, "score_soil": 2},

# Linaria — hommels met lange tong
"Linaria purpurea":         {"score_insects": 3, "score_birds": 0, "score_soil": 1},
"Linaria vulgaris":         {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Lupinus — hommels + stikstofbinder (fabaceae)
"Lupinus hybriden":         {"score_insects": 3, "score_birds": 0, "score_soil": 5},

# Lythrum — topplant voor oeverinsecten
"Lythrum salicaria":        {"score_insects": 5, "score_birds": 1, "score_soil": 3},

# Malva — bijen en stuifmeel
"Malva sylvestris":         {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Myosotis — bijen en zweefvliegen
"Myosotis scorpioides":     {"score_insects": 2, "score_birds": 1, "score_soil": 1},

# Nepeta — topplant voor bijen en vlinders
"Nepeta faassenii":         {"score_insects": 4, "score_birds": 0, "score_soil": 1},

# Nymphaea — bijen, libellenhabitat
"Nymphaea alba":            {"score_insects": 2, "score_birds": 2, "score_soil": 2},

# Origanum — absolute topper, rijkste nectarproducent
"Origanum vulgare":         {"score_insects": 5, "score_birds": 1, "score_soil": 1},

# Osteospermum — zweefvliegen en bijen
"Osteospermum cultivars":   {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Pachysandra — bodembedekker in diepe schaduw
"Pachysandra terminalis":   {"score_insects": 1, "score_birds": 0, "score_soil": 3},

# Paeonia — hommels en kevers
"Paeonia":                  {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Persicaria — bijen, zweefvliegen
"Persicaria affinis":       {"score_insects": 3, "score_birds": 1, "score_soil": 2},
"Persicaria maculosa":      {"score_insects": 2, "score_birds": 2, "score_soil": 1},

# Petasites — vroege nectarbron voor hommelkoninginnen (maart!)
"Petasites hybridus":       {"score_insects": 3, "score_birds": 0, "score_soil": 2},

# Phlox — vroege vlinders en bijen
"Phlox subulata":           {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Prunella — hommels en bijen
"Prunella vulgaris":        {"score_insects": 3, "score_birds": 1, "score_soil": 2},

# Pulmonaria — vroege nectarplant voor hommels
"Pulmonaria officinalis":   {"score_insects": 3, "score_birds": 0, "score_soil": 1},
"Pulmonaria saccharata":    {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Pulsatilla — vroege hommelnectarplant
"Pulsatilla vulgaris":      {"score_insects": 2, "score_birds": 1, "score_soil": 1},

# Ranunculus — honingbijen, hommels, zweefvliegen
"Ranunculus acris":         {"score_insects": 3, "score_birds": 1, "score_soil": 2},
"Ranunculus repens":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Sanguisorba — bijen, vlinders
"Sanguisorba officinalis":  {"score_insects": 3, "score_birds": 1, "score_soil": 2},

# Saponaria — nachtvlinders en dagvlinders
"Saponaria officinalis":    {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Sedum — zweefvliegen, bijen, vlinders
"Sedum acre":               {"score_insects": 3, "score_birds": 0, "score_soil": 1},
"Sedum spectabile":         {"score_insects": 4, "score_birds": 1, "score_soil": 1},

# Silene — vlinders en hommels
"Silene flos-cuculi":       {"score_insects": 3, "score_birds": 0, "score_soil": 2},

# Solidago — top-10 insectenplant (honderden soorten)
"Solidago":                 {"score_insects": 5, "score_birds": 2, "score_soil": 2},

# Stachys — beperkte insectenwaarde
"Stachys byzantina":        {"score_insects": 2, "score_birds": 0, "score_soil": 2},

# Symphytum — hommels met lange tong, bodemverbeterend (comfrey)
"Symphytum officinale":     {"score_insects": 3, "score_birds": 0, "score_soil": 4},

# Thymus — topplant voor bijen, vlinders, hommels
"Thymus praecox":           {"score_insects": 5, "score_birds": 0, "score_soil": 1},
"Thymus pulegioides":       {"score_insects": 5, "score_birds": 0, "score_soil": 1},

# Trifolium — absolute top voor honingbijen, stikstofbinder
"Trifolium repens":         {"score_insects": 5, "score_birds": 1, "score_soil": 5},

# Tussilago — allereerste nectarplant van het jaar
"Tussilago farfara":        {"score_insects": 3, "score_birds": 0, "score_soil": 2},

# Verbena — vlinders en hommels
"Verbena bonariensis":      {"score_insects": 4, "score_birds": 1, "score_soil": 1},

# Veronica — bijen, hommels, vlinders
"Veronica longifolia":      {"score_insects": 3, "score_birds": 0, "score_soil": 1},
"Veronica filiformis":      {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Viola — vroege nectarbron voor koninginnehommels
"Viola":                    {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# ──────────────────────────────────────────────────────────────────────────────
# WILDE PLANTEN
# ──────────────────────────────────────────────────────────────────────────────

# Alliaria — waardplant oranjetipje
"Alliaria petiolata":       {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Calystegia — langtonge hommels en dagvlinders
"Calystegia sepium":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Cardamine — waardplant oranjetipje (kritisch!)
"Cardamine pratensis":      {"score_insects": 3, "score_birds": 0, "score_soil": 2},
"Cardamine hirsuta":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Capsella — vroege nectarplant, zaden voor vogels
"Capsella bursa-pastoris":  {"score_insects": 1, "score_birds": 2, "score_soil": 1},

# Cerastium fontanum — beperkte waarde
"Cerastium fontanum":       {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Chelidonium — bijen en zweefvliegen
"Chelidonium majus":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Cirsium arvense — topplant voor vlinders, hommels, bijen
"Cirsium arvense":          {"score_insects": 5, "score_birds": 2, "score_soil": 2},

# Claytonia — beperkte waarde
"Claytonia perfoliata":     {"score_insects": 1, "score_birds": 0, "score_soil": 1},

# Elytrigia repens — invasief gras, zeer lage ecologische waarde
"Elytrigia repens":         {"score_insects": 0, "score_birds": 1, "score_soil": 1},

# Equisetum — primitieve plant, geen bloemen, beperkte waarde
"Equisetum arvense":        {"score_insects": 0, "score_birds": 0, "score_soil": 2},

# Erigeron canadensis — invasief, beperkte waarde
"Erigeron canadensis":      {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Ficaria — vroege nectarplant voor hommels
"Ficaria verna":            {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Galinsoga — beperkte waarde
"Galinsoga parviflora":     {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Galium aparine — zaden voor vogels (lijstervogel)
"Galium aparine":           {"score_insects": 1, "score_birds": 2, "score_soil": 1},

# Galium odoratum — bodembedekker in schaduw, kleine insecten
"Galium odoratum":          {"score_insects": 2, "score_birds": 0, "score_soil": 2},

# Glechoma — vroege hommelnectarplant
"Glechoma hederacea":       {"score_insects": 3, "score_birds": 0, "score_soil": 2},

# Hieracium aurantiacum — bijen en zweefvliegen
"Hieracium aurantiacum":    {"score_insects": 2, "score_birds": 1, "score_soil": 1},

# Hypericum perforatum — zweefvliegen en kleine bijen (ook in wilde planten)
# (al boven gedefinieerd)

# Matricaria chamomilla — zweefvliegen en kleine bijen
"Matricaria chamomilla":    {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Petasites hybridus — vroege nectarbron (al boven)

# Plantago lanceolata — zaden voor vogels, insecten
"Plantago lanceolata":      {"score_insects": 2, "score_birds": 3, "score_soil": 2},
"Plantago major":           {"score_insects": 1, "score_birds": 2, "score_soil": 1},

# Poa annua — verwaarloosbare waarde
"Poa annua":                {"score_insects": 0, "score_birds": 1, "score_soil": 1},

# Polygonum aviculare — zaden voor vogels
"Polygonum aviculare":      {"score_insects": 1, "score_birds": 2, "score_soil": 1},

# Pteridium aquilinum — beschutting voor dieren
"Pteridium aquilinum":      {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Rhamnus cathartica — waardplant citroentje
"Rhamnus cathartica":       {"score_insects": 3, "score_birds": 2, "score_soil": 1},

# Rumex — zaden voor vogels
"Rumex acetosa":            {"score_insects": 1, "score_birds": 3, "score_soil": 1},
"Rumex obtusifolius":       {"score_insects": 1, "score_birds": 2, "score_soil": 1},

# Senecio vulgaris — beperkte waarde
"Senecio vulgaris":         {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Solanum nigrum — bessen voor merels
"Solanum nigrum":           {"score_insects": 1, "score_birds": 3, "score_soil": 1},

# Sonchus arvensis — bijen en zweefvliegen, zaden voor vogels
"Sonchus arvensis":         {"score_insects": 3, "score_birds": 2, "score_soil": 1},

# Stellaria holostea — vroege nectarplant, zaden voor vogels
"Stellaria holostea":       {"score_insects": 2, "score_birds": 2, "score_soil": 1},

# Tanacetum — zweefvliegen, zaden voor vogels
"Tanacetum vulgare":        {"score_insects": 3, "score_birds": 2, "score_soil": 1},

# Taraxacum — absolute top-5 insectenplant
"Taraxacum officinale":     {"score_insects": 5, "score_birds": 2, "score_soil": 2},

# Urtica dioica — waardplant dagpauwoog, atalanta; ook zaden
"Urtica dioica":            {"score_insects": 4, "score_birds": 3, "score_soil": 3},
"Urtica urens":             {"score_insects": 3, "score_birds": 2, "score_soil": 2},

# Vaccinium myrtillus — bessen voor vogels, hommels
"Vaccinium myrtillus":      {"score_insects": 3, "score_birds": 4, "score_soil": 2},

# Verbascum — bijen en hommels, nestholtes in stengels
"Verbascum cultivars":      {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Atriplex hortensis — zaden voor vogels
"Atriplex hortensis":       {"score_insects": 1, "score_birds": 2, "score_soil": 1},

# ──────────────────────────────────────────────────────────────────────────────
# BOLLEN & KNOLLEN
# ──────────────────────────────────────────────────────────────────────────────

# Allium — bijen en hommels
"Allium aflatunense":       {"score_insects": 3, "score_birds": 1, "score_soil": 1},
"Allium giganteum":         {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Crocus — kritisch vroege nectarplant (maart)
"Crocus chrysanthus":       {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Dahlia — enkelvoudig: goed voor bijen; gevuld: slecht
"Dahlia hybriden":          {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Fritillaria — vroege hommelnectarplant
"Fritillaria imperialis":   {"score_insects": 2, "score_birds": 0, "score_soil": 1},
"Fritillaria meleagris":    {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Galanthus — kritisch winterbloeier voor hommelkoninginnen
"Galanthus nivalis":        {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Hyacinthus — vroege nectarplant
"Hyacinthus orientalis":    {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Muscari — vroege nectarplant voor bijen en hommels
"Muscari armeniacum":       {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Narcissus — vroege nectarplant (beperkt toegankelijk)
"Narcissus":                {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Scilla — vroege nectarplant
"Scilla siberica":          {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Tulipa — hommels bezoeken vroege tulpen
"Tulipa hybriden":          {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# ──────────────────────────────────────────────────────────────────────────────
# KUIPPLANTEN
# ──────────────────────────────────────────────────────────────────────────────

# Agapanthus — hommels en bijen
"Agapanthus hybriden":      {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Cordyline — beperkte ecologische waarde
"Cordyline australis":      {"score_insects": 0, "score_birds": 0, "score_soil": 1},

# Fuchsia — hommels met lange tong
"Fuchsia hybriden":         {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Laurus — vroege nectarbron voor bijen
"Laurus nobilis":           {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Mandevilla — tropisch, minimale ecologische waarde in NL
"Mandevilla":               {"score_insects": 0, "score_birds": 0, "score_soil": 1},

# Olea — bloemen voor bijen, vruchten voor merels
"Olea europaea":            {"score_insects": 2, "score_birds": 1, "score_soil": 1},

# Pelargonium — zweefvliegen bezoeken de bloemen
"Pelargonium zonale":       {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Petunia — beperkte ecologische waarde
"Petunia surfinia cultivars": {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# ──────────────────────────────────────────────────────────────────────────────
# EENJARIGEN
# ──────────────────────────────────────────────────────────────────────────────

# Begonia — beperkte ecologische waarde (gevulde bloemen)
"Begonia semperflorens":    {"score_insects": 0, "score_birds": 0, "score_soil": 1},

# Calendula — zweefvliegen, bijen, vlinders
"Calendula officinalis":    {"score_insects": 4, "score_birds": 1, "score_soil": 2},

# Centaurea cyanus — topplant voor bijen, hommels, vlinders
"Centaurea cyanus":         {"score_insects": 5, "score_birds": 2, "score_soil": 1},

# Cosmos — zweefvliegen, vlinders
"Cosmos bipinnatus":        {"score_insects": 4, "score_birds": 1, "score_soil": 1},

# Digitalis — buisvormig voor hommels
"Digitalis purpurea":       {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Helianthus annuus — bijen, hommels, maar ook distelvink!
"Helianthus annuus":        {"score_insects": 3, "score_birds": 4, "score_soil": 1},

# Impatiens — beperkte ecologische waarde
"Impatiens walleriana":     {"score_insects": 1, "score_birds": 0, "score_soil": 1},

# Papaver rhoeas — rijke stuifmeelplant voor bijen
"Papaver rhoeas":           {"score_insects": 4, "score_birds": 2, "score_soil": 1},

# Tagetes — zweefvliegen + aaltjeswerend
"Tagetes":                  {"score_insects": 3, "score_birds": 0, "score_soil": 2},

# Zinnia — vlinders, zweefvliegen
"Zinnia elegans":           {"score_insects": 4, "score_birds": 1, "score_soil": 1},

# ──────────────────────────────────────────────────────────────────────────────
# KEUKENKRUIDEN
# ──────────────────────────────────────────────────────────────────────────────

# Allium schoenoprasum — bijen en hommels
"Allium schoenoprasum":     {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Foeniculum — uitstekend schermbloeier voor zweefvliegen
"Foeniculum vulgare":       {"score_insects": 4, "score_birds": 1, "score_soil": 1},

# Mentha — bijen en zweefvliegen
"Mentha x piperita":        {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Petroselinum — second year: zweefvliegen, sluipwespen
"Petroselinum crispum":     {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# ──────────────────────────────────────────────────────────────────────────────
# GRASSEN
# ──────────────────────────────────────────────────────────────────────────────

# Calamagrostis — zaden voor zangvogels
"Calamagrostis x acutiflora": {"score_insects": 1, "score_birds": 3, "score_soil": 2},

# Carex — beperkte insectenwaarde, schuilplaats
"Carex buchananii":         {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Cortaderia — nestmateriaal, minimale ecologische waarde
"Cortaderia selloana":      {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Festuca — schuilplaats voor insecten en spinnen
"Festuca glauca":           {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Molinia — waardplant voor vlinders, zaden voor vogels
"Molinia caerulea":         {"score_insects": 2, "score_birds": 3, "score_soil": 2},

# Pennisetum — zaden voor vogels
"Pennisetum alopecuroides": {"score_insects": 1, "score_birds": 3, "score_soil": 1},

# ──────────────────────────────────────────────────────────────────────────────
# HEESTERS (incl. wintergroene)
# ──────────────────────────────────────────────────────────────────────────────

# Amelanchier — vroege bloemen + bessen voor vogels
"Amelanchier lamarckii":    {"score_insects": 3, "score_birds": 4, "score_soil": 1},

# Aucuba — bessen decoratief in winter, beperkte insectenwaarde
"Aucuba japonica":          {"score_insects": 0, "score_birds": 2, "score_soil": 1},

# Berberis — bessen voor vogels, bloemen voor bijen
"Berberis julianae":        {"score_insects": 2, "score_birds": 3, "score_soil": 1},
"Berberis thunbergii":      {"score_insects": 1, "score_birds": 3, "score_soil": 1},
"Berberis vulgaris":        {"score_insects": 2, "score_birds": 3, "score_soil": 1},

# Buddleja — absolute topplant voor vlinders
"Buddleja davidii":         {"score_insects": 5, "score_birds": 1, "score_soil": 1},

# Buxus — kleine bloemen voor kleine bijen, anders beperkt
"Buxus sempervirens":       {"score_insects": 1, "score_birds": 0, "score_soil": 1},

# Calluna — topplant voor honingbijen (heidehoning)
"Calluna vulgaris":         {"score_insects": 4, "score_birds": 1, "score_soil": 2},

# Cornus — bessen voor vogels, bloemen voor bijen
"Cornus alba":              {"score_insects": 2, "score_birds": 3, "score_soil": 2},
"Cornus sericea":           {"score_insects": 2, "score_birds": 3, "score_soil": 2},

# Corylus — vroege katjes voor hommels, noten voor vogels
"Corylus avellana":         {"score_insects": 3, "score_birds": 4, "score_soil": 2},

# Cotinus — kleine bloemen voor zweefvliegen
"Cotinus coggygria":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Cotoneaster — topbessenplant voor vogels
"Cotoneaster suecicus":     {"score_insects": 2, "score_birds": 5, "score_soil": 1},

# Deutzia — bijen en zweefvliegen
"Deutzia gracilis":         {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Diervilla — bijen, bodembedekker
"Diervilla sessilifolia":   {"score_insects": 2, "score_birds": 0, "score_soil": 2},

# Erica — vroege nectarplant voor koninginnehommels
"Erica carnea":             {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Forsythia — vroege hommelnectarplant
"Forsythia x intermedia":   {"score_insects": 3, "score_birds": 0, "score_soil": 1},

# Hedera helix — unieke late herfstbloei voor klimopbij + bessen voor vogels
"Hedera helix":             {"score_insects": 4, "score_birds": 4, "score_soil": 3},

# Hypericum 'Hidcote' — bijen en zweefvliegen
"Hypericum 'Hidcote'":      {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Ilex aquifolium — bessen onmisbaar voor merels in winter
"Ilex aquifolium":          {"score_insects": 2, "score_birds": 5, "score_soil": 1},

# Kerria — vroege hommelnectarplant
"Kerria japonica":          {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Laburnum — hommels voor de bloemtrossen
"Laburnum x watereri":      {"score_insects": 2, "score_birds": 0, "score_soil": 2},

# Leycesteria — bessen voor fazanten en merels
"Leycesteria formosa":      {"score_insects": 1, "score_birds": 4, "score_soil": 1},

# Ligustrum vulgare — bloemen voor bijen, bessen voor spreeuwen
"Ligustrum vulgare":        {"score_insects": 3, "score_birds": 3, "score_soil": 1},

# Lonicera nitida — beperkte ecologische waarde (als haag)
"Lonicera nitida":          {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Magnolia — vroege bloemen voor koninginnehommels
"Magnolia stellata":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},
"Magnolia x soulangeana":   {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Mahonia — vroege nectarbron voor koninginnehommels + bessen
"Mahonia aquifolium":       {"score_insects": 3, "score_birds": 3, "score_soil": 2},

# Rhododendron ponticum — invasief, beperkte waarde (giftige nectar)
"Rhododendron ponticum":    {"score_insects": 2, "score_birds": 1, "score_soil": 1},

# Ribes sanguineum — vroege koninginnehommel + bessen
"Ribes sanguineum":         {"score_insects": 3, "score_birds": 3, "score_soil": 1},

# Robinia — uitzonderlijk nectarrijk voor bijen, stikstofbinder
"Robinia pseudoacacia":     {"score_insects": 4, "score_birds": 1, "score_soil": 5},

# Rosa canina — bloemen voor bijen, rozenbottels voor vogels
"Rosa canina":              {"score_insects": 3, "score_birds": 4, "score_soil": 1},

# Salvia nemorosa — topplant voor bijen en vlinders
"Salvia nemorosa":          {"score_insects": 5, "score_birds": 1, "score_soil": 1},

# Skimmia — vroege bijen, winterbessen
"Skimmia japonica":         {"score_insects": 2, "score_birds": 2, "score_soil": 1},

# Spiraea — zweefvliegen en kleine bijen
"Spiraea nipponica":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Symphoricarpos — winterbessen voor vogels
"Symphoricarpos chenaultii": {"score_insects": 1, "score_birds": 3, "score_soil": 1},

# Viburnum — bloemen voor bijen, bessen voor vogels
"Viburnum opulus":          {"score_insects": 3, "score_birds": 4, "score_soil": 1},

# Vinca — vroege hommelnectarplant, bodembedekker
"Vinca major":              {"score_insects": 2, "score_birds": 0, "score_soil": 3},
"Vinca minor":              {"score_insects": 2, "score_birds": 0, "score_soil": 3},

# Weigela — hommels voor de buisvormige bloemen
"Weigela":                  {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# ──────────────────────────────────────────────────────────────────────────────
# KLIMPLANTEN & ROZEN
# ──────────────────────────────────────────────────────────────────────────────

# Clematis — bijen en hommels
"Clematis armandii":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},
"Clematis jackmanii":       {"score_insects": 2, "score_birds": 0, "score_soil": 1},
"Clematis vitalba":         {"score_insects": 2, "score_birds": 2, "score_soil": 1},

# Fallopia — zweefvliegen en kleine bijen (maar invasief)
"Fallopia baldschuanica":   {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Hydrangea — bijen en zweefvliegen
"Hydrangea anomala petiolaris": {"score_insects": 2, "score_birds": 0, "score_soil": 1},
"Hydrangea macrophylla":    {"score_insects": 1, "score_birds": 0, "score_soil": 1},

# Lonicera periclymenum — nachtvlinders + bessen voor vogels
"Lonicera periclymenum":    {"score_insects": 3, "score_birds": 3, "score_soil": 1},

# Parthenocissus — bessen voor spreeuwen en merels
"Parthenocissus tricuspidata": {"score_insects": 1, "score_birds": 3, "score_soil": 1},

# Rosa — open enkelvoudige rozen voor bijen, rozenbottels voor vogels
"Rosa arvensis":            {"score_insects": 2, "score_birds": 2, "score_soil": 1},
"Rosa glauca":              {"score_insects": 2, "score_birds": 2, "score_soil": 1},
"Rosa nitida":              {"score_insects": 2, "score_birds": 2, "score_soil": 1},
"Rosa rugosa":              {"score_insects": 3, "score_birds": 2, "score_soil": 1},

# Wisteria — hommels en bijen, stikstofbinder (fabaceae)
"Wisteria sinensis":        {"score_insects": 3, "score_birds": 0, "score_soil": 3},

# ──────────────────────────────────────────────────────────────────────────────
# BOMEN
# ──────────────────────────────────────────────────────────────────────────────

# Abies — kegels voor vogels, naalden voor insecten
"Abies koreana":            {"score_insects": 1, "score_birds": 2, "score_soil": 1},

# Acer — vroege nectarplant voor bijen, rupsenwaardplant
"Acer campestre":           {"score_insects": 3, "score_birds": 3, "score_soil": 2},
"Acer platanoides":         {"score_insects": 3, "score_birds": 2, "score_soil": 2},
"Acer pseudoplatanus":      {"score_insects": 3, "score_birds": 2, "score_soil": 2},

# Aesculus — nectarplant voor bijen en hommels
"Aesculus hippocastanum":   {"score_insects": 3, "score_birds": 1, "score_soil": 1},

# Alnus glutinosa — stikstofbinder (symbiose), elsenpopjes voor sijsjes
"Alnus glutinosa":          {"score_insects": 3, "score_birds": 4, "score_soil": 5},

# Betula — honderden insectensoorten, katjes voor bijen, zaden voor vogels
"Betula pendula":           {"score_insects": 3, "score_birds": 4, "score_soil": 2},
"Betula pubescens":         {"score_insects": 3, "score_birds": 4, "score_soil": 2},

# Carpinus — zaden voor sijsjes, nestgelegenheid
"Carpinus betulus":         {"score_insects": 2, "score_birds": 3, "score_soil": 2},

# Cedrus — beperkte ecologische waarde
"Cedrus atlantica":         {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Chamaecyparis — beperkte waarde
"Chamaecyparis lawsoniana": {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Citrus trifoliata — beperkte NL-waarde
"Citrus trifoliata":        {"score_insects": 1, "score_birds": 0, "score_soil": 1},

# Crataegus — topplant voor bijen én vogels (meidoornbessen)
"Crataegus laevigata":      {"score_insects": 4, "score_birds": 5, "score_soil": 1},
"Crataegus monogyna":       {"score_insects": 4, "score_birds": 5, "score_soil": 1},

# Eucalyptus — beperkte NL-ecologische waarde
"Eucalyptus gunnii":        {"score_insects": 2, "score_birds": 0, "score_soil": 1},

# Fagus — beukennootjes voor vlaamse gaai, eekhoorns; blad voor rupsen
"Fagus sylvatica":          {"score_insects": 2, "score_birds": 3, "score_soil": 2},

# Fraxinus — zaden voor vogels, waardplant voor vele insecten
"Fraxinus excelsior":       {"score_insects": 2, "score_birds": 4, "score_soil": 2},

# Ginkgo — beperkte ecologische waarde in NL
"Ginkgo biloba":            {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Larix — kegels voor vogels
"Larix decidua":            {"score_insects": 1, "score_birds": 2, "score_soil": 2},

# Picea — kegels voor kruisbek, pimpelmees; dichte beschutting
"Picea abies":              {"score_insects": 1, "score_birds": 3, "score_soil": 1},

# Pinus mugo — beperkte waarde
"Pinus mugo mughus":        {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Pinus sylvestris — kegels voor kruisbek, schors voor insecten en specht
"Pinus sylvestris":         {"score_insects": 2, "score_birds": 3, "score_soil": 1},

# Platanus — beperkte ecologische waarde in NL
"Platanus x hispanica":     {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Populus — waardplant voor honderden insecten, katjes voor bijen
"Populus alba":             {"score_insects": 3, "score_birds": 3, "score_soil": 2},
"Populus tremula":          {"score_insects": 4, "score_birds": 3, "score_soil": 2},

# Prunus — vroege bloemen voor bijen, vruchten voor vogels
"Prunus cerasifera":        {"score_insects": 3, "score_birds": 3, "score_soil": 1},
"Prunus padus":             {"score_insects": 3, "score_birds": 3, "score_soil": 1},
"Prunus spinosa":           {"score_insects": 4, "score_birds": 4, "score_soil": 1},

# Quercus robur — rijkste boom voor biodiversiteit in Europa
"Quercus robur":            {"score_insects": 5, "score_birds": 5, "score_soil": 2},

# Salix — vroege katjes zijn kritisch voor hommels; vele insectensoorten
"Salix alba":               {"score_insects": 4, "score_birds": 3, "score_soil": 3},
"Salix aurita":             {"score_insects": 4, "score_birds": 2, "score_soil": 2},
"Salix babylonica":         {"score_insects": 3, "score_birds": 2, "score_soil": 2},
"Salix x sepulcralis":      {"score_insects": 3, "score_birds": 2, "score_soil": 2},

# Sorbus aucuparia — topbessenplant voor trekvogels (kramsvogel, koperwiek)
"Sorbus aucuparia":         {"score_insects": 3, "score_birds": 5, "score_soil": 2},

# Taxus — bessen onmisbaar voor merels; dichte nestgelegenheid
"Taxus baccata":            {"score_insects": 1, "score_birds": 4, "score_soil": 1},

# Thuja — beperkte waarde
"Thuja occidentalis":       {"score_insects": 1, "score_birds": 1, "score_soil": 1},

# Tilia — absolute topplant voor bijen (lindehoning)
"Tilia x europaea":         {"score_insects": 5, "score_birds": 2, "score_soil": 2},

# Tsuga — beperkte waarde
"Tsuga canadensis":         {"score_insects": 1, "score_birds": 2, "score_soil": 1},

# x Cupressocyparis — dichte haag, minimale ecologische waarde
"x Cupressocyparis leylandii": {"score_insects": 0, "score_birds": 0, "score_soil": 1},


# Aanvullend (ontbrekend uit eerste run)
"Erysimum":                 {"score_insects": 3, "score_birds": 0, "score_soil": 1},
"Caltha palustris":         {"score_insects": 4, "score_birds": 1, "score_soil": 2},
"Bellis perennis":          {"score_insects": 2, "score_birds": 0, "score_soil": 1},

}
