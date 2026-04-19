"""
Plantenpedia — Externe informatiebronnen per plant
Samenvoegen via __init__.py: SOURCES wordt gemerged in ENRICHMENTS.

Upload: python data/upload.py --fields sources
"""

# ── Helper-functies ───────────────────────────────────────────────────────────

def _wiki(name: str) -> dict:
    slug = name.replace(" ", "_")
    return {
        "title": f"Wikipedia — {name}",
        "url": f"https://nl.wikipedia.org/wiki/{slug}",
        "description": "Encyclopedische informatie over taxonomie, verspreiding en ecologie",
    }

def _pfaf(name: str) -> dict:
    slug = name.replace(" ", "+")
    return {
        "title": "Plants For A Future (PFAF)",
        "url": f"https://pfaf.org/user/Plant.aspx?LatinName={slug}",
        "description": "Eetbare en medicinale toepassingen, toxiciteit en teeltadvies",
    }

_FLORON = {
    "title": "FLORON Verspreidingsatlas",
    "url": "https://www.verspreidingsatlas.nl/",
    "description": "Actuele verspreidingsgegevens van wilde planten in Nederland",
}

# ── Categorieën ───────────────────────────────────────────────────────────────
# Planten die extra PFAF-bron krijgen (eetbaar / medicinaal gebruik)
_PFAF_PLANTS: set = {
    "Achillea millefolium", "Aegopodium podagraria", "Alliaria petiolata",
    "Allium schoenoprasum", "Alnus glutinosa", "Anthriscus sylvestris",
    "Aquilegia vulgaris", "Atriplex hortensis", "Bellis perennis",
    "Calendula officinalis", "Caltha palustris", "Capsella bursa-pastoris",
    "Cardamine pratensis", "Centaurea cyanus", "Chelidonium majus",
    "Corylus avellana", "Filipendula ulmaria", "Foeniculum vulgare",
    "Fragaria vesca", "Galium odoratum", "Geum urbanum",
    "Glechoma hederacea", "Heracleum sphondylium", "Hypericum perforatum",
    "Lamium maculatum", "Lavandula angustifolia", "Laurus nobilis",
    "Matricaria chamomilla", "Mentha x piperita", "Origanum vulgare",
    "Petroselinum crispum", "Plantago lanceolata", "Plantago major",
    "Prunella vulgaris", "Pulmonaria officinalis", "Rosa canina",
    "Rosa rugosa", "Rumex acetosa", "Sambucus nigra",
    "Saponaria officinalis", "Sorbus aucuparia", "Symphytum officinale",
    "Tanacetum vulgare", "Taraxacum officinale", "Thymus praecox",
    "Thymus pulegioides", "Trifolium repens", "Tussilago farfara",
    "Urtica dioica", "Urtica urens", "Vaccinium myrtillus",
    "Galium aparine", "Ficaria verna", "Malva sylvestris",
}

# Planten die extra FLORON-bron krijgen (inheems in Nederland/België)
_FLORON_PLANTS: set = {
    "Achillea millefolium", "Achillea ptarmica", "Aegopodium podagraria",
    "Ajuga reptans", "Alliaria petiolata", "Alnus glutinosa",
    "Anthriscus sylvestris", "Aquilegia vulgaris", "Bellis perennis",
    "Betula pendula", "Betula pubescens", "Calluna vulgaris",
    "Caltha palustris", "Campanula rotundifolia", "Capsella bursa-pastoris",
    "Cardamine hirsuta", "Cardamine pratensis", "Carpinus betulus",
    "Centaurea cyanus", "Cerastium fontanum", "Chelidonium majus",
    "Cirsium arvense", "Corylus avellana", "Crataegus laevigata",
    "Crataegus monogyna", "Digitalis purpurea", "Elytrigia repens",
    "Equisetum arvense", "Ficaria verna", "Filipendula ulmaria",
    "Fragaria vesca", "Fraxinus excelsior", "Fritillaria meleagris",
    "Galanthus nivalis", "Galium aparine", "Galium odoratum",
    "Geranium pratense", "Geranium sanguineum", "Geum rivale",
    "Geum urbanum", "Glechoma hederacea", "Hedera helix",
    "Heracleum sphondylium", "Hypericum perforatum", "Ilex aquifolium",
    "Iris pseudacorus", "Knautia arvensis", "Lamiastrum galeobdolon",
    "Lamium maculatum", "Ligustrum vulgare", "Linaria vulgaris",
    "Lonicera periclymenum", "Lythrum salicaria", "Malva sylvestris",
    "Matricaria chamomilla", "Molinia caerulea", "Myosotis scorpioides",
    "Nymphaea alba", "Origanum vulgare", "Papaver rhoeas",
    "Persicaria affinis", "Persicaria maculosa", "Petasites hybridus",
    "Plantago lanceolata", "Plantago major", "Poa annua",
    "Polygonum aviculare", "Populus alba", "Populus tremula",
    "Prunella vulgaris", "Prunus padus", "Prunus spinosa",
    "Pteridium aquilinum", "Pulmonaria officinalis", "Pulsatilla vulgaris",
    "Quercus robur", "Ranunculus acris", "Ranunculus repens",
    "Rhamnus cathartica", "Rosa arvensis", "Rosa canina",
    "Rumex acetosa", "Rumex obtusifolius", "Salix alba",
    "Salix aurita", "Sambucus nigra", "Sanguisorba officinalis",
    "Saponaria officinalis", "Senecio vulgaris", "Silene flos-cuculi",
    "Solanum nigrum", "Solidago", "Sonchus arvensis",
    "Sorbus aucuparia", "Stellaria holostea", "Symphytum officinale",
    "Tanacetum vulgare", "Taraxacum officinale", "Taxus baccata",
    "Thymus praecox", "Thymus pulegioides", "Trifolium repens",
    "Tussilago farfara", "Urtica dioica", "Urtica urens",
    "Vaccinium myrtillus", "Viburnum opulus", "Vinca minor",
    "Knautia arvensis", "Erica carnea",
}

# ── Alle planten in de encyclopedie ──────────────────────────────────────────
_ALL_PLANTS = [
    "Abies koreana", "Acaena buchananii", "Acanthus mollis",
    "Acer campestre", "Acer platanoides", "Acer pseudoplatanus",
    "Achillea millefolium", "Achillea ptarmica", "Aconitum carmichaelii",
    "Aegopodium podagraria", "Aesculus hippocastanum", "Agapanthus hybriden",
    "Ajuga reptans", "Alcea rosea", "Alchemilla mollis",
    "Alliaria petiolata", "Allium aflatunense", "Allium giganteum",
    "Allium schoenoprasum", "Alnus glutinosa", "Amelanchier lamarckii",
    "Anemone blanda", "Anemone coronaria", "Anthriscus sylvestris",
    "Aquilegia vulgaris", "Arabis caucasica", "Armeria maritima",
    "Aster frikartii", "Astrantia major", "Atriplex hortensis",
    "Aubrieta", "Aucuba japonica", "Aurinia saxatilis",
    "Begonia semperflorens", "Bellis perennis", "Berberis julianae",
    "Berberis thunbergii", "Berberis vulgaris", "Betula pendula",
    "Betula pubescens", "Brunnera macrophylla", "Buddleja davidii",
    "Buxus sempervirens", "Calamagrostis x acutiflora", "Calendula officinalis",
    "Calluna vulgaris", "Caltha palustris", "Calystegia sepium",
    "Campanula carpatica", "Campanula portenschlagiana", "Capsella bursa-pastoris",
    "Cardamine hirsuta", "Cardamine pratensis", "Carex buchananii",
    "Carpinus betulus", "Cedrus atlantica", "Centaurea cyanus",
    "Centaurea montana", "Cerastium fontanum", "Cerastium tomentosum",
    "Chamaecyparis lawsoniana", "Chelidonium majus", "Cirsium arvense",
    "Citrus trifoliata", "Claytonia perfoliata", "Clematis armandii",
    "Clematis jackmanii", "Clematis vitalba", "Cordyline australis",
    "Coreopsis verticillata", "Cornus alba", "Cornus sericea",
    "Cortaderia selloana", "Corylus avellana", "Cosmos bipinnatus",
    "Cotinus coggygria", "Cotoneaster suecicus", "Crataegus laevigata",
    "Crataegus monogyna", "Crocus chrysanthus", "Dahlia hybriden",
    "Deutzia gracilis", "Dianthus barbatus", "Dianthus deltoides",
    "Dicentra spectabilis", "Diervilla sessilifolia", "Digitalis purpurea",
    "Doronicum orientale", "Echinacea purpurea", "Echinops bannaticus",
    "Elytrigia repens", "Equisetum arvense", "Erica carnea",
    "Erigeron canadensis", "Erysimum", "Eucalyptus gunnii",
    "Euphorbia epithymoides", "Fagus sylvatica", "Fallopia baldschuanica",
    "Festuca glauca", "Ficaria verna", "Filipendula ulmaria",
    "Foeniculum vulgare", "Forsythia x intermedia", "Fragaria vesca",
    "Fraxinus excelsior", "Fritillaria imperialis", "Fritillaria meleagris",
    "Fuchsia hybriden", "Galanthus nivalis", "Galinsoga parviflora",
    "Galium aparine", "Galium odoratum", "Geranium endressii",
    "Geranium phaeum", "Geranium pratense", "Geranium sanguineum",
    "Geum rivale", "Geum urbanum", "Ginkgo biloba",
    "Glechoma hederacea", "Gypsophila paniculata", "Hedera helix",
    "Helianthemum", "Helianthus annuus", "Helleborus niger",
    "Heracleum sphondylium", "Hesperis matronalis", "Heuchera micrantha",
    "Hieracium aurantiacum", "Hosta tardiana", "Hyacinthus orientalis",
    "Hydrangea anomala petiolaris", "Hydrangea macrophylla", "Hypericum 'Hidcote'",
    "Hypericum perforatum", "Iberis sempervirens", "Ilex aquifolium",
    "Impatiens walleriana", "Iris pseudacorus", "Kerria japonica",
    "Knautia arvensis", "Laburnum x watereri", "Lamiastrum galeobdolon",
    "Lamium maculatum", "Lamium orvala", "Larix decidua",
    "Laurus nobilis", "Lavandula angustifolia", "Leucanthemum hybriden",
    "Leucanthemum vulgare", "Leycesteria formosa", "Ligustrum vulgare",
    "Linaria purpurea", "Linaria vulgaris", "Lonicera nitida",
    "Lonicera periclymenum", "Lupinus hybriden", "Lythrum salicaria",
    "Magnolia stellata", "Magnolia x soulangeana", "Mahonia aquifolium",
    "Malva sylvestris", "Mandevilla", "Matricaria chamomilla",
    "Mentha x piperita", "Molinia caerulea", "Muscari armeniacum",
    "Myosotis scorpioides", "Narcissus", "Nepeta faassenii",
    "Nymphaea alba", "Olea europaea", "Origanum vulgare",
    "Osteospermum cultivars", "Pachysandra terminalis", "Paeonia",
    "Papaver rhoeas", "Parthenocissus tricuspidata", "Pelargonium zonale",
    "Pennisetum alopecuroides", "Persicaria affinis", "Persicaria maculosa",
    "Petasites hybridus", "Petroselinum crispum", "Petunia surfinia cultivars",
    "Phlox subulata", "Picea abies", "Pinus mugo mughus",
    "Pinus sylvestris", "Plantago lanceolata", "Plantago major",
    "Platanus x hispanica", "Poa annua", "Polygonum aviculare",
    "Populus alba", "Populus tremula", "Prunella vulgaris",
    "Prunus cerasifera", "Prunus padus", "Prunus spinosa",
    "Pteridium aquilinum", "Pulmonaria officinalis", "Pulmonaria saccharata",
    "Pulsatilla vulgaris", "Quercus robur", "Ranunculus acris",
    "Ranunculus repens", "Rhamnus cathartica", "Rhododendron ponticum",
    "Ribes sanguineum", "Robinia pseudoacacia", "Rosa arvensis",
    "Rosa canina", "Rosa glauca", "Rosa nitida",
    "Rosa rugosa", "Rumex acetosa", "Rumex obtusifolius",
    "Salix alba", "Salix aurita", "Salix babylonica",
    "Salix x sepulcralis", "Salvia nemorosa", "Sambucus nigra",
    "Sanguisorba officinalis", "Saponaria officinalis", "Scilla siberica",
    "Sedum acre", "Sedum spectabile", "Senecio vulgaris",
    "Silene flos-cuculi", "Skimmia japonica", "Solanum nigrum",
    "Solidago", "Sonchus arvensis", "Sorbus aucuparia",
    "Spiraea nipponica", "Stachys byzantina", "Stellaria holostea",
    "Symphoricarpos chenaultii", "Symphytum officinale", "Tagetes",
    "Tanacetum vulgare", "Taraxacum officinale", "Taxus baccata",
    "Thuja occidentalis", "Thymus praecox", "Thymus pulegioides",
    "Tilia x europaea", "Trifolium repens", "Tsuga canadensis",
    "Tulipa hybriden", "Tussilago farfara", "Urtica dioica",
    "Urtica urens", "Vaccinium myrtillus", "Verbascum cultivars",
    "Verbena bonariensis", "Veronica filiformis", "Veronica longifolia",
    "Viburnum opulus", "Vinca major", "Vinca minor",
    "Viola", "Weigela", "Wisteria sinensis",
    "Zinnia elegans", "x Cupressocyparis leylandii",
]

# ── SOURCES dict opbouwen ─────────────────────────────────────────────────────
SOURCES: dict = {}
for _name in _ALL_PLANTS:
    _srcs = [_wiki(_name)]
    if _name in _PFAF_PLANTS:
        _srcs.append(_pfaf(_name))
    if _name in _FLORON_PLANTS:
        _srcs.append(_FLORON)
    SOURCES[_name] = {"sources": _srcs}
