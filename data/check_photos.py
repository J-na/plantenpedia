import urllib.request, urllib.parse, json, sys, time
sys.stdout.reconfigure(encoding='utf-8')

API = 'https://commons.wikimedia.org/w/api.php'

missing_list = [
    'Acaena_buchananii_kz1.jpg','Acanthus_mollis_Hdg_02.jpg','Aconitum_carmichaelii2.jpg',
    'Ajuga_reptans_200904.jpg','Alchemilla_mollis_003.jpg','Arabis_caucasica_-_flowers_(aka).jpg',
    'Armeria_maritima_Whitley_Bay.jpg','Aster_frikartii_Monch_3.jpg','Astrantia_major_001.jpg',
    'Aubrieta_deltoidea0.jpg','Aurinia_saxatilis_(Brassicaceae)_plant.jpg','Brunnera_macrophylla_plant.jpg',
    'Campanula_carpatica_003.jpg','Centaurea_montana0.jpg','Cerastium_tomentosum_plant.jpg',
    'Coreopsis_verticillata4.jpg','Dianthus_deltoides_flowers.jpg','Dicentra_spectabilis_Flore.jpg',
    'Doronicum_orientale_flower.jpg','Echinacea_purpurea1.jpg','Erysimum_cheiri1.jpg',
    'Euphorbia_epithymoides1.jpg','Foeniculum_vulgare_002.jpg','Galium_odoratum_eF.jpg',
    'Geranium_endressii_a1.jpg','Geranium_sanguineum_003.jpg','Gypsophila_paniculata_2.jpg',
    'Helianthemum_apenninum_1.jpg','Heuchera_micrantha_Palace_Purple.jpg','Hosta_tardiana_Halcyon.jpg',
    'Iberis_sempervirens2.jpg','Lamiastrum_galeobdolon_subsp._argentatum.jpg','Lamium_orvala_001.jpg',
    'Leucanthemum_x_superbum_Becky.jpg','Linaria_purpurea_002.jpg','Lupinus_Russell_hybrids.jpg',
    'Nepeta_x_faassenii_kz04.jpg','Pachysandra_terminalis_-_leaves_and_flowers.jpg',
    'Paeonia_lactiflora_Sarah_Bernhardt_1.jpg','Persicaria_affinis_4.jpg',
    'Pulmonaria_saccharata_Mrs_Moon.jpg','Pulsatilla_vulgaris_004.jpg',
    'Salvia_nemorosa_Caradonna_kz02.jpg','Sanguisorba_officinalis_kz.jpg',
    'Solidago_canadensis_Golden_Rod.jpg','Thymus_praecox_01.jpg','Verbena_bonariensis_1.jpg',
    'Vinca_major_Flower_2200px.jpg','Vinca_minor_15.jpg','Viola_x_wittrockiana_Blaue_Schonheit.jpg',
    'Alcea_rosea_flowers.jpg','Calendula_officinalis_001.jpg','Cornflower_Centaurea_cyanus_Purple_Gem.jpg',
    'Digitalis_purpurea_Koeh.jpg','Tagetes_erecta_flower_head.jpg','Zinnia_elegans_cv._Uproar_Rose.jpg',
    'Cosmos_bipinnatus_Radiance.jpg','Galanthus_nivalis-_snowdrop.jpg',
    'Tulipa_suaveolens_floriade_to_Wikimedia.jpg','Dahlia_x_hybrida_Nuit_d_ete.jpg',
    'Crocus_chrysanthus_Blue_Bird_02.jpg','Agapanthus_praecox_7.jpg','Laurus_nobilis-leaves.jpg',
    'Olea_europaea_kz01.jpg','Iris_pseudacorus_flowers.jpg','Lythrum_salicaria_kz05.jpg',
    'Allium_schoenoprasum_003.jpg','Peppermint_Mentha_x_piperita.jpg','Petroselinum_crispum_003.jpg',
    'Pennisetum_alopecuroides_Hameln.jpg','Urtica_dioica_Ies.jpg','Bellis_perennis_L_002.jpg',
    'Matricaria_recutita_-_Echte_Kamille_-_true_camomile.jpg','Leucanthemum_vulgare_Maikonigin_kz.jpg',
    'Papaver_rhoeas_in_Kullu_valley.jpg','Anthriscus_sylvestris_kz.jpg','Glechoma_hederacea_kz2.jpg',
    'Rumex_acetosa_Lauvsnes.jpg','Stellaria_media_kz.jpg','Geum_rivale_close-up.jpg',
    'Heracleum_sphondylium_kz1.jpg','Galium_aparine_kz.jpg','Tanacetum_vulgare_kz1.jpg',
    'Verbascum_thapsus1.jpg','Knautia_arvensis_kz1.jpg','Silene_flos-cuculi_kz1.jpg',
    'Capsella_bursa-pastoris_kz.jpg','Ranunculus_repens_kz.jpg','Claytonia_perfoliata_kz1.jpg',
    'Atriplex_hortensis_kz.jpg','Galinsoga_parviflora_kz.jpg','Buddleja_davidii_Fascinating_kz.jpg',
    'Corylus_avellana_catkins.jpg','Prunus_spinosa_Prunus_spinosa_(aka).jpg',
    'Amelanchier_lamarckii_blooms.jpg','Hydrangea_macrophylla_kz01.jpg',
    'Forsythia_x_intermedia_Lynwood_kz.jpg','Cornus_alba_Sibirica_kz1.jpg',
    'Spiraea_nipponica_Snowmound_kz.jpg','Magnolia_x_soulangeana_kz01.jpg',
    'Lavandula_angustifolia_kz01.jpg','Hedera_helix_kz5.jpg','Mahonia_aquifolium_kz04.jpg',
    'Ilex_aquifolium_kz03.jpg','Rhododendron_ponticum_kz2.jpg','Buxus_sempervirens_kz01.jpg',
    'Quercus_robur_kz1.jpg','Tilia_x_europaea_kz1.jpg','Betula_pubescens_kz2.jpg',
    'Fagus_sylvatica_Atropurpurea.jpg','Crataegus_laevigata_kz1.jpg','Clematis_Jackmanii_kz.jpg',
    'Parthenocissus_tricuspidata_kz1.jpg','Rosa_glauca_kz1.jpg','Aquilegia_vulgaris_kz01.jpg',
    'Vaccinium_myrtillus_kz1.jpg','Geranium_phaeum_kz1.jpg','Hesperis_matronalis_kz.jpg',
    'Thymus_pulegioides_kz.jpg','Geum_urbanum_kz1.jpg','Geranium_pratense_kz03.jpg',
    'Saponaria_officinalis_kz.jpg','Berberis_vulgaris_kz1.jpg','Veronica_longifolia_kz.jpg',
    'Myosotis_scorpioides_kz.jpg','Carex_buchananii_kz.jpg','Cortaderia_selloana_kz1.jpg',
    'Molinia_caerulea_kz1.jpg','Achillea_ptarmica_kz.jpg','Hieracium_aurantiacum_kz.jpg',
    'Berberis_thunbergii_kz1.jpg','Ribes_sanguineum_kz01.jpg','Weigela_florida_kz.jpg',
    'Acer_campestre_kz03.jpg','Hypericum_Hidcote_kz.jpg','Leycesteria_formosa_kz.jpg',
    'Deutzia_gracilis_kz.jpg','Ligustrum_vulgare_kz.jpg','Lonicera_nitida_kz.jpg',
    'Skimmia_japonica_kz03.jpg','Aucuba_japonica_kz.jpg','Eucalyptus_gunnii_kz.jpg',
    'Cotoneaster_suecicus_kz.jpg','Berberis_julianae_kz.jpg','Clematis_armandii_kz.jpg',
    'Fallopia_baldschuanica_kz.jpg','Hydrangea_anomala_petiolaris_kz.jpg','Rosa_nitida_kz.jpg',
    'Kerria_japonica_kz.jpg','Diervilla_sessilifolia_kz.jpg','Symphoricarpos_x_chenaultii_kz.jpg',
    'Cornus_sericea_kz.jpg','Salix_babylonica_var._pekinensis_kz.jpg','Poncirus_trifoliata_kz.jpg',
    'Allium_giganteum_kz.jpg','Hyacinthus_orientalis_kz.jpg','Anemone_blanda_kz1.jpg',
    'Scilla_siberica_kz.jpg','Fritillaria_imperialis_kz01.jpg','Anemone_coronaria_kz.jpg',
    'Fuchsia_hybrida_hort_ex_Siebold_Voss.jpg','Mandevilla_splendens_kz.jpg',
    'Pelargonium_zonale_kz.jpg','Cordyline_australis_kz.jpg','Petunia_Surfinia_White_kz.jpg',
    'Begonia_semperflorens_kz.jpg','Impatiens_walleriana_kz.jpg','Dianthus_barbatus_kz.jpg',
    'Osteospermum_cultivar_kz.jpg','Carpinus_betulus_kz2.jpg','Acer_pseudoplatanus_kz1.jpg',
    'Fraxinus_excelsior_kz1.jpg','Laburnum_x_watereri_kz.jpg','Platanus_hispanica_kz1.jpg',
    'Populus_alba_kz1.jpg','Prunus_cerasifera_kz1.jpg','Salix_x_sepulcralis_kz.jpg',
    'Cedrus_atlantica_kz.jpg','Chamaecyparis_lawsoniana_kz.jpg','Cupressocyparis_leylandii_kz.jpg',
    'Picea_abies_kz03.jpg','Pinus_mugo_kz.jpg','Thuja_occidentalis_kz.jpg','Tsuga_canadensis_kz.jpg',
    'Calystegia_sepium_kz.jpg','Cardamine_hirsuta_kz.jpg','Cerastium_fontanum_kz.jpg',
    'Elymus_repens_kz.jpg','Erigeron_canadensis_kz.jpg','Persicaria_maculosa_kz.jpg',
    'Petasites_hybridus_kz.jpg','Poa_annua_kz.jpg','Polygonum_aviculare_kz.jpg',
    'Pteridium_aquilinum_kz.jpg','Ranunculus_acris_kz.jpg','Rumex_obtusifolius_kz.jpg',
    'Senecio_vulgaris_kz.jpg','Solanum_nigrum_kz.jpg','Sonchus_arvensis_kz.jpg',
    'Urtica_urens_kz.jpg','Veronica_filiformis_kz.jpg',
]

def search_commons(prefix):
    params = urllib.parse.urlencode({
        'action': 'query', 'list': 'allimages',
        'aiprefix': prefix, 'ailimit': 5,
        'aiprop': 'title', 'format': 'json',
    })
    req = urllib.request.Request(f'{API}?{params}', headers={'User-Agent': 'PlantenpediaBot/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        return [img['title'].replace('File:', '') for img in data.get('query', {}).get('allimages', [])]
    except:
        return []

replacements = {}
no_replacement = []

for i, fn in enumerate(missing_list):
    parts = fn.replace('_', ' ').split()
    prefix = '_'.join(parts[:2]) if len(parts) >= 2 else parts[0]
    results = search_commons(prefix)
    good = [r for r in results if r.lower().endswith(('.jpg', '.png', '.jpeg'))]
    if good:
        replacements[fn] = good[0]
    else:
        no_replacement.append(fn)
    if i % 30 == 29:
        time.sleep(0.5)

out_path = 'c:/Users/jonat/OneDrive/Documenten/Ecologisch hovenier/Plantenpedia/data/photo_replacements.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({'replacements': replacements, 'no_replacement': no_replacement}, f, ensure_ascii=False, indent=2)

print(f'Klaar: {len(replacements)} vervangingen, {len(no_replacement)} zonder resultaat')
for fn in no_replacement:
    print('GEEN:', fn)
