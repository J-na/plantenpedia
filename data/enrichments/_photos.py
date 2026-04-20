"""
Plantenpedia — Foto's per plant (alle categorieën)

Elke plant krijgt idealiter 3 foto's met een type:
  "bloeiwijze"  — bloem of bloeiwijze
  "habitus"     — totaalplant / habitusfoto
  "blad"        — blad of jonge plant
  "vrucht"      — vrucht, bes of zaad

Samenvoegen via __init__.py → overschrijft de photos-sleutel per plant.
Upload: python data/upload.py --fields photos
"""
from ._helpers import wiki

PHOTOS: dict = {

# ══════════════════════════════════════════════════════════════════════════════
# WILDE PLANTEN & WATERPLANTEN
# ══════════════════════════════════════════════════════════════════════════════

"Caltha palustris": {"photos": [
    wiki("Caltha_palustris_1.jpg", "Dotterbloem in bloei", type_="bloeiwijze"),
    wiki("Caltha_palustris_Sturm18.jpg", "Botanische illustratie dotterbloem", type_="habitus"),
    wiki("Caltha_palustris_leaf.jpg", "Dotterbloem — blad", type_="blad"),
]},

"Iris pseudacorus": {"photos": [
    wiki("Iris_pseudacorus(01).jpg", "Gele lis in bloei", type_="bloeiwijze"),
    wiki("Iris_pseudacorus_kz02.jpg", "Gele lis — habitus", type_="habitus"),
    wiki("Yellow_flag_iris_(Iris_pseudacorus)_seed_pods.jpg", "Gele lis — zaaddozen", type_="vrucht"),
]},

"Nymphaea alba": {"photos": [
    wiki("Nymphaea_alba_kz01.jpg", "Waterlelie in bloei", type_="bloeiwijze"),
    wiki("Nymphaea_alba_1.jpg", "Waterlelie — habitus", type_="habitus"),
    wiki("Nuphar_lutea_leaf_ies.jpg", "Drijfblad waterplant", type_="blad"),
]},

"Lythrum salicaria": {"photos": [
    wiki("Lythrum_salicaria_kz01.jpg", "Kattenstaart in bloei", type_="bloeiwijze"),
    wiki("Lythrum_salicaria,_2014-09-15,_O'Hara_Twp,_01.jpg", "Kattenstaart langs oever", type_="habitus"),
    wiki("Lythrum_salicaria_leaves.jpg", "Kattenstaart — blad", type_="blad"),
]},

"Aegopodium podagraria": {"photos": [
    wiki("Aegopodium_podagraria1_ies.jpg", "Zevenblad in bloei", type_="bloeiwijze"),
    wiki("Aegopodium_podagraria_kz01.jpg", "Zevenblad — habitus", type_="habitus"),
    wiki("Aegopodium_podagraria_Sturm18.jpg", "Zevenblad — bladeren", type_="blad"),
]},

"Taraxacum officinale": {"photos": [
    wiki("Taraxacum_officinale_kz02.jpg", "Paardenbloem in bloei", type_="bloeiwijze"),
    wiki("Taraxacum_officinale_-_seed_head.jpg", "Paardenbloem — zaadbol", type_="vrucht"),
    wiki("Taraxacum_officinale_kz01.jpg", "Paardenbloem — rozet", type_="blad"),
]},

"Urtica dioica": {"photos": [
    wiki("Urtica_dioica,_AJT_Johnsingh._P1100576.jpg", "Grote brandnetel", type_="bloeiwijze"),
    wiki("Urtica_dioica_subsp._dioica_kz01.jpg", "Brandnetel — habitus", type_="habitus"),
    wiki("Urtica_dioica_leaf.jpg", "Brandnetel — blad", type_="blad"),
]},

"Bellis perennis": {"photos": [
    wiki("Bellis_perennis(01).jpg", "Madeliefje in bloei", type_="bloeiwijze"),
    wiki("Bellis_perennis_L._01.jpg", "Madeliefje in gazon", type_="habitus"),
    wiki("Bellis_perennis_kz02.jpg", "Madeliefje — rozet", type_="blad"),
]},

"Matricaria chamomilla": {"photos": [
    wiki("Matricaria_recutita.RH.jpg", "Echte kamille in bloei", type_="bloeiwijze"),
    wiki("Matricaria_chamomilla_kz01.jpg", "Kamille — habitus", type_="habitus"),
    wiki("Matricaria_chamomilla_Sturm18.jpg", "Kamille — botanische illustratie", type_="blad"),
]},

"Leucanthemum vulgare": {"photos": [
    wiki("Leucanthemum_vulgare(1).jpg", "Gewone margriet in bloei", type_="bloeiwijze"),
    wiki("Leucanthemum_vulgare_kz01.jpg", "Margriet — habitus", type_="habitus"),
    wiki("Leucanthemum_vulgare_Sturm18.jpg", "Margriet — botanische illustratie", type_="blad"),
]},

"Papaver rhoeas": {"photos": [
    wiki("Papaver_rhoeas_kz01.jpg", "Klaproos in bloei", type_="bloeiwijze"),
    wiki("Papaver_rhoeas'_field(28182472016).jpg", "Klaprozen in korenveld", type_="habitus"),
    wiki("Papaver_rhoeas_-_seed_pod.jpg", "Klaproos — zaaddoos", type_="vrucht"),
]},

"Anthriscus sylvestris": {"photos": [
    wiki("Anthriscus_sylvestris(01).jpg", "Fluitenkruid in bloei", type_="bloeiwijze"),
    wiki("Anthriscus_sylvestris_kz01.jpg", "Fluitenkruid — habitus", type_="habitus"),
    wiki("Anthriscus_sylvestris_Sturm18.jpg", "Fluitenkruid — botanische illustratie", type_="blad"),
]},

"Chelidonium majus": {"photos": [
    wiki("Chelidonium_majus_kz1.jpg", "Stinkende gouwe in bloei", type_="bloeiwijze"),
    wiki("Chelidonium_majus_kz02.jpg", "Stinkende gouwe — habitus", type_="habitus"),
    wiki("Chelidonium_majus_Sturm18.jpg", "Stinkende gouwe — botanische illustratie", type_="blad"),
]},

"Alliaria petiolata": {"photos": [
    wiki("Alliaria_petiolata_kz02.jpg", "Look-zonder-look in bloei", type_="bloeiwijze"),
    wiki("Alliaria_petiolata_kz01.jpg", "Look-zonder-look — habitus", type_="habitus"),
    wiki("Alliaria_petiolata_Sturm18.jpg", "Look-zonder-look — blad", type_="blad"),
]},

"Cardamine pratensis": {"photos": [
    wiki("Cardamine_pratensis_flowers.jpg", "Pinksterbloem in bloei", type_="bloeiwijze"),
    wiki("Cardamine_pratensis_kz01.jpg", "Pinksterbloem — habitus", type_="habitus"),
    wiki("Cardamine_pratensis_Sturm18.jpg", "Pinksterbloem — botanische illustratie", type_="blad"),
]},

"Glechoma hederacea": {"photos": [
    wiki("Glechoma_hederacea,_2022-04-25,_Mellon_Park,_01.jpg", "Hondsdraf in bloei", type_="bloeiwijze"),
    wiki("Glechoma_hederacea_kz01.jpg", "Hondsdraf — habitus", type_="habitus"),
    wiki("Glechoma_hederacea_Sturm18.jpg", "Hondsdraf — blad", type_="blad"),
]},

"Rumex acetosa": {"photos": [
    wiki("Rumex_acetosa_kz02.jpg", "Veldzuring in bloei", type_="bloeiwijze"),
    wiki("Rumex_acetosa_kz01.jpg", "Veldzuring — habitus", type_="habitus"),
    wiki("Rumex_acetosa_Sturm18.jpg", "Veldzuring — blad", type_="blad"),
]},

"Plantago lanceolata": {"photos": [
    wiki("Plantago_lanceolata_kz1.jpg", "Smalle weegbree in bloei", type_="bloeiwijze"),
    wiki("Plantago_lanceolata_kz02.jpg", "Smalle weegbree — habitus", type_="habitus"),
    wiki("Plantago_lanceolata_Sturm18.jpg", "Smalle weegbree — blad", type_="blad"),
]},

"Trifolium repens": {"photos": [
    wiki("Trifolium_repens_kz01.jpg", "Witte klaver in bloei", type_="bloeiwijze"),
    wiki("Trifolium_repens_kz02.jpg", "Witte klaver — habitus", type_="habitus"),
    wiki("Trifolium_repens_Sturm18.jpg", "Witte klaver — blad", type_="blad"),
]},

"Cirsium arvense": {"photos": [
    wiki("Cirsium_arvense_kz01.jpg", "Akkerdistel in bloei", type_="bloeiwijze"),
    wiki("Cirsium_arvense_kz02.jpg", "Akkerdistel — habitus", type_="habitus"),
    wiki("Cirsium_arvense_Sturm18.jpg", "Akkerdistel — blad", type_="blad"),
]},

"Plantago major": {"photos": [
    wiki("Plantago_major_kz01.jpg", "Grote weegbree in bloei", type_="bloeiwijze"),
    wiki("Plantago_major_kz02.jpg", "Grote weegbree — habitus", type_="habitus"),
    wiki("Plantago_major_Sturm18.jpg", "Grote weegbree — blad", type_="blad"),
]},

"Stellaria holostea": {"photos": [
    wiki("Stellaria_holostea_kz01.jpg", "Grote muur in bloei", type_="bloeiwijze"),
    wiki("Stellaria_holostea_1.jpg", "Grote muur — habitus", type_="habitus"),
    wiki("Stellaria_holostea_Sturm18.jpg", "Grote muur — blad", type_="blad"),
]},

"Geum rivale": {"photos": [
    wiki("Geum_rivale_kz01.jpg", "Knikkend nagelkruid in bloei", type_="bloeiwijze"),
    wiki("Geum_rivale_1.jpg", "Knikkend nagelkruid — habitus", type_="habitus"),
    wiki("Geum_rivale_Sturm18.jpg", "Knikkend nagelkruid — blad", type_="blad"),
]},

"Heracleum sphondylium": {"photos": [
    wiki("Heracleum_sphondylium1.jpg", "Gewone bereklauw in bloei", type_="bloeiwijze"),
    wiki("Heracleum_sphondylium_kz01.jpg", "Gewone bereklauw — habitus", type_="habitus"),
    wiki("Heracleum_sphondylium_Sturm18.jpg", "Gewone bereklauw — blad", type_="blad"),
]},

"Symphytum officinale": {"photos": [
    wiki("Symphytum_officinale_kz02.jpg", "Gewone smeerwortel in bloei", type_="bloeiwijze"),
    wiki("Symphytum_officinale_kz01.jpg", "Smeerwortel — habitus", type_="habitus"),
    wiki("Symphytum_officinale_Sturm18.jpg", "Smeerwortel — blad", type_="blad"),
]},

"Equisetum arvense": {"photos": [
    wiki("Equisetum_arvense_kz01.jpg", "Heermoes — vruchtbare stengel", type_="bloeiwijze"),
    wiki("Equisetum_arvense_kz02.jpg", "Heermoes — vegetatieve stengel", type_="habitus"),
    wiki("Equisetum_arvense_Sturm18.jpg", "Heermoes — botanische illustratie", type_="blad"),
]},

"Ficaria verna": {"photos": [
    wiki("Ficaria_verna_kz01.jpg", "Speenkruid in bloei", type_="bloeiwijze"),
    wiki("Ficaria_verna_1.jpg", "Speenkruid — habitus", type_="habitus"),
    wiki("Ficaria_verna_Sturm18.jpg", "Speenkruid — blad", type_="blad"),
]},

"Galium aparine": {"photos": [
    wiki("Galium_aparine_kz01.jpg", "Kleefkruid in bloei", type_="bloeiwijze"),
    wiki("Galium_aparine_kz02.jpg", "Kleefkruid — habitus", type_="habitus"),
    wiki("Galium_aparine_fruit.jpg", "Kleefkruid — klittende vruchten", type_="vrucht"),
]},

"Tussilago farfara": {"photos": [
    wiki("Tussilago_farfara_kz01.jpg", "Klein hoefblad in bloei", type_="bloeiwijze"),
    wiki("Tussilago_farfara_1.jpg", "Klein hoefblad — habitus", type_="habitus"),
    wiki("Tussilago_farfara_kz02.jpg", "Klein hoefblad — blad", type_="blad"),
]},

"Tanacetum vulgare": {"photos": [
    wiki("Tanacetum_vulgare_kz01.jpg", "Boerenwormkruid in bloei", type_="bloeiwijze"),
    wiki("Tanacetum_vulgare_1.jpg", "Boerenwormkruid — habitus", type_="habitus"),
    wiki("Tanacetum_vulgare_Sturm18.jpg", "Boerenwormkruid — blad", type_="blad"),
]},

"Hypericum perforatum": {"photos": [
    wiki("Hypericum_perforatum_kz01.jpg", "Sint-janskruid in bloei", type_="bloeiwijze"),
    wiki("Hypericum_perforatum_001.jpg", "Sint-janskruid — habitus", type_="habitus"),
    wiki("Hypericum_perforatum_Sturm18.jpg", "Sint-janskruid — blad", type_="blad"),
]},

"Origanum vulgare": {"photos": [
    wiki("Origanum_vulgare_kz01.jpg", "Wilde marjolein in bloei", type_="bloeiwijze"),
    wiki("Origanum_vulgare_20070821_002.jpg", "Wilde marjolein — habitus", type_="habitus"),
    wiki("Origanum_vulgare_Sturm18.jpg", "Wilde marjolein — blad", type_="blad"),
]},

"Malva sylvestris": {"photos": [
    wiki("Malva_sylvestris_kz02.jpg", "Groot kaasjeskruid in bloei", type_="bloeiwijze"),
    wiki("Malva_sylvestris_1.jpg", "Groot kaasjeskruid — habitus", type_="habitus"),
    wiki("Malva_sylvestris_Sturm18.jpg", "Groot kaasjeskruid — blad", type_="blad"),
]},

"Verbascum cultivars": {"photos": [
    wiki("Verbascum_thapsus_kz01.jpg", "Koningskaars in bloei", type_="bloeiwijze"),
    wiki("Verbascum_thapsus_1.jpg", "Koningskaars — habitus", type_="habitus"),
    wiki("Verbascum_thapsus_Sturm18.jpg", "Koningskaars — blad", type_="blad"),
]},

"Knautia arvensis": {"photos": [
    wiki("Knautia_arvensis_kz01.jpg", "Beemdkroon in bloei", type_="bloeiwijze"),
    wiki("Knautia_arvensis_1.jpg", "Beemdkroon — habitus", type_="habitus"),
    wiki("Knautia_arvensis_Sturm18.jpg", "Beemdkroon — blad", type_="blad"),
]},

"Prunella vulgaris": {"photos": [
    wiki("Prunella_vulgaris_kz01.jpg", "Gewone brunel in bloei", type_="bloeiwijze"),
    wiki("Prunella_vulgaris_kz02.jpg", "Gewone brunel — habitus", type_="habitus"),
    wiki("Prunella_vulgaris_Sturm18.jpg", "Gewone brunel — blad", type_="blad"),
]},

"Silene flos-cuculi": {"photos": [
    wiki("Silene_flos-cuculi_kz01.jpg", "Echte koekoeksbloem in bloei", type_="bloeiwijze"),
    wiki("Silene_flos-cuculi_1.jpg", "Echte koekoeksbloem — habitus", type_="habitus"),
    wiki("Silene_flos-cuculi_Sturm18.jpg", "Echte koekoeksbloem — blad", type_="blad"),
]},

"Capsella bursa-pastoris": {"photos": [
    wiki("Capsella_bursa-pastoris_kz02.jpg", "Herderstasje in bloei", type_="bloeiwijze"),
    wiki("Capsella_bursa-pastoris_kz01.jpg", "Herderstasje — habitus", type_="habitus"),
    wiki("Capsella_bursa-pastoris_Sturm18.jpg", "Herderstasje — zaadpeulen", type_="vrucht"),
]},

"Ranunculus repens": {"photos": [
    wiki("Ranunculus_repens_kz01.jpg", "Kruipende boterbloem in bloei", type_="bloeiwijze"),
    wiki("Ranunculus_repens_kz02.jpg", "Kruipende boterbloem — habitus", type_="habitus"),
    wiki("Ranunculus_repens_Sturm18.jpg", "Kruipende boterbloem — blad", type_="blad"),
]},

"Claytonia perfoliata": {"photos": [
    wiki("Claytonia_perfoliata_kz01.jpg", "Winterpostelein in bloei", type_="bloeiwijze"),
    wiki("Claytonia_perfoliata_1.jpg", "Winterpostelein — habitus", type_="habitus"),
    wiki("Claytonia_perfoliata_Sturm18.jpg", "Winterpostelein — blad", type_="blad"),
]},

"Atriplex hortensis": {"photos": [
    wiki("Atriplex_hortensis_kz01.jpg", "Tuinmelde in bloei", type_="bloeiwijze"),
    wiki("Atriplex_hortensis_1.jpg", "Tuinmelde — habitus", type_="habitus"),
    wiki("Atriplex_hortensis_Sturm18.jpg", "Tuinmelde — blad", type_="blad"),
]},

"Galinsoga parviflora": {"photos": [
    wiki("Galinsoga_parviflora_kz01.jpg", "Knopkruid in bloei", type_="bloeiwijze"),
    wiki("Galinsoga_parviflora_1.jpg", "Knopkruid — habitus", type_="habitus"),
    wiki("Galinsoga_parviflora_Sturm18.jpg", "Knopkruid — blad", type_="blad"),
]},

"Fragaria vesca": {"photos": [
    wiki("Fragaria_vesca_kz01.jpg", "Bosaardbei in bloei", type_="bloeiwijze"),
    wiki("Fragaria_vesca_1.jpg", "Bosaardbei — habitus", type_="habitus"),
    wiki("Fragaria_vesca_-_fruits.jpg", "Bosaardbei — vruchten", type_="vrucht"),
]},

"Thymus pulegioides": {"photos": [
    wiki("Thymus_pulegioides_kz01.jpg", "Grote tijm in bloei", type_="bloeiwijze"),
    wiki("Thymus_pulegioides_1.jpg", "Grote tijm — habitus", type_="habitus"),
    wiki("Thymus_pulegioides_Sturm18.jpg", "Grote tijm — blad", type_="blad"),
]},

"Geum urbanum": {"photos": [
    wiki("Geum_urbanum_kz01.jpg", "Geel nagelkruid in bloei", type_="bloeiwijze"),
    wiki("Geum_urbanum_kz02.jpg", "Geel nagelkruid — habitus", type_="habitus"),
    wiki("Geum_urbanum_Sturm18.jpg", "Geel nagelkruid — blad", type_="blad"),
]},

"Geranium pratense": {"photos": [
    wiki("Geranium_pratense_kz01.jpg", "Beemdooievaarsbek in bloei", type_="bloeiwijze"),
    wiki("Geranium_pratense_kz02.jpg", "Beemdooievaarsbek — habitus", type_="habitus"),
    wiki("Geranium_pratense_Sturm18.jpg", "Beemdooievaarsbek — blad", type_="blad"),
]},

"Saponaria officinalis": {"photos": [
    wiki("Saponaria_officinalis_kz01.jpg", "Zeepkruid in bloei", type_="bloeiwijze"),
    wiki("Saponaria_officinalis_1.jpg", "Zeepkruid — habitus", type_="habitus"),
    wiki("Saponaria_officinalis_Sturm18.jpg", "Zeepkruid — blad", type_="blad"),
]},

"Veronica longifolia": {"photos": [
    wiki("Veronica_longifolia_kz01.jpg", "Langbladige ereprijs in bloei", type_="bloeiwijze"),
    wiki("Veronica_longifolia_1.jpg", "Langbladige ereprijs — habitus", type_="habitus"),
    wiki("Veronica_longifolia_Sturm18.jpg", "Langbladige ereprijs — blad", type_="blad"),
]},

"Myosotis scorpioides": {"photos": [
    wiki("Myosotis_scorpioides_kz01.jpg", "Moerasvergeet-mij-nietje in bloei", type_="bloeiwijze"),
    wiki("Myosotis_scorpioides_1.jpg", "Moerasvergeet-mij-nietje — habitus", type_="habitus"),
    wiki("Myosotis_scorpioides_Sturm18.jpg", "Moerasvergeet-mij-nietje — blad", type_="blad"),
]},

"Achillea ptarmica": {"photos": [
    wiki("Achillea_ptarmica_kz01.jpg", "Wilde bertram in bloei", type_="bloeiwijze"),
    wiki("Achillea_ptarmica_1.jpg", "Wilde bertram — habitus", type_="habitus"),
    wiki("Achillea_ptarmica_Sturm18.jpg", "Wilde bertram — blad", type_="blad"),
]},

"Linaria vulgaris": {"photos": [
    wiki("Linaria_vulgaris_kz01.jpg", "Vlasbekje in bloei", type_="bloeiwijze"),
    wiki("Linaria_vulgaris_kz02.jpg", "Vlasbekje — habitus", type_="habitus"),
    wiki("Linaria_vulgaris_Sturm18.jpg", "Vlasbekje — blad", type_="blad"),
]},

"Hieracium aurantiacum": {"photos": [
    wiki("Hieracium_aurantiacum_kz01.jpg", "Oranje havikskruid in bloei", type_="bloeiwijze"),
    wiki("Hieracium_aurantiacum_1.jpg", "Oranje havikskruid — habitus", type_="habitus"),
    wiki("Hieracium_aurantiacum_Sturm18.jpg", "Oranje havikskruid — blad", type_="blad"),
]},

"Calystegia sepium": {"photos": [
    wiki("Calystegia_sepium_kz01.jpg", "Haagwinde in bloei", type_="bloeiwijze"),
    wiki("Calystegia_sepium_1.jpg", "Haagwinde — habitus", type_="habitus"),
    wiki("Calystegia_sepium_Sturm18.jpg", "Haagwinde — blad", type_="blad"),
]},

"Cardamine hirsuta": {"photos": [
    wiki("Cardamine_hirsuta_kz01.jpg", "Kleine veldkers in bloei", type_="bloeiwijze"),
    wiki("Cardamine_hirsuta_1.jpg", "Kleine veldkers — habitus", type_="habitus"),
    wiki("Cardamine_hirsuta_Sturm18.jpg", "Kleine veldkers — blad", type_="blad"),
]},

"Cerastium fontanum": {"photos": [
    wiki("Cerastium_fontanum_kz01.jpg", "Gewone hoornbloem in bloei", type_="bloeiwijze"),
    wiki("Cerastium_fontanum_1.jpg", "Gewone hoornbloem — habitus", type_="habitus"),
    wiki("Cerastium_fontanum_Sturm18.jpg", "Gewone hoornbloem — blad", type_="blad"),
]},

"Elytrigia repens": {"photos": [
    wiki("Elytrigia_repens_kz01.jpg", "Kweekgras — aarpluim", type_="bloeiwijze"),
    wiki("Elytrigia_repens_1.jpg", "Kweekgras — habitus", type_="habitus"),
    wiki("Elytrigia_repens_Sturm18.jpg", "Kweekgras — botanische illustratie", type_="blad"),
]},

"Erigeron canadensis": {"photos": [
    wiki("Erigeron_canadensis_kz01.jpg", "Canadees fijnstraal in bloei", type_="bloeiwijze"),
    wiki("Erigeron_canadensis_1.jpg", "Canadees fijnstraal — habitus", type_="habitus"),
    wiki("Erigeron_canadensis_Sturm18.jpg", "Canadees fijnstraal — blad", type_="blad"),
]},

"Persicaria maculosa": {"photos": [
    wiki("Persicaria_maculosa_kz01.jpg", "Perzikkruid in bloei", type_="bloeiwijze"),
    wiki("Persicaria_maculosa_kz02.jpg", "Perzikkruid — habitus", type_="habitus"),
    wiki("Persicaria_maculosa_Sturm18.jpg", "Perzikkruid — blad", type_="blad"),
]},

"Petasites hybridus": {"photos": [
    wiki("Petasites_hybridus_kz01.jpg", "Groot hoefblad in bloei", type_="bloeiwijze"),
    wiki("Petasites_hybridus_kz02.jpg", "Groot hoefblad — habitus", type_="habitus"),
    wiki("Petasites_hybridus_leaf.jpg", "Groot hoefblad — reuzenblad", type_="blad"),
]},

"Poa annua": {"photos": [
    wiki("Poa_annua_kz01.jpg", "Straatgras — pluim", type_="bloeiwijze"),
    wiki("Poa_annua_1.jpg", "Straatgras — habitus", type_="habitus"),
    wiki("Poa_annua_Sturm18.jpg", "Straatgras — botanische illustratie", type_="blad"),
]},

"Polygonum aviculare": {"photos": [
    wiki("Polygonum_aviculare_kz01.jpg", "Varkensgras in bloei", type_="bloeiwijze"),
    wiki("Polygonum_aviculare_1.jpg", "Varkensgras — habitus", type_="habitus"),
    wiki("Polygonum_aviculare_Sturm18.jpg", "Varkensgras — blad", type_="blad"),
]},

"Pteridium aquilinum": {"photos": [
    wiki("Pteridium_aquilinum_kz01.jpg", "Adelaarsvaren — habitus", type_="habitus"),
    wiki("Pteridium_aquilinum_1.jpg", "Adelaarsvaren — blad", type_="blad"),
    wiki("Pteridium_aquilinum_fiddleheads.jpg", "Adelaarsvaren — jonge scheuten", type_="blad"),
]},

"Ranunculus acris": {"photos": [
    wiki("Ranunculus_acris_kz01.jpg", "Scherpe boterbloem in bloei", type_="bloeiwijze"),
    wiki("Ranunculus_acris_kz02.jpg", "Scherpe boterbloem — habitus", type_="habitus"),
    wiki("Ranunculus_acris_Sturm18.jpg", "Scherpe boterbloem — blad", type_="blad"),
]},

"Rumex obtusifolius": {"photos": [
    wiki("Rumex_obtusifolius_kz01.jpg", "Ridderzuring in bloei", type_="bloeiwijze"),
    wiki("Rumex_obtusifolius_kz02.jpg", "Ridderzuring — habitus", type_="habitus"),
    wiki("Rumex_obtusifolius_Sturm18.jpg", "Ridderzuring — blad", type_="blad"),
]},

"Sedum acre": {"photos": [
    wiki("Sedum_acre_kz01.jpg", "Muurpeper in bloei", type_="bloeiwijze"),
    wiki("Sedum_acre_kz02.jpg", "Muurpeper — habitus", type_="habitus"),
    wiki("Sedum_acre_Sturm18.jpg", "Muurpeper — blad", type_="blad"),
]},

"Senecio vulgaris": {"photos": [
    wiki("Senecio_vulgaris_kz01.jpg", "Klein kruiskruid in bloei", type_="bloeiwijze"),
    wiki("Senecio_vulgaris_1.jpg", "Klein kruiskruid — habitus", type_="habitus"),
    wiki("Senecio_vulgaris_Sturm18.jpg", "Klein kruiskruid — blad", type_="blad"),
]},

"Solanum nigrum": {"photos": [
    wiki("Solanum_nigrum_kz01.jpg", "Zwarte nachtschade in bloei", type_="bloeiwijze"),
    wiki("Solanum_nigrum_kz02.jpg", "Zwarte nachtschade — habitus", type_="habitus"),
    wiki("Solanum_nigrum_fruit.jpg", "Zwarte nachtschade — bessen", type_="vrucht"),
]},

"Sonchus arvensis": {"photos": [
    wiki("Sonchus_arvensis_kz01.jpg", "Akkermelkdistel in bloei", type_="bloeiwijze"),
    wiki("Sonchus_arvensis_1.jpg", "Akkermelkdistel — habitus", type_="habitus"),
    wiki("Sonchus_arvensis_Sturm18.jpg", "Akkermelkdistel — blad", type_="blad"),
]},

"Urtica urens": {"photos": [
    wiki("Urtica_urens_kz01.jpg", "Kleine brandnetel — habitus", type_="habitus"),
    wiki("Urtica_urens_1.jpg", "Kleine brandnetel in bloei", type_="bloeiwijze"),
    wiki("Urtica_urens_Sturm18.jpg", "Kleine brandnetel — blad", type_="blad"),
]},

"Veronica filiformis": {"photos": [
    wiki("Veronica_filiformis_kz01.jpg", "Draadereprijs in bloei", type_="bloeiwijze"),
    wiki("Veronica_filiformis_1.jpg", "Draadereprijs — habitus", type_="habitus"),
    wiki("Veronica_filiformis_Sturm18.jpg", "Draadereprijs — blad", type_="blad"),
]},

# ══════════════════════════════════════════════════════════════════════════════
# VASTE PLANTEN
# ══════════════════════════════════════════════════════════════════════════════

"Acaena buchananii": {"photos": [
    wiki("Acaena_buchananii_kz01.jpg", "Stekelnootje — habitus", type_="habitus"),
    wiki("Acaena_buchananii_1.jpg", "Stekelnootje — blad", type_="blad"),
]},

"Acanthus mollis": {"photos": [
    wiki("Acanthus_mollis_kz01.jpg", "Berenklauw in bloei", type_="bloeiwijze"),
    wiki("Acanthus_mollis_1.jpg", "Berenklauw — habitus", type_="habitus"),
    wiki("Acanthus_mollis_leaf.jpg", "Berenklauw — blad", type_="blad"),
]},

"Achillea millefolium": {"photos": [
    wiki("Achillea_millefolium_kz02.jpg", "Gewone duizendblad in bloei", type_="bloeiwijze"),
    wiki("Achillea_millefolium_20100523.jpg", "Duizendblad — habitus", type_="habitus"),
    wiki("Achillea_millefolium_Sturm18.jpg", "Duizendblad — blad", type_="blad"),
]},

"Aconitum carmichaelii": {"photos": [
    wiki("Aconitum_carmichaelii_kz01.jpg", "Helmbloem in bloei", type_="bloeiwijze"),
    wiki("Aconitum_carmichaelii_1.jpg", "Monnikskap — habitus", type_="habitus"),
    wiki("Aconitum_carmichaelii_Sturm18.jpg", "Monnikskap — blad", type_="blad"),
]},

"Ajuga reptans": {"photos": [
    wiki("Ajuga_reptans_kz01.jpg", "Kruipend zenegroen in bloei", type_="bloeiwijze"),
    wiki("Ajuga_reptans_1.jpg", "Zenegroen — habitus", type_="habitus"),
    wiki("Ajuga_reptans_kz02.jpg", "Zenegroen — blad", type_="blad"),
]},

"Alchemilla mollis": {"photos": [
    wiki("Alchemilla_mollis_kz01.jpg", "Vrouwenmantel in bloei", type_="bloeiwijze"),
    wiki("Alchemilla_mollis_1.jpg", "Vrouwenmantel — habitus", type_="habitus"),
    wiki("Alchemilla_mollis_kz02.jpg", "Vrouwenmantel — dauwdruppels op blad", type_="blad"),
]},

"Arabis caucasica": {"photos": [
    wiki("Arabis_caucasica_kz01.jpg", "Kaukasische scheefkelk in bloei", type_="bloeiwijze"),
    wiki("Arabis_caucasica_1.jpg", "Scheefkelk — habitus", type_="habitus"),
    wiki("Arabis_caucasica_Sturm18.jpg", "Scheefkelk — blad", type_="blad"),
]},

"Armeria maritima": {"photos": [
    wiki("Armeria_maritima_kz01.jpg", "Engels gras in bloei", type_="bloeiwijze"),
    wiki("Armeria_maritima_kz02.jpg", "Engels gras — habitus", type_="habitus"),
    wiki("Armeria_maritima_1.jpg", "Engels gras — grasachtig blad", type_="blad"),
]},

"Aster frikartii": {"photos": [
    wiki("Aster_frikartii_kz01.jpg", "Herfstaster in bloei", type_="bloeiwijze"),
    wiki("Aster_frikartii_1.jpg", "Herfstaster — habitus", type_="habitus"),
    wiki("Aster_frikartii_Monch.jpg", "Aster 'Mönch' — bloem close-up", type_="bloeiwijze"),
]},

"Astrantia major": {"photos": [
    wiki("Astrantia_major_kz01.jpg", "Grote zevenster in bloei", type_="bloeiwijze"),
    wiki("Astrantia_major_kz02.jpg", "Zevenster — habitus", type_="habitus"),
    wiki("Astrantia_major_1.jpg", "Zevenster — blad", type_="blad"),
]},

"Aubrieta": {"photos": [
    wiki("Aubrieta_deltoidea_kz01.jpg", "Aubrieta in bloei", type_="bloeiwijze"),
    wiki("Aubrieta_1.jpg", "Aubrieta — habitus", type_="habitus"),
    wiki("Aubrieta_cultivar.jpg", "Aubrieta — cultivar", type_="bloeiwijze"),
]},

"Aurinia saxatilis": {"photos": [
    wiki("Aurinia_saxatilis_kz01.jpg", "Goudkorf in bloei", type_="bloeiwijze"),
    wiki("Aurinia_saxatilis_1.jpg", "Goudkorf — habitus", type_="habitus"),
    wiki("Aurinia_saxatilis_Sturm18.jpg", "Goudkorf — blad", type_="blad"),
]},

"Brunnera macrophylla": {"photos": [
    wiki("Brunnera_macrophylla_kz01.jpg", "Groot vergeet-mij-niet in bloei", type_="bloeiwijze"),
    wiki("Brunnera_macrophylla_1.jpg", "Brunnera — habitus", type_="habitus"),
    wiki("Brunnera_macrophylla_kz02.jpg", "Brunnera — blad", type_="blad"),
]},

"Campanula carpatica": {"photos": [
    wiki("Campanula_carpatica_kz01.jpg", "Karpatische klokjesbloem in bloei", type_="bloeiwijze"),
    wiki("Campanula_carpatica_1.jpg", "Karpatische klokjesbloem — habitus", type_="habitus"),
    wiki("Campanula_carpatica_kz02.jpg", "Karpatische klokjesbloem — blad", type_="blad"),
]},

"Campanula portenschlagiana": {"photos": [
    wiki("Campanula_portenschlagiana_kz01.jpg", "Dalmatische klokjesbloem in bloei", type_="bloeiwijze"),
    wiki("Campanula_portenschlagiana_1.jpg", "Dalmatische klokjesbloem — habitus", type_="habitus"),
    wiki("Campanula_portenschlagiana_kz02.jpg", "Dalmatische klokjesbloem — blad", type_="blad"),
]},

"Centaurea montana": {"photos": [
    wiki("Centaurea_montana_kz01.jpg", "Bergkorenbloem in bloei", type_="bloeiwijze"),
    wiki("Centaurea_montana_kz02.jpg", "Bergkorenbloem — habitus", type_="habitus"),
    wiki("Centaurea_montana_Sturm18.jpg", "Bergkorenbloem — blad", type_="blad"),
]},

"Cerastium tomentosum": {"photos": [
    wiki("Cerastium_tomentosum_kz01.jpg", "Viltige hoornbloem in bloei", type_="bloeiwijze"),
    wiki("Cerastium_tomentosum_1.jpg", "Viltige hoornbloem — habitus", type_="habitus"),
    wiki("Cerastium_tomentosum_kz02.jpg", "Viltige hoornbloem — blad", type_="blad"),
]},

"Coreopsis verticillata": {"photos": [
    wiki("Coreopsis_verticillata_kz01.jpg", "Siermeisjesbloem in bloei", type_="bloeiwijze"),
    wiki("Coreopsis_verticillata_1.jpg", "Siermeisjesbloem — habitus", type_="habitus"),
    wiki("Coreopsis_verticillata_kz02.jpg", "Siermeisjesbloem — blad", type_="blad"),
]},

"Dianthus deltoides": {"photos": [
    wiki("Dianthus_deltoides_kz01.jpg", "Steenanjer in bloei", type_="bloeiwijze"),
    wiki("Dianthus_deltoides_kz02.jpg", "Steenanjer — habitus", type_="habitus"),
    wiki("Dianthus_deltoides_Sturm18.jpg", "Steenanjer — blad", type_="blad"),
]},

"Dicentra spectabilis": {"photos": [
    wiki("Lamprocapnos_spectabilis_kz01.jpg", "Gebroken hartje in bloei", type_="bloeiwijze"),
    wiki("Lamprocapnos_spectabilis_1.jpg", "Gebroken hartje — habitus", type_="habitus"),
    wiki("Lamprocapnos_spectabilis_kz02.jpg", "Gebroken hartje — blad", type_="blad"),
]},

"Doronicum orientale": {"photos": [
    wiki("Doronicum_orientale_kz01.jpg", "Geitenbloem in bloei", type_="bloeiwijze"),
    wiki("Doronicum_orientale_1.jpg", "Geitenbloem — habitus", type_="habitus"),
    wiki("Doronicum_orientale_kz02.jpg", "Geitenbloem — blad", type_="blad"),
]},

"Echinacea purpurea": {"photos": [
    wiki("Echinacea_purpurea_kz01.jpg", "Rode zonnehoed in bloei", type_="bloeiwijze"),
    wiki("Echinacea_purpurea_kz02.jpg", "Rode zonnehoed — habitus", type_="habitus"),
    wiki("Echinacea_purpurea_1.jpg", "Rode zonnehoed — zaadbol", type_="vrucht"),
]},

"Echinops bannaticus": {"photos": [
    wiki("Echinops_bannaticus_kz01.jpg", "Kogeldistel in bloei", type_="bloeiwijze"),
    wiki("Echinops_bannaticus_1.jpg", "Kogeldistel — habitus", type_="habitus"),
    wiki("Echinops_bannaticus_kz02.jpg", "Kogeldistel — blad", type_="blad"),
]},

"Erysimum": {"photos": [
    wiki("Erysimum_cheiri_kz01.jpg", "Muurbloem in bloei", type_="bloeiwijze"),
    wiki("Erysimum_cheiri_1.jpg", "Muurbloem — habitus", type_="habitus"),
    wiki("Erysimum_cheiri_kz02.jpg", "Muurbloem — blad", type_="blad"),
]},

"Euphorbia epithymoides": {"photos": [
    wiki("Euphorbia_epithymoides_kz01.jpg", "Veelkleurig wolfsmelk in bloei", type_="bloeiwijze"),
    wiki("Euphorbia_epithymoides_1.jpg", "Veelkleurig wolfsmelk — habitus", type_="habitus"),
    wiki("Euphorbia_epithymoides_kz02.jpg", "Veelkleurig wolfsmelk — blad", type_="blad"),
]},

"Foeniculum vulgare": {"photos": [
    wiki("Foeniculum_vulgare_kz01.jpg", "Venkel in bloei", type_="bloeiwijze"),
    wiki("Foeniculum_vulgare_kz02.jpg", "Venkel — habitus", type_="habitus"),
    wiki("Foeniculum_vulgare_Sturm18.jpg", "Venkel — blad", type_="blad"),
]},

"Galium odoratum": {"photos": [
    wiki("Galium_odoratum_kz01.jpg", "Lievevrouwebedstro in bloei", type_="bloeiwijze"),
    wiki("Galium_odoratum_kz02.jpg", "Lievevrouwebedstro — habitus", type_="habitus"),
    wiki("Galium_odoratum_Sturm18.jpg", "Lievevrouwebedstro — blad", type_="blad"),
]},

"Geranium endressii": {"photos": [
    wiki("Geranium_endressii_kz01.jpg", "Pyreneese ooievaarsbek in bloei", type_="bloeiwijze"),
    wiki("Geranium_endressii_1.jpg", "Pyreneese ooievaarsbek — habitus", type_="habitus"),
    wiki("Geranium_endressii_kz02.jpg", "Pyreneese ooievaarsbek — blad", type_="blad"),
]},

"Geranium sanguineum": {"photos": [
    wiki("Geranium_sanguineum_kz01.jpg", "Bloedooievaarsbek in bloei", type_="bloeiwijze"),
    wiki("Geranium_sanguineum_kz02.jpg", "Bloedooievaarsbek — habitus", type_="habitus"),
    wiki("Geranium_sanguineum_Sturm18.jpg", "Bloedooievaarsbek — blad", type_="blad"),
]},

"Gypsophila paniculata": {"photos": [
    wiki("Gypsophila_paniculata_kz01.jpg", "Gipskruid in bloei", type_="bloeiwijze"),
    wiki("Gypsophila_paniculata_1.jpg", "Gipskruid — habitus", type_="habitus"),
    wiki("Gypsophila_paniculata_kz02.jpg", "Gipskruid — blad", type_="blad"),
]},

"Helianthemum": {"photos": [
    wiki("Helianthemum_nummularium_kz01.jpg", "Zonneroosje in bloei", type_="bloeiwijze"),
    wiki("Helianthemum_nummularium_1.jpg", "Zonneroosje — habitus", type_="habitus"),
    wiki("Helianthemum_nummularium_kz02.jpg", "Zonneroosje — blad", type_="blad"),
]},

"Helleborus niger": {"photos": [
    wiki("Helleborus_niger_kz01.jpg", "Kerstroos in bloei", type_="bloeiwijze"),
    wiki("Helleborus_niger_kz02.jpg", "Kerstroos — habitus", type_="habitus"),
    wiki("Helleborus_niger_1.jpg", "Kerstroos — blad", type_="blad"),
]},

"Heuchera micrantha": {"photos": [
    wiki("Heuchera_micrantha_kz01.jpg", "Purperbel in bloei", type_="bloeiwijze"),
    wiki("Heuchera_micrantha_1.jpg", "Purperbel — habitus", type_="habitus"),
    wiki("Heuchera_micrantha_kz02.jpg", "Purperbel — decoratief blad", type_="blad"),
]},

"Hosta tardiana": {"photos": [
    wiki("Hosta_tardiana_kz01.jpg", "Blauwe hartlelie in bloei", type_="bloeiwijze"),
    wiki("Hosta_tardiana_1.jpg", "Hartlelie — habitus", type_="habitus"),
    wiki("Hosta_tardiana_kz02.jpg", "Hartlelie — blad", type_="blad"),
]},

"Iberis sempervirens": {"photos": [
    wiki("Iberis_sempervirens_kz01.jpg", "Scheefbloem in bloei", type_="bloeiwijze"),
    wiki("Iberis_sempervirens_1.jpg", "Scheefbloem — habitus", type_="habitus"),
    wiki("Iberis_sempervirens_kz02.jpg", "Scheefbloem — blad", type_="blad"),
]},

"Lamiastrum galeobdolon": {"photos": [
    wiki("Lamiastrum_galeobdolon_kz01.jpg", "Gele dovenetel in bloei", type_="bloeiwijze"),
    wiki("Lamiastrum_galeobdolon_kz02.jpg", "Gele dovenetel — habitus", type_="habitus"),
    wiki("Lamiastrum_galeobdolon_Sturm18.jpg", "Gele dovenetel — blad", type_="blad"),
]},

"Lamium maculatum": {"photos": [
    wiki("Lamium_maculatum_kz01.jpg", "Gevlekte dovenetel in bloei", type_="bloeiwijze"),
    wiki("Lamium_maculatum_kz02.jpg", "Gevlekte dovenetel — habitus", type_="habitus"),
    wiki("Lamium_maculatum_Sturm18.jpg", "Gevlekte dovenetel — blad", type_="blad"),
]},

"Lamium orvala": {"photos": [
    wiki("Lamium_orvala_kz01.jpg", "Grote dovenetel in bloei", type_="bloeiwijze"),
    wiki("Lamium_orvala_1.jpg", "Grote dovenetel — habitus", type_="habitus"),
    wiki("Lamium_orvala_kz02.jpg", "Grote dovenetel — blad", type_="blad"),
]},

"Leucanthemum hybriden": {"photos": [
    wiki("Leucanthemum_x_superbum_kz01.jpg", "Margriet-hybride in bloei", type_="bloeiwijze"),
    wiki("Leucanthemum_x_superbum_1.jpg", "Margriet-hybride — habitus", type_="habitus"),
    wiki("Leucanthemum_x_superbum_kz02.jpg", "Margriet-hybride — blad", type_="blad"),
]},

"Linaria purpurea": {"photos": [
    wiki("Linaria_purpurea_kz01.jpg", "Paars vlasbekje in bloei", type_="bloeiwijze"),
    wiki("Linaria_purpurea_1.jpg", "Paars vlasbekje — habitus", type_="habitus"),
    wiki("Linaria_purpurea_kz02.jpg", "Paars vlasbekje — blad", type_="blad"),
]},

"Lupinus hybriden": {"photos": [
    wiki("Lupinus_polyphyllus_kz01.jpg", "Lupine in bloei", type_="bloeiwijze"),
    wiki("Lupinus_polyphyllus_1.jpg", "Lupine — habitus", type_="habitus"),
    wiki("Lupinus_polyphyllus_kz02.jpg", "Lupine — handvormig blad", type_="blad"),
]},

"Nepeta faassenii": {"photos": [
    wiki("Nepeta_x_faassenii_kz01.jpg", "Kattenkruid in bloei", type_="bloeiwijze"),
    wiki("Nepeta_faassenii_1.jpg", "Kattenkruid — habitus", type_="habitus"),
    wiki("Nepeta_x_faassenii_kz02.jpg", "Kattenkruid — blad", type_="blad"),
]},

"Pachysandra terminalis": {"photos": [
    wiki("Pachysandra_terminalis_kz01.jpg", "Schaduwkruiper — habitus", type_="habitus"),
    wiki("Pachysandra_terminalis_1.jpg", "Schaduwkruiper — bodembedekker", type_="habitus"),
    wiki("Pachysandra_terminalis_kz02.jpg", "Schaduwkruiper — blad", type_="blad"),
]},

"Paeonia": {"photos": [
    wiki("Paeonia_lactiflora_kz01.jpg", "Pioen in bloei", type_="bloeiwijze"),
    wiki("Paeonia_lactiflora_1.jpg", "Pioen — habitus", type_="habitus"),
    wiki("Paeonia_lactiflora_kz02.jpg", "Pioen — blad", type_="blad"),
]},

"Persicaria affinis": {"photos": [
    wiki("Persicaria_affinis_kz01.jpg", "Laag duizendknoop in bloei", type_="bloeiwijze"),
    wiki("Persicaria_affinis_1.jpg", "Laag duizendknoop — habitus", type_="habitus"),
    wiki("Persicaria_affinis_kz02.jpg", "Laag duizendknoop — blad", type_="blad"),
]},

"Phlox subulata": {"photos": [
    wiki("Phlox_subulata_kz01.jpg", "Mosflox in bloei", type_="bloeiwijze"),
    wiki("Phlox_subulata_kz02.jpg", "Mosflox — habitus", type_="habitus"),
    wiki("Phlox_subulata_1.jpg", "Mosflox — blad", type_="blad"),
]},

"Pulmonaria saccharata": {"photos": [
    wiki("Pulmonaria_saccharata_kz01.jpg", "Bonte longkruid in bloei", type_="bloeiwijze"),
    wiki("Pulmonaria_saccharata_1.jpg", "Bonte longkruid — habitus", type_="habitus"),
    wiki("Pulmonaria_saccharata_kz02.jpg", "Bonte longkruid — gevlekt blad", type_="blad"),
]},

"Pulsatilla vulgaris": {"photos": [
    wiki("Pulsatilla_vulgaris_kz01.jpg", "Gewone pulsatilla in bloei", type_="bloeiwijze"),
    wiki("Pulsatilla_vulgaris_kz02.jpg", "Pulsatilla — habitus", type_="habitus"),
    wiki("Pulsatilla_vulgaris_-_seed_heads.jpg", "Pulsatilla — verige vruchten", type_="vrucht"),
]},

"Salvia nemorosa": {"photos": [
    wiki("Salvia_nemorosa_kz01.jpg", "Bossalie in bloei", type_="bloeiwijze"),
    wiki("Salvia_nemorosa_kz02.jpg", "Bossalie — habitus", type_="habitus"),
    wiki("Salvia_nemorosa_1.jpg", "Bossalie — blad", type_="blad"),
]},

"Sanguisorba officinalis": {"photos": [
    wiki("Sanguisorba_officinalis_kz01.jpg", "Grote pimpernel in bloei", type_="bloeiwijze"),
    wiki("Sanguisorba_officinalis_kz02.jpg", "Grote pimpernel — habitus", type_="habitus"),
    wiki("Sanguisorba_officinalis_Sturm18.jpg", "Grote pimpernel — blad", type_="blad"),
]},

"Solidago": {"photos": [
    wiki("Solidago_canadensis_kz01.jpg", "Guldenroede in bloei", type_="bloeiwijze"),
    wiki("Solidago_canadensis_kz02.jpg", "Guldenroede — habitus", type_="habitus"),
    wiki("Solidago_canadensis_1.jpg", "Guldenroede — blad", type_="blad"),
]},

"Thymus praecox": {"photos": [
    wiki("Thymus_praecox_kz01.jpg", "Kruiptijm in bloei", type_="bloeiwijze"),
    wiki("Thymus_praecox_kz02.jpg", "Kruiptijm — habitus", type_="habitus"),
    wiki("Thymus_praecox_1.jpg", "Kruiptijm — blad", type_="blad"),
]},

"Verbena bonariensis": {"photos": [
    wiki("Verbena_bonariensis_kz01.jpg", "IJzerhard in bloei", type_="bloeiwijze"),
    wiki("Verbena_bonariensis_kz02.jpg", "IJzerhard — habitus", type_="habitus"),
    wiki("Verbena_bonariensis_1.jpg", "IJzerhard — blad", type_="blad"),
]},

"Vinca major": {"photos": [
    wiki("Vinca_major_kz01.jpg", "Grote maagdenpalm in bloei", type_="bloeiwijze"),
    wiki("Vinca_major_kz02.jpg", "Grote maagdenpalm — habitus", type_="habitus"),
    wiki("Vinca_major_1.jpg", "Grote maagdenpalm — blad", type_="blad"),
]},

"Vinca minor": {"photos": [
    wiki("Vinca_minor_kz01.jpg", "Kleine maagdenpalm in bloei", type_="bloeiwijze"),
    wiki("Vinca_minor_kz02.jpg", "Kleine maagdenpalm — habitus", type_="habitus"),
    wiki("Vinca_minor_Sturm18.jpg", "Kleine maagdenpalm — blad", type_="blad"),
]},

"Viola": {"photos": [
    wiki("Viola_odorata_kz01.jpg", "Viooltje in bloei", type_="bloeiwijze"),
    wiki("Viola_odorata_kz02.jpg", "Viooltje — habitus", type_="habitus"),
    wiki("Viola_odorata_Sturm18.jpg", "Viooltje — blad", type_="blad"),
]},

"Aquilegia vulgaris": {"photos": [
    wiki("Aquilegia_vulgaris_kz01.jpg", "Wilde akelei in bloei", type_="bloeiwijze"),
    wiki("Aquilegia_vulgaris_kz02.jpg", "Wilde akelei — habitus", type_="habitus"),
    wiki("Aquilegia_vulgaris_Sturm18.jpg", "Wilde akelei — blad", type_="blad"),
]},

"Filipendula ulmaria": {"photos": [
    wiki("Filipendula_ulmaria_kz01.jpg", "Moerasspirea in bloei", type_="bloeiwijze"),
    wiki("Filipendula_ulmaria_kz02.jpg", "Moerasspirea — habitus", type_="habitus"),
    wiki("Filipendula_ulmaria_Sturm18.jpg", "Moerasspirea — blad", type_="blad"),
]},

"Geranium phaeum": {"photos": [
    wiki("Geranium_phaeum_kz01.jpg", "Donkere ooievaarsbek in bloei", type_="bloeiwijze"),
    wiki("Geranium_phaeum_kz02.jpg", "Donkere ooievaarsbek — habitus", type_="habitus"),
    wiki("Geranium_phaeum_Sturm18.jpg", "Donkere ooievaarsbek — blad", type_="blad"),
]},

"Pulmonaria officinalis": {"photos": [
    wiki("Pulmonaria_officinalis_kz01.jpg", "Gevlekt longkruid in bloei", type_="bloeiwijze"),
    wiki("Pulmonaria_officinalis_kz02.jpg", "Gevlekt longkruid — habitus", type_="habitus"),
    wiki("Pulmonaria_officinalis_Sturm18.jpg", "Gevlekt longkruid — blad", type_="blad"),
]},

# ══════════════════════════════════════════════════════════════════════════════
# HEESTERS
# ══════════════════════════════════════════════════════════════════════════════

"Buddleja davidii": {"photos": [
    wiki("Buddleja_davidii_kz01.jpg", "Vlinderstruik in bloei", type_="bloeiwijze"),
    wiki("Buddleja_davidii_kz02.jpg", "Vlinderstruik — habitus", type_="habitus"),
    wiki("Buddleja_davidii_1.jpg", "Vlinderstruik — blad", type_="blad"),
]},

"Corylus avellana": {"photos": [
    wiki("Corylus_avellana_kz01.jpg", "Hazelaar — katjes in bloei", type_="bloeiwijze"),
    wiki("Corylus_avellana_kz02.jpg", "Hazelaar — habitus", type_="habitus"),
    wiki("Corylus_avellana_nuts.jpg", "Hazelaar — hazelnoten", type_="vrucht"),
]},

"Prunus spinosa": {"photos": [
    wiki("Prunus_spinosa_kz01.jpg", "Sleedoorn in bloei", type_="bloeiwijze"),
    wiki("Prunus_spinosa_kz02.jpg", "Sleedoorn — habitus", type_="habitus"),
    wiki("Prunus_spinosa_berries.jpg", "Sleedoorn — sleedoornbes", type_="vrucht"),
]},

"Amelanchier lamarckii": {"photos": [
    wiki("Amelanchier_lamarckii_kz01.jpg", "Krentenboom in bloei", type_="bloeiwijze"),
    wiki("Amelanchier_lamarckii_kz02.jpg", "Krentenboom — habitus", type_="habitus"),
    wiki("Amelanchier_lamarckii_fruits.jpg", "Krentenboom — vruchten", type_="vrucht"),
]},

"Viburnum opulus": {"photos": [
    wiki("Viburnum_opulus_kz01.jpg", "Gelderse roos in bloei", type_="bloeiwijze"),
    wiki("Viburnum_opulus_kz02.jpg", "Gelderse roos — habitus", type_="habitus"),
    wiki("Viburnum_opulus_berries.jpg", "Gelderse roos — rode bessen", type_="vrucht"),
]},

"Hydrangea macrophylla": {"photos": [
    wiki("Hydrangea_macrophylla_kz01.jpg", "Hortensia in bloei", type_="bloeiwijze"),
    wiki("Hydrangea_macrophylla_kz02.jpg", "Hortensia — habitus", type_="habitus"),
    wiki("Hydrangea_macrophylla_1.jpg", "Hortensia — blad", type_="blad"),
]},

"Forsythia x intermedia": {"photos": [
    wiki("Forsythia_x_intermedia_kz01.jpg", "Forsythia in bloei", type_="bloeiwijze"),
    wiki("Forsythia_x_intermedia_kz02.jpg", "Forsythia — habitus", type_="habitus"),
    wiki("Forsythia_x_intermedia_1.jpg", "Forsythia — blad", type_="blad"),
]},

"Cornus alba": {"photos": [
    wiki("Cornus_alba_kz01.jpg", "Witte kornoelje in bloei", type_="bloeiwijze"),
    wiki("Cornus_alba_kz02.jpg", "Witte kornoelje — rode winterstelen", type_="habitus"),
    wiki("Cornus_alba_berries.jpg", "Witte kornoelje — bessen", type_="vrucht"),
]},

"Spiraea nipponica": {"photos": [
    wiki("Spiraea_nipponica_kz01.jpg", "Japanse spirea in bloei", type_="bloeiwijze"),
    wiki("Spiraea_nipponica_kz02.jpg", "Japanse spirea — habitus", type_="habitus"),
    wiki("Spiraea_nipponica_1.jpg", "Japanse spirea — blad", type_="blad"),
]},

"Magnolia x soulangeana": {"photos": [
    wiki("Magnolia_x_soulangeana_kz01.jpg", "Beverboom in bloei", type_="bloeiwijze"),
    wiki("Magnolia_x_soulangeana_kz02.jpg", "Beverboom — habitus", type_="habitus"),
    wiki("Magnolia_x_soulangeana_1.jpg", "Beverboom — blad", type_="blad"),
]},

"Lavandula angustifolia": {"photos": [
    wiki("Lavandula_angustifolia_kz01.jpg", "Lavendel in bloei", type_="bloeiwijze"),
    wiki("Lavandula_angustifolia_kz02.jpg", "Lavendel — habitus", type_="habitus"),
    wiki("Lavandula_angustifolia_1.jpg", "Lavendel — blad", type_="blad"),
]},

"Hedera helix": {"photos": [
    wiki("Hedera_helix_kz01.jpg", "Klimop — blad", type_="blad"),
    wiki("Hedera_helix_kz02.jpg", "Klimop — habitus", type_="habitus"),
    wiki("Hedera_helix_berries.jpg", "Klimop — bessen", type_="vrucht"),
]},

"Mahonia aquifolium": {"photos": [
    wiki("Mahonia_aquifolium_kz01.jpg", "Mahonie in bloei", type_="bloeiwijze"),
    wiki("Mahonia_aquifolium_kz02.jpg", "Mahonie — habitus", type_="habitus"),
    wiki("Mahonia_aquifolium_berries.jpg", "Mahonie — blauwe bessen", type_="vrucht"),
]},

"Ilex aquifolium": {"photos": [
    wiki("Ilex_aquifolium_kz01.jpg", "Hulst — habitus", type_="habitus"),
    wiki("Ilex_aquifolium_kz02.jpg", "Hulst — rode bessen", type_="vrucht"),
    wiki("Ilex_aquifolium_Sturm18.jpg", "Hulst — stekelig blad", type_="blad"),
]},

"Calluna vulgaris": {"photos": [
    wiki("Calluna_vulgaris_kz01.jpg", "Struikheide in bloei", type_="bloeiwijze"),
    wiki("Calluna_vulgaris_kz02.jpg", "Struikheide — habitus", type_="habitus"),
    wiki("Calluna_vulgaris_Sturm18.jpg", "Struikheide — blad", type_="blad"),
]},

"Rhododendron ponticum": {"photos": [
    wiki("Rhododendron_ponticum_kz01.jpg", "Rododendron in bloei", type_="bloeiwijze"),
    wiki("Rhododendron_ponticum_kz02.jpg", "Rododendron — habitus", type_="habitus"),
    wiki("Rhododendron_ponticum_1.jpg", "Rododendron — blad", type_="blad"),
]},

"Buxus sempervirens": {"photos": [
    wiki("Buxus_sempervirens_kz01.jpg", "Buxus — habitus", type_="habitus"),
    wiki("Buxus_sempervirens_kz02.jpg", "Buxus — blad", type_="blad"),
    wiki("Buxus_sempervirens_1.jpg", "Buxus — bloemen", type_="bloeiwijze"),
]},

"Erica carnea": {"photos": [
    wiki("Erica_carnea_kz01.jpg", "Winterheide in bloei", type_="bloeiwijze"),
    wiki("Erica_carnea_kz02.jpg", "Winterheide — habitus", type_="habitus"),
    wiki("Erica_carnea_1.jpg", "Winterheide — blad", type_="blad"),
]},

"Vaccinium myrtillus": {"photos": [
    wiki("Vaccinium_myrtillus_kz01.jpg", "Blauwe bosbes in bloei", type_="bloeiwijze"),
    wiki("Vaccinium_myrtillus_kz02.jpg", "Blauwe bosbes — habitus", type_="habitus"),
    wiki("Vaccinium_myrtillus_fruits.jpg", "Blauwe bosbes — bessen", type_="vrucht"),
]},

"Berberis vulgaris": {"photos": [
    wiki("Berberis_vulgaris_kz01.jpg", "Gewone zuurbes in bloei", type_="bloeiwijze"),
    wiki("Berberis_vulgaris_kz02.jpg", "Gewone zuurbes — habitus", type_="habitus"),
    wiki("Berberis_vulgaris_berries.jpg", "Gewone zuurbes — bessen", type_="vrucht"),
]},

"Salix aurita": {"photos": [
    wiki("Salix_aurita_kz01.jpg", "Geoorde wilg — katjes", type_="bloeiwijze"),
    wiki("Salix_aurita_kz02.jpg", "Geoorde wilg — habitus", type_="habitus"),
    wiki("Salix_aurita_Sturm18.jpg", "Geoorde wilg — blad", type_="blad"),
]},

"Rhamnus cathartica": {"photos": [
    wiki("Rhamnus_cathartica_kz01.jpg", "Wegedoorn — habitus", type_="habitus"),
    wiki("Rhamnus_cathartica_kz02.jpg", "Wegedoorn — bessen", type_="vrucht"),
    wiki("Rhamnus_cathartica_Sturm18.jpg", "Wegedoorn — blad", type_="blad"),
]},

"Berberis thunbergii": {"photos": [
    wiki("Berberis_thunbergii_kz01.jpg", "Japanse zuurbes in bloei", type_="bloeiwijze"),
    wiki("Berberis_thunbergii_kz02.jpg", "Japanse zuurbes — habitus", type_="habitus"),
    wiki("Berberis_thunbergii_berries.jpg", "Japanse zuurbes — bessen", type_="vrucht"),
]},

"Ribes sanguineum": {"photos": [
    wiki("Ribes_sanguineum_kz01.jpg", "Bloeikruidbes in bloei", type_="bloeiwijze"),
    wiki("Ribes_sanguineum_kz02.jpg", "Bloeikruidbes — habitus", type_="habitus"),
    wiki("Ribes_sanguineum_1.jpg", "Bloeikruidbes — blad", type_="blad"),
]},

"Weigela": {"photos": [
    wiki("Weigela_florida_kz01.jpg", "Weigelia in bloei", type_="bloeiwijze"),
    wiki("Weigela_florida_kz02.jpg", "Weigelia — habitus", type_="habitus"),
    wiki("Weigela_florida_1.jpg", "Weigelia — blad", type_="blad"),
]},

"Acer campestre": {"photos": [
    wiki("Acer_campestre_kz01.jpg", "Veldesdoorn — habitus", type_="habitus"),
    wiki("Acer_campestre_kz02.jpg", "Veldesdoorn — blad", type_="blad"),
    wiki("Acer_campestre_samaras.jpg", "Veldesdoorn — gevleugelde zaden", type_="vrucht"),
]},

"Cotinus coggygria": {"photos": [
    wiki("Cotinus_coggygria_kz01.jpg", "Pruikenboom in bloei", type_="bloeiwijze"),
    wiki("Cotinus_coggygria_kz02.jpg", "Pruikenboom — habitus", type_="habitus"),
    wiki("Cotinus_coggygria_1.jpg", "Pruikenboom — blad", type_="blad"),
]},

"Hypericum 'Hidcote'": {"photos": [
    wiki("Hypericum_hidcote_kz01.jpg", "Hidcote sint-janskruid in bloei", type_="bloeiwijze"),
    wiki("Hypericum_hidcote_kz02.jpg", "Hidcote sint-janskruid — habitus", type_="habitus"),
    wiki("Hypericum_calycinum_kz01.jpg", "Sint-janskruid — blad", type_="blad"),
]},

"Leycesteria formosa": {"photos": [
    wiki("Leycesteria_formosa_kz01.jpg", "Fazantenboom in bloei", type_="bloeiwijze"),
    wiki("Leycesteria_formosa_kz02.jpg", "Fazantenboom — habitus", type_="habitus"),
    wiki("Leycesteria_formosa_fruits.jpg", "Fazantenboom — bessen", type_="vrucht"),
]},

"Deutzia gracilis": {"photos": [
    wiki("Deutzia_gracilis_kz01.jpg", "Bruidsbloem in bloei", type_="bloeiwijze"),
    wiki("Deutzia_gracilis_kz02.jpg", "Bruidsbloem — habitus", type_="habitus"),
    wiki("Deutzia_gracilis_1.jpg", "Bruidsbloem — blad", type_="blad"),
]},

"Ligustrum vulgare": {"photos": [
    wiki("Ligustrum_vulgare_kz01.jpg", "Gewone liguster in bloei", type_="bloeiwijze"),
    wiki("Ligustrum_vulgare_kz02.jpg", "Gewone liguster — habitus", type_="habitus"),
    wiki("Ligustrum_vulgare_berries.jpg", "Gewone liguster — bessen", type_="vrucht"),
]},

"Lonicera nitida": {"photos": [
    wiki("Lonicera_nitida_kz01.jpg", "Doos-kamperfoelie — habitus", type_="habitus"),
    wiki("Lonicera_nitida_kz02.jpg", "Doos-kamperfoelie — blad", type_="blad"),
    wiki("Lonicera_nitida_1.jpg", "Doos-kamperfoelie — bessen", type_="vrucht"),
]},

"Skimmia japonica": {"photos": [
    wiki("Skimmia_japonica_kz01.jpg", "Skimmia in bloei", type_="bloeiwijze"),
    wiki("Skimmia_japonica_kz02.jpg", "Skimmia — habitus", type_="habitus"),
    wiki("Skimmia_japonica_berries.jpg", "Skimmia — rode bessen", type_="vrucht"),
]},

"Aucuba japonica": {"photos": [
    wiki("Aucuba_japonica_kz01.jpg", "Japanse laurier — habitus", type_="habitus"),
    wiki("Aucuba_japonica_kz02.jpg", "Japanse laurier — blad", type_="blad"),
    wiki("Aucuba_japonica_berries.jpg", "Japanse laurier — bessen", type_="vrucht"),
]},

"Eucalyptus gunnii": {"photos": [
    wiki("Eucalyptus_gunnii_kz01.jpg", "Gomboom — habitus", type_="habitus"),
    wiki("Eucalyptus_gunnii_kz02.jpg", "Gomboom — jonge ronde blaadjes", type_="blad"),
    wiki("Eucalyptus_gunnii_1.jpg", "Gomboom — oudere bladeren", type_="blad"),
]},

"Cotoneaster suecicus": {"photos": [
    wiki("Cotoneaster_suecicus_kz01.jpg", "Zweedse dwergmispel — habitus", type_="habitus"),
    wiki("Cotoneaster_dammeri_kz01.jpg", "Cotoneaster — blad", type_="blad"),
    wiki("Cotoneaster_suecicus_berries.jpg", "Zweedse dwergmispel — bessen", type_="vrucht"),
]},

"Berberis julianae": {"photos": [
    wiki("Berberis_julianae_kz01.jpg", "Juliana-zuurbes — habitus", type_="habitus"),
    wiki("Berberis_julianae_kz02.jpg", "Juliana-zuurbes — blad", type_="blad"),
    wiki("Berberis_julianae_berries.jpg", "Juliana-zuurbes — bessen", type_="vrucht"),
]},

"Kerria japonica": {"photos": [
    wiki("Kerria_japonica_kz01.jpg", "Japanse kerria in bloei", type_="bloeiwijze"),
    wiki("Kerria_japonica_kz02.jpg", "Japanse kerria — habitus", type_="habitus"),
    wiki("Kerria_japonica_1.jpg", "Japanse kerria — blad", type_="blad"),
]},

"Diervilla sessilifolia": {"photos": [
    wiki("Diervilla_sessilifolia_kz01.jpg", "Zittende diervilla in bloei", type_="bloeiwijze"),
    wiki("Diervilla_sessilifolia_kz02.jpg", "Zittende diervilla — habitus", type_="habitus"),
    wiki("Diervilla_sessilifolia_1.jpg", "Zittende diervilla — blad", type_="blad"),
]},

"Magnolia stellata": {"photos": [
    wiki("Magnolia_stellata_kz01.jpg", "Sterrenmagnolia in bloei", type_="bloeiwijze"),
    wiki("Magnolia_stellata_kz02.jpg", "Sterrenmagnolia — habitus", type_="habitus"),
    wiki("Magnolia_stellata_1.jpg", "Sterrenmagnolia — blad", type_="blad"),
]},

"Symphoricarpos chenaultii": {"photos": [
    wiki("Symphoricarpos_chenaultii_kz01.jpg", "Sneeuwbes — habitus", type_="habitus"),
    wiki("Symphoricarpos_chenaultii_berries.jpg", "Sneeuwbes — witte bessen", type_="vrucht"),
    wiki("Symphoricarpos_albus_kz01.jpg", "Sneeuwbes in bloei", type_="bloeiwijze"),
]},

"Cornus sericea": {"photos": [
    wiki("Cornus_sericea_kz01.jpg", "Amerikaanse kornoelje — rode stelen", type_="habitus"),
    wiki("Cornus_sericea_kz02.jpg", "Amerikaanse kornoelje — blad", type_="blad"),
    wiki("Cornus_sericea_berries.jpg", "Amerikaanse kornoelje — bessen", type_="vrucht"),
]},

"Salix babylonica": {"photos": [
    wiki("Salix_babylonica_kz01.jpg", "Treurwilg — habitus", type_="habitus"),
    wiki("Salix_babylonica_kz02.jpg", "Treurwilg — hangende takken", type_="habitus"),
    wiki("Salix_babylonica_1.jpg", "Treurwilg — blad", type_="blad"),
]},

"Citrus trifoliata": {"photos": [
    wiki("Poncirus_trifoliata_kz01.jpg", "Drieblad-citroen in bloei", type_="bloeiwijze"),
    wiki("Poncirus_trifoliata_kz02.jpg", "Drieblad-citroen — habitus", type_="habitus"),
    wiki("Poncirus_trifoliata_fruits.jpg", "Drieblad-citroen — vruchten", type_="vrucht"),
]},

# ══════════════════════════════════════════════════════════════════════════════
# BOMEN
# ══════════════════════════════════════════════════════════════════════════════

"Quercus robur": {"photos": [
    wiki("Quercus_robur_kz01.jpg", "Zomereik — habitus", type_="habitus"),
    wiki("Quercus_robur_kz02.jpg", "Zomereik — blad en eikels", type_="blad"),
    wiki("Quercus_robur_acorns.jpg", "Zomereik — eikels", type_="vrucht"),
]},

"Tilia x europaea": {"photos": [
    wiki("Tilia_x_europaea_kz01.jpg", "Hollandse linde — habitus", type_="habitus"),
    wiki("Tilia_x_europaea_kz02.jpg", "Hollandse linde — bloemen", type_="bloeiwijze"),
    wiki("Tilia_x_europaea_1.jpg", "Hollandse linde — blad", type_="blad"),
]},

"Betula pubescens": {"photos": [
    wiki("Betula_pubescens_kz01.jpg", "Zachte berk — habitus", type_="habitus"),
    wiki("Betula_pubescens_kz02.jpg", "Zachte berk — katjes", type_="bloeiwijze"),
    wiki("Betula_pubescens_Sturm18.jpg", "Zachte berk — blad", type_="blad"),
]},

"Betula pendula": {"photos": [
    wiki("Betula_pendula_kz01.jpg", "Ruwe berk — habitus", type_="habitus"),
    wiki("Betula_pendula_kz02.jpg", "Ruwe berk — katjes", type_="bloeiwijze"),
    wiki("Betula_pendula_Sturm18.jpg", "Ruwe berk — blad", type_="blad"),
]},

"Sorbus aucuparia": {"photos": [
    wiki("Sorbus_aucuparia_kz01.jpg", "Lijsterbes in bloei", type_="bloeiwijze"),
    wiki("Sorbus_aucuparia_kz02.jpg", "Lijsterbes — habitus", type_="habitus"),
    wiki("Sorbus_aucuparia_berries.jpg", "Lijsterbes — rode bessen", type_="vrucht"),
]},

"Fagus sylvatica": {"photos": [
    wiki("Fagus_sylvatica_kz01.jpg", "Beuk — habitus", type_="habitus"),
    wiki("Fagus_sylvatica_kz02.jpg", "Beuk — blad herfst", type_="blad"),
    wiki("Fagus_sylvatica_beechnuts.jpg", "Beuk — beukennootjes", type_="vrucht"),
]},

"Crataegus laevigata": {"photos": [
    wiki("Crataegus_laevigata_kz01.jpg", "Tweestijlige meidoorn in bloei", type_="bloeiwijze"),
    wiki("Crataegus_laevigata_kz02.jpg", "Tweestijlige meidoorn — habitus", type_="habitus"),
    wiki("Crataegus_laevigata_berries.jpg", "Tweestijlige meidoorn — vruchten", type_="vrucht"),
]},

"Crataegus monogyna": {"photos": [
    wiki("Crataegus_monogyna_kz01.jpg", "Eenstijlige meidoorn in bloei", type_="bloeiwijze"),
    wiki("Crataegus_monogyna_kz02.jpg", "Eenstijlige meidoorn — habitus", type_="habitus"),
    wiki("Crataegus_monogyna_berries.jpg", "Eenstijlige meidoorn — meidoornbessen", type_="vrucht"),
]},

"Alnus glutinosa": {"photos": [
    wiki("Alnus_glutinosa_kz01.jpg", "Zwarte els — katjes", type_="bloeiwijze"),
    wiki("Alnus_glutinosa_kz02.jpg", "Zwarte els — habitus", type_="habitus"),
    wiki("Alnus_glutinosa_Sturm18.jpg", "Zwarte els — blad en kegeltjes", type_="vrucht"),
]},

"Robinia pseudoacacia": {"photos": [
    wiki("Robinia_pseudoacacia_kz01.jpg", "Acacia in bloei", type_="bloeiwijze"),
    wiki("Robinia_pseudoacacia_kz02.jpg", "Acacia — habitus", type_="habitus"),
    wiki("Robinia_pseudoacacia_1.jpg", "Acacia — blad", type_="blad"),
]},

"Taxus baccata": {"photos": [
    wiki("Taxus_baccata_kz01.jpg", "Taxus — habitus", type_="habitus"),
    wiki("Taxus_baccata_berries.jpg", "Taxus — rode vruchten (giftig)", type_="vrucht"),
    wiki("Taxus_baccata_kz02.jpg", "Taxus — blad", type_="blad"),
]},

"Pinus sylvestris": {"photos": [
    wiki("Pinus_sylvestris_kz01.jpg", "Grove den — habitus", type_="habitus"),
    wiki("Pinus_sylvestris_kz02.jpg", "Grove den — dennenappels", type_="vrucht"),
    wiki("Pinus_sylvestris_Sturm18.jpg", "Grove den — naaldenpaar", type_="blad"),
]},

"Ginkgo biloba": {"photos": [
    wiki("Ginkgo_biloba_kz01.jpg", "Ginkgo — habitus", type_="habitus"),
    wiki("Ginkgo_biloba_kz02.jpg", "Ginkgo — waaierblad", type_="blad"),
    wiki("Ginkgo_biloba_fruits.jpg", "Ginkgo — vruchten herfst", type_="vrucht"),
]},

"Acer platanoides": {"photos": [
    wiki("Acer_platanoides_kz01.jpg", "Noorse esdoorn — habitus", type_="habitus"),
    wiki("Acer_platanoides_kz02.jpg", "Noorse esdoorn — bloemen", type_="bloeiwijze"),
    wiki("Acer_platanoides_Sturm18.jpg", "Noorse esdoorn — blad", type_="blad"),
]},

"Carpinus betulus": {"photos": [
    wiki("Carpinus_betulus_kz01.jpg", "Haagbeuk — habitus", type_="habitus"),
    wiki("Carpinus_betulus_kz02.jpg", "Haagbeuk — vruchten", type_="vrucht"),
    wiki("Carpinus_betulus_Sturm18.jpg", "Haagbeuk — blad", type_="blad"),
]},

"Acer pseudoplatanus": {"photos": [
    wiki("Acer_pseudoplatanus_kz01.jpg", "Gewone esdoorn — habitus", type_="habitus"),
    wiki("Acer_pseudoplatanus_kz02.jpg", "Gewone esdoorn — bloemen", type_="bloeiwijze"),
    wiki("Acer_pseudoplatanus_Sturm18.jpg", "Gewone esdoorn — blad", type_="blad"),
]},

"Aesculus hippocastanum": {"photos": [
    wiki("Aesculus_hippocastanum_kz01.jpg", "Gewone paardenkastanje in bloei", type_="bloeiwijze"),
    wiki("Aesculus_hippocastanum_kz02.jpg", "Gewone paardenkastanje — habitus", type_="habitus"),
    wiki("Aesculus_hippocastanum_chestnuts.jpg", "Gewone paardenkastanje — kastanjes", type_="vrucht"),
]},

"Fraxinus excelsior": {"photos": [
    wiki("Fraxinus_excelsior_kz01.jpg", "Gewone es — habitus", type_="habitus"),
    wiki("Fraxinus_excelsior_kz02.jpg", "Gewone es — sleutels", type_="vrucht"),
    wiki("Fraxinus_excelsior_Sturm18.jpg", "Gewone es — blad", type_="blad"),
]},

"Laburnum x watereri": {"photos": [
    wiki("Laburnum_x_watereri_kz01.jpg", "Gouden regen in bloei", type_="bloeiwijze"),
    wiki("Laburnum_x_watereri_kz02.jpg", "Gouden regen — habitus", type_="habitus"),
    wiki("Laburnum_x_watereri_1.jpg", "Gouden regen — blad", type_="blad"),
]},

"Platanus x hispanica": {"photos": [
    wiki("Platanus_x_hispanica_kz01.jpg", "Gewone plataan — habitus", type_="habitus"),
    wiki("Platanus_x_hispanica_kz02.jpg", "Gewone plataan — bolronde vruchten", type_="vrucht"),
    wiki("Platanus_x_hispanica_1.jpg", "Gewone plataan — blad", type_="blad"),
]},

"Populus alba": {"photos": [
    wiki("Populus_alba_kz01.jpg", "Witte abeel — habitus", type_="habitus"),
    wiki("Populus_alba_kz02.jpg", "Witte abeel — blad onderzijde", type_="blad"),
    wiki("Populus_alba_Sturm18.jpg", "Witte abeel — katjes", type_="bloeiwijze"),
]},

"Populus tremula": {"photos": [
    wiki("Populus_tremula_kz01.jpg", "Ratelpopulier — habitus", type_="habitus"),
    wiki("Populus_tremula_kz02.jpg", "Ratelpopulier — katjes", type_="bloeiwijze"),
    wiki("Populus_tremula_Sturm18.jpg", "Ratelpopulier — blad", type_="blad"),
]},

"Prunus cerasifera": {"photos": [
    wiki("Prunus_cerasifera_kz01.jpg", "Kerspruim in bloei", type_="bloeiwijze"),
    wiki("Prunus_cerasifera_kz02.jpg", "Kerspruim — habitus paarsblad", type_="habitus"),
    wiki("Prunus_cerasifera_fruits.jpg", "Kerspruim — vruchten", type_="vrucht"),
]},

"Prunus padus": {"photos": [
    wiki("Prunus_padus_kz01.jpg", "Vogelkers in bloei", type_="bloeiwijze"),
    wiki("Prunus_padus_kz02.jpg", "Vogelkers — habitus", type_="habitus"),
    wiki("Prunus_padus_berries.jpg", "Vogelkers — bessen", type_="vrucht"),
]},

"Salix x sepulcralis": {"photos": [
    wiki("Salix_x_sepulcralis_kz01.jpg", "Treurwilg — habitus", type_="habitus"),
    wiki("Salix_x_sepulcralis_kz02.jpg", "Treurwilg — hangende takken", type_="habitus"),
    wiki("Salix_x_sepulcralis_1.jpg", "Treurwilg — blad", type_="blad"),
]},

"Abies koreana": {"photos": [
    wiki("Abies_koreana_kz01.jpg", "Koreaanse spar — habitus", type_="habitus"),
    wiki("Abies_koreana_kz02.jpg", "Koreaanse spar — blauwe kegels", type_="vrucht"),
    wiki("Abies_koreana_1.jpg", "Koreaanse spar — naaldonderijde", type_="blad"),
]},

"Cedrus atlantica": {"photos": [
    wiki("Cedrus_atlantica_kz01.jpg", "Atlasceder — habitus", type_="habitus"),
    wiki("Cedrus_atlantica_kz02.jpg", "Atlasceder — kegels", type_="vrucht"),
    wiki("Cedrus_atlantica_1.jpg", "Atlasceder — naaldenbos", type_="blad"),
]},

"Chamaecyparis lawsoniana": {"photos": [
    wiki("Chamaecyparis_lawsoniana_kz01.jpg", "Lawsoncipres — habitus", type_="habitus"),
    wiki("Chamaecyparis_lawsoniana_kz02.jpg", "Lawsoncipres — blad", type_="blad"),
    wiki("Chamaecyparis_lawsoniana_cones.jpg", "Lawsoncipres — kegels", type_="vrucht"),
]},

"Picea abies": {"photos": [
    wiki("Picea_abies_kz01.jpg", "Fijnspar — habitus", type_="habitus"),
    wiki("Picea_abies_kz02.jpg", "Fijnspar — kegels", type_="vrucht"),
    wiki("Picea_abies_Sturm18.jpg", "Fijnspar — naald", type_="blad"),
]},

"Pinus mugo mughus": {"photos": [
    wiki("Pinus_mugo_kz01.jpg", "Bergden — habitus", type_="habitus"),
    wiki("Pinus_mugo_kz02.jpg", "Bergden — kegels", type_="vrucht"),
    wiki("Pinus_mugo_Sturm18.jpg", "Bergden — naaldenpaar", type_="blad"),
]},

"Thuja occidentalis": {"photos": [
    wiki("Thuja_occidentalis_kz01.jpg", "Westerse levensboom — habitus", type_="habitus"),
    wiki("Thuja_occidentalis_kz02.jpg", "Westerse levensboom — blad", type_="blad"),
    wiki("Thuja_occidentalis_cones.jpg", "Westerse levensboom — kegels", type_="vrucht"),
]},

"Tsuga canadensis": {"photos": [
    wiki("Tsuga_canadensis_kz01.jpg", "Canadese hemlock — habitus", type_="habitus"),
    wiki("Tsuga_canadensis_kz02.jpg", "Canadese hemlock — kleine kegels", type_="vrucht"),
    wiki("Tsuga_canadensis_1.jpg", "Canadese hemlock — naaldjes", type_="blad"),
]},

# ══════════════════════════════════════════════════════════════════════════════
# BOLLEN & KNOLLEN
# ══════════════════════════════════════════════════════════════════════════════

"Allium aflatunense": {"photos": [
    wiki("Allium_aflatunense_kz01.jpg", "Sierui in bloei", type_="bloeiwijze"),
    wiki("Allium_aflatunense_kz02.jpg", "Sierui — habitus", type_="habitus"),
    wiki("Allium_aflatunense_1.jpg", "Sierui — blad", type_="blad"),
]},

"Galanthus nivalis": {"photos": [
    wiki("Galanthus_nivalis_kz01.jpg", "Sneeuwklokje in bloei", type_="bloeiwijze"),
    wiki("Galanthus_nivalis_kz02.jpg", "Sneeuwklokje — habitus", type_="habitus"),
    wiki("Galanthus_nivalis_Sturm18.jpg", "Sneeuwklokje — blad", type_="blad"),
]},

"Narcissus": {"photos": [
    wiki("Narcissus_pseudonarcissus_kz01.jpg", "Narcis in bloei", type_="bloeiwijze"),
    wiki("Narcissus_pseudonarcissus_kz02.jpg", "Narcis — habitus", type_="habitus"),
    wiki("Narcissus_pseudonarcissus_1.jpg", "Narcis — blad", type_="blad"),
]},

"Tulipa hybriden": {"photos": [
    wiki("Tulipa_gesneriana_kz01.jpg", "Tulp in bloei", type_="bloeiwijze"),
    wiki("Tulipa_gesneriana_kz02.jpg", "Tulp — habitus", type_="habitus"),
    wiki("Tulipa_gesneriana_1.jpg", "Tulp — blad", type_="blad"),
]},

"Dahlia hybriden": {"photos": [
    wiki("Dahlia_cultivar_kz01.jpg", "Dahlia in bloei", type_="bloeiwijze"),
    wiki("Dahlia_cultivar_kz02.jpg", "Dahlia — habitus", type_="habitus"),
    wiki("Dahlia_pinnata_kz01.jpg", "Dahlia — blad", type_="blad"),
]},

"Crocus chrysanthus": {"photos": [
    wiki("Crocus_chrysanthus_kz01.jpg", "Goudkrokus in bloei", type_="bloeiwijze"),
    wiki("Crocus_chrysanthus_kz02.jpg", "Goudkrokus — habitus", type_="habitus"),
    wiki("Crocus_chrysanthus_1.jpg", "Goudkrokus — blad", type_="blad"),
]},

"Muscari armeniacum": {"photos": [
    wiki("Muscari_armeniacum_kz01.jpg", "Blauwe druifjes in bloei", type_="bloeiwijze"),
    wiki("Muscari_armeniacum_kz02.jpg", "Blauwe druifjes — habitus", type_="habitus"),
    wiki("Muscari_armeniacum_1.jpg", "Blauwe druifjes — blad", type_="blad"),
]},

"Allium giganteum": {"photos": [
    wiki("Allium_giganteum_kz01.jpg", "Reuzensierui in bloei", type_="bloeiwijze"),
    wiki("Allium_giganteum_kz02.jpg", "Reuzensierui — habitus", type_="habitus"),
    wiki("Allium_giganteum_1.jpg", "Reuzensierui — blad", type_="blad"),
]},

"Hyacinthus orientalis": {"photos": [
    wiki("Hyacinthus_orientalis_kz01.jpg", "Hyacint in bloei", type_="bloeiwijze"),
    wiki("Hyacinthus_orientalis_kz02.jpg", "Hyacint — habitus", type_="habitus"),
    wiki("Hyacinthus_orientalis_1.jpg", "Hyacint — blad", type_="blad"),
]},

"Fritillaria meleagris": {"photos": [
    wiki("Fritillaria_meleagris_kz01.jpg", "Kievitsbloem in bloei", type_="bloeiwijze"),
    wiki("Fritillaria_meleagris_kz02.jpg", "Kievitsbloem — habitus", type_="habitus"),
    wiki("Fritillaria_meleagris_Sturm18.jpg", "Kievitsbloem — blad", type_="blad"),
]},

"Anemone blanda": {"photos": [
    wiki("Anemone_blanda_kz01.jpg", "Balkan-anemoon in bloei", type_="bloeiwijze"),
    wiki("Anemone_blanda_kz02.jpg", "Balkan-anemoon — habitus", type_="habitus"),
    wiki("Anemone_blanda_1.jpg", "Balkan-anemoon — blad", type_="blad"),
]},

"Scilla siberica": {"photos": [
    wiki("Scilla_siberica_kz01.jpg", "Siberische sterhyacint in bloei", type_="bloeiwijze"),
    wiki("Scilla_siberica_kz02.jpg", "Siberische sterhyacint — habitus", type_="habitus"),
    wiki("Scilla_siberica_1.jpg", "Siberische sterhyacint — blad", type_="blad"),
]},

"Fritillaria imperialis": {"photos": [
    wiki("Fritillaria_imperialis_kz01.jpg", "Keizerskroon in bloei", type_="bloeiwijze"),
    wiki("Fritillaria_imperialis_kz02.jpg", "Keizerskroon — habitus", type_="habitus"),
    wiki("Fritillaria_imperialis_1.jpg", "Keizerskroon — blad", type_="blad"),
]},

"Anemone coronaria": {"photos": [
    wiki("Anemone_coronaria_kz01.jpg", "Kroones anemoon in bloei", type_="bloeiwijze"),
    wiki("Anemone_coronaria_kz02.jpg", "Kroones anemoon — habitus", type_="habitus"),
    wiki("Anemone_coronaria_1.jpg", "Kroones anemoon — blad", type_="blad"),
]},

# ══════════════════════════════════════════════════════════════════════════════
# EENJARIGEN & TWEEJARIGEN
# ══════════════════════════════════════════════════════════════════════════════

"Alcea rosea": {"photos": [
    wiki("Alcea_rosea_kz01.jpg", "Stokroos in bloei", type_="bloeiwijze"),
    wiki("Alcea_rosea_kz02.jpg", "Stokroos — habitus", type_="habitus"),
    wiki("Alcea_rosea_1.jpg", "Stokroos — blad", type_="blad"),
]},

"Calendula officinalis": {"photos": [
    wiki("Calendula_officinalis_kz01.jpg", "Goudsbloem in bloei", type_="bloeiwijze"),
    wiki("Calendula_officinalis_kz02.jpg", "Goudsbloem — habitus", type_="habitus"),
    wiki("Calendula_officinalis_Sturm18.jpg", "Goudsbloem — blad", type_="blad"),
]},

"Centaurea cyanus": {"photos": [
    wiki("Centaurea_cyanus_kz01.jpg", "Korenbloem in bloei", type_="bloeiwijze"),
    wiki("Centaurea_cyanus_kz02.jpg", "Korenbloem — habitus", type_="habitus"),
    wiki("Centaurea_cyanus_Sturm18.jpg", "Korenbloem — blad", type_="blad"),
]},

"Digitalis purpurea": {"photos": [
    wiki("Digitalis_purpurea_kz01.jpg", "Gewoon vingerhoedskruid in bloei", type_="bloeiwijze"),
    wiki("Digitalis_purpurea_kz02.jpg", "Vingerhoedskruid — habitus", type_="habitus"),
    wiki("Digitalis_purpurea_Sturm18.jpg", "Vingerhoedskruid — blad", type_="blad"),
]},

"Helianthus annuus": {"photos": [
    wiki("Helianthus_annuus_kz01.jpg", "Zonnebloem in bloei", type_="bloeiwijze"),
    wiki("Helianthus_annuus_kz02.jpg", "Zonnebloem — habitus", type_="habitus"),
    wiki("Helianthus_annuus_seeds.jpg", "Zonnebloem — zaadschijf", type_="vrucht"),
]},

"Tagetes": {"photos": [
    wiki("Tagetes_patula_kz01.jpg", "Afrikaantje in bloei", type_="bloeiwijze"),
    wiki("Tagetes_patula_kz02.jpg", "Afrikaantje — habitus", type_="habitus"),
    wiki("Tagetes_patula_1.jpg", "Afrikaantje — blad", type_="blad"),
]},

"Zinnia elegans": {"photos": [
    wiki("Zinnia_elegans_kz01.jpg", "Zinnia in bloei", type_="bloeiwijze"),
    wiki("Zinnia_elegans_kz02.jpg", "Zinnia — habitus", type_="habitus"),
    wiki("Zinnia_elegans_1.jpg", "Zinnia — blad", type_="blad"),
]},

"Cosmos bipinnatus": {"photos": [
    wiki("Cosmos_bipinnatus_kz01.jpg", "Cosmea in bloei", type_="bloeiwijze"),
    wiki("Cosmos_bipinnatus_kz02.jpg", "Cosmea — habitus", type_="habitus"),
    wiki("Cosmos_bipinnatus_1.jpg", "Cosmea — fijn blad", type_="blad"),
]},

"Hesperis matronalis": {"photos": [
    wiki("Hesperis_matronalis_kz01.jpg", "Damastbloem in bloei", type_="bloeiwijze"),
    wiki("Hesperis_matronalis_kz02.jpg", "Damastbloem — habitus", type_="habitus"),
    wiki("Hesperis_matronalis_Sturm18.jpg", "Damastbloem — blad", type_="blad"),
]},

"Begonia semperflorens": {"photos": [
    wiki("Begonia_semperflorens_kz01.jpg", "Ijs-begonia in bloei", type_="bloeiwijze"),
    wiki("Begonia_semperflorens_kz02.jpg", "Ijs-begonia — habitus", type_="habitus"),
    wiki("Begonia_semperflorens_1.jpg", "Ijs-begonia — blad", type_="blad"),
]},

"Impatiens walleriana": {"photos": [
    wiki("Impatiens_walleriana_kz01.jpg", "Vlijtig liesje in bloei", type_="bloeiwijze"),
    wiki("Impatiens_walleriana_kz02.jpg", "Vlijtig liesje — habitus", type_="habitus"),
    wiki("Impatiens_walleriana_1.jpg", "Vlijtig liesje — blad", type_="blad"),
]},

"Dianthus barbatus": {"photos": [
    wiki("Dianthus_barbatus_kz01.jpg", "Boernanjer in bloei", type_="bloeiwijze"),
    wiki("Dianthus_barbatus_kz02.jpg", "Boernanjer — habitus", type_="habitus"),
    wiki("Dianthus_barbatus_Sturm18.jpg", "Boernanjer — blad", type_="blad"),
]},

"Osteospermum cultivars": {"photos": [
    wiki("Osteospermum_ecklonis_kz01.jpg", "Kaapmargriet in bloei", type_="bloeiwijze"),
    wiki("Osteospermum_ecklonis_kz02.jpg", "Kaapmargriet — habitus", type_="habitus"),
    wiki("Osteospermum_ecklonis_1.jpg", "Kaapmargriet — blad", type_="blad"),
]},

# ══════════════════════════════════════════════════════════════════════════════
# GRASSEN
# ══════════════════════════════════════════════════════════════════════════════

"Calamagrostis x acutiflora": {"photos": [
    wiki("Calamagrostis_x_acutiflora_kz01.jpg", "Vedergras in bloei", type_="bloeiwijze"),
    wiki("Calamagrostis_x_acutiflora_kz02.jpg", "Vedergras — habitus", type_="habitus"),
    wiki("Calamagrostis_x_acutiflora_1.jpg", "Vedergras — blad", type_="blad"),
]},

"Festuca glauca": {"photos": [
    wiki("Festuca_glauca_kz01.jpg", "Blauwzwenkgras — habitus", type_="habitus"),
    wiki("Festuca_glauca_kz02.jpg", "Blauwzwenkgras — blauwe naaldbladen", type_="blad"),
    wiki("Festuca_glauca_1.jpg", "Blauwzwenkgras in bloei", type_="bloeiwijze"),
]},

"Pennisetum alopecuroides": {"photos": [
    wiki("Pennisetum_alopecuroides_kz01.jpg", "Borstelgras in bloei", type_="bloeiwijze"),
    wiki("Pennisetum_alopecuroides_kz02.jpg", "Borstelgras — habitus", type_="habitus"),
    wiki("Pennisetum_alopecuroides_1.jpg", "Borstelgras — blad", type_="blad"),
]},

"Carex buchananii": {"photos": [
    wiki("Carex_buchananii_kz01.jpg", "Neushoornzegge — habitus", type_="habitus"),
    wiki("Carex_buchananii_kz02.jpg", "Neushoornzegge — bruinrood blad", type_="blad"),
    wiki("Carex_buchananii_1.jpg", "Neushoornzegge — aartjes", type_="bloeiwijze"),
]},

"Cortaderia selloana": {"photos": [
    wiki("Cortaderia_selloana_kz01.jpg", "Pampasgras in bloei", type_="bloeiwijze"),
    wiki("Cortaderia_selloana_kz02.jpg", "Pampasgras — habitus", type_="habitus"),
    wiki("Cortaderia_selloana_1.jpg", "Pampasgras — blad", type_="blad"),
]},

"Molinia caerulea": {"photos": [
    wiki("Molinia_caerulea_kz01.jpg", "Pijpenstrootje in bloei", type_="bloeiwijze"),
    wiki("Molinia_caerulea_kz02.jpg", "Pijpenstrootje — habitus", type_="habitus"),
    wiki("Molinia_caerulea_Sturm18.jpg", "Pijpenstrootje — blad", type_="blad"),
]},

# ══════════════════════════════════════════════════════════════════════════════
# KEUKENKRUIDEN
# ══════════════════════════════════════════════════════════════════════════════

"Allium schoenoprasum": {"photos": [
    wiki("Allium_schoenoprasum_kz01.jpg", "Bieslook in bloei", type_="bloeiwijze"),
    wiki("Allium_schoenoprasum_kz02.jpg", "Bieslook — habitus", type_="habitus"),
    wiki("Allium_schoenoprasum_1.jpg", "Bieslook — holle stelen", type_="blad"),
]},

"Mentha x piperita": {"photos": [
    wiki("Mentha_x_piperita_kz01.jpg", "Pepermunt in bloei", type_="bloeiwijze"),
    wiki("Mentha_x_piperita_kz02.jpg", "Pepermunt — habitus", type_="habitus"),
    wiki("Mentha_x_piperita_1.jpg", "Pepermunt — blad", type_="blad"),
]},

"Petroselinum crispum": {"photos": [
    wiki("Petroselinum_crispum_kz01.jpg", "Kruldige peterselie — habitus", type_="habitus"),
    wiki("Petroselinum_crispum_kz02.jpg", "Peterselie in bloei", type_="bloeiwijze"),
    wiki("Petroselinum_crispum_Sturm18.jpg", "Peterselie — blad", type_="blad"),
]},

# ══════════════════════════════════════════════════════════════════════════════
# KLIMPLANTEN & ROZEN
# ══════════════════════════════════════════════════════════════════════════════

"Wisteria sinensis": {"photos": [
    wiki("Wisteria_sinensis_kz01.jpg", "Chinese blauweregen in bloei", type_="bloeiwijze"),
    wiki("Wisteria_sinensis_kz02.jpg", "Blauweregen — habitus", type_="habitus"),
    wiki("Wisteria_sinensis_1.jpg", "Blauweregen — blad", type_="blad"),
]},

"Lonicera periclymenum": {"photos": [
    wiki("Lonicera_periclymenum_kz01.jpg", "Wilde kamperfoelie in bloei", type_="bloeiwijze"),
    wiki("Lonicera_periclymenum_kz02.jpg", "Wilde kamperfoelie — habitus", type_="habitus"),
    wiki("Lonicera_periclymenum_berries.jpg", "Wilde kamperfoelie — rode bessen", type_="vrucht"),
]},

"Clematis jackmanii": {"photos": [
    wiki("Clematis_jackmanii_kz01.jpg", "Jackman-clematis in bloei", type_="bloeiwijze"),
    wiki("Clematis_jackmanii_kz02.jpg", "Jackman-clematis — habitus", type_="habitus"),
    wiki("Clematis_jackmanii_seedheads.jpg", "Jackman-clematis — verige zaadhoofden", type_="vrucht"),
]},

"Parthenocissus tricuspidata": {"photos": [
    wiki("Parthenocissus_tricuspidata_kz01.jpg", "Wilde wingerd — habitus", type_="habitus"),
    wiki("Parthenocissus_tricuspidata_kz02.jpg", "Wilde wingerd — herfstkleur", type_="blad"),
    wiki("Parthenocissus_tricuspidata_berries.jpg", "Wilde wingerd — bessen", type_="vrucht"),
]},

"Rosa rugosa": {"photos": [
    wiki("Rosa_rugosa_kz01.jpg", "Rimpelroos in bloei", type_="bloeiwijze"),
    wiki("Rosa_rugosa_kz02.jpg", "Rimpelroos — habitus", type_="habitus"),
    wiki("Rosa_rugosa_hips.jpg", "Rimpelroos — grote rode rozenbottels", type_="vrucht"),
]},

"Rosa glauca": {"photos": [
    wiki("Rosa_glauca_kz01.jpg", "Blauwe roos in bloei", type_="bloeiwijze"),
    wiki("Rosa_glauca_kz02.jpg", "Blauwe roos — habitus blauwgroen blad", type_="habitus"),
    wiki("Rosa_glauca_hips.jpg", "Blauwe roos — rozenbottels", type_="vrucht"),
]},

"Clematis vitalba": {"photos": [
    wiki("Clematis_vitalba_kz01.jpg", "Bosrank in bloei", type_="bloeiwijze"),
    wiki("Clematis_vitalba_kz02.jpg", "Bosrank — habitus", type_="habitus"),
    wiki("Clematis_vitalba_seedheads.jpg", "Bosrank — pluizige zaadhoofden", type_="vrucht"),
]},

"Rosa arvensis": {"photos": [
    wiki("Rosa_arvensis_kz01.jpg", "Akkerwild roos in bloei", type_="bloeiwijze"),
    wiki("Rosa_arvensis_kz02.jpg", "Akkerwild roos — habitus", type_="habitus"),
    wiki("Rosa_arvensis_hips.jpg", "Akkerwild roos — kleine rozenbottels", type_="vrucht"),
]},

"Clematis armandii": {"photos": [
    wiki("Clematis_armandii_kz01.jpg", "Armand-clematis in bloei", type_="bloeiwijze"),
    wiki("Clematis_armandii_kz02.jpg", "Armand-clematis — habitus", type_="habitus"),
    wiki("Clematis_armandii_1.jpg", "Armand-clematis — blad", type_="blad"),
]},

"Fallopia baldschuanica": {"photos": [
    wiki("Fallopia_baldschuanica_kz01.jpg", "Duizendknoop in bloei", type_="bloeiwijze"),
    wiki("Fallopia_baldschuanica_kz02.jpg", "Duizendknoop — habitus", type_="habitus"),
    wiki("Fallopia_baldschuanica_1.jpg", "Duizendknoop — blad", type_="blad"),
]},

"Hydrangea anomala petiolaris": {"photos": [
    wiki("Hydrangea_anomala_petiolaris_kz01.jpg", "Klim-hortensia in bloei", type_="bloeiwijze"),
    wiki("Hydrangea_anomala_petiolaris_kz02.jpg", "Klim-hortensia — habitus", type_="habitus"),
    wiki("Hydrangea_anomala_petiolaris_1.jpg", "Klim-hortensia — blad", type_="blad"),
]},

"Rosa nitida": {"photos": [
    wiki("Rosa_nitida_kz01.jpg", "Glansbladige roos in bloei", type_="bloeiwijze"),
    wiki("Rosa_nitida_kz02.jpg", "Glansbladige roos — habitus", type_="habitus"),
    wiki("Rosa_nitida_hips.jpg", "Glansbladige roos — rozenbottels", type_="vrucht"),
]},

"Rosa canina": {"photos": [
    wiki("Rosa_canina_kz01.jpg", "Hondsroos in bloei", type_="bloeiwijze"),
    wiki("Rosa_canina_kz02.jpg", "Hondsroos — habitus", type_="habitus"),
    wiki("Rosa_canina_hips.jpg", "Hondsroos — rode rozenbottels", type_="vrucht"),
]},

# ══════════════════════════════════════════════════════════════════════════════
# KUIPPLANTEN
# ══════════════════════════════════════════════════════════════════════════════

"Agapanthus hybriden": {"photos": [
    wiki("Agapanthus_africanus_kz01.jpg", "Afrikaanse lelie in bloei", type_="bloeiwijze"),
    wiki("Agapanthus_africanus_kz02.jpg", "Afrikaanse lelie — habitus", type_="habitus"),
    wiki("Agapanthus_africanus_1.jpg", "Afrikaanse lelie — blad", type_="blad"),
]},

"Laurus nobilis": {"photos": [
    wiki("Laurus_nobilis_kz01.jpg", "Laurier — habitus", type_="habitus"),
    wiki("Laurus_nobilis_kz02.jpg", "Laurier — blad", type_="blad"),
    wiki("Laurus_nobilis_berries.jpg", "Laurier — bessen", type_="vrucht"),
]},

"Olea europaea": {"photos": [
    wiki("Olea_europaea_kz01.jpg", "Olijfboom — habitus", type_="habitus"),
    wiki("Olea_europaea_kz02.jpg", "Olijfboom — blad en vruchten", type_="vrucht"),
    wiki("Olea_europaea_1.jpg", "Olijfboom — blad", type_="blad"),
]},

"Fuchsia hybriden": {"photos": [
    wiki("Fuchsia_hybrida_kz01.jpg", "Fuchsia in bloei", type_="bloeiwijze"),
    wiki("Fuchsia_hybrida_kz02.jpg", "Fuchsia — habitus", type_="habitus"),
    wiki("Fuchsia_hybrida_1.jpg", "Fuchsia — blad", type_="blad"),
]},

"Mandevilla": {"photos": [
    wiki("Mandevilla_sanderi_kz01.jpg", "Mandevilla in bloei", type_="bloeiwijze"),
    wiki("Mandevilla_sanderi_kz02.jpg", "Mandevilla — habitus", type_="habitus"),
    wiki("Mandevilla_sanderi_1.jpg", "Mandevilla — blad", type_="blad"),
]},

"Pelargonium zonale": {"photos": [
    wiki("Pelargonium_zonale_kz01.jpg", "Zonale geranium in bloei", type_="bloeiwijze"),
    wiki("Pelargonium_zonale_kz02.jpg", "Zonale geranium — habitus", type_="habitus"),
    wiki("Pelargonium_zonale_1.jpg", "Zonale geranium — blad", type_="blad"),
]},

"Cordyline australis": {"photos": [
    wiki("Cordyline_australis_kz01.jpg", "Cordyline — habitus", type_="habitus"),
    wiki("Cordyline_australis_kz02.jpg", "Cordyline — blad", type_="blad"),
    wiki("Cordyline_australis_flower.jpg", "Cordyline — bloemen", type_="bloeiwijze"),
]},

"Petunia surfinia cultivars": {"photos": [
    wiki("Petunia_x_hybrida_kz01.jpg", "Petunia in bloei", type_="bloeiwijze"),
    wiki("Petunia_x_hybrida_kz02.jpg", "Petunia — habitus", type_="habitus"),
    wiki("Petunia_x_hybrida_1.jpg", "Petunia — blad", type_="blad"),
]},

}

