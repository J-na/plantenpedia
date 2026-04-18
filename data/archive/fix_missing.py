import urllib.request, urllib.parse, json, sys, re, time
sys.stdout.reconfigure(encoding='utf-8')

API = 'https://commons.wikimedia.org/w/api.php'

no_replacement = [
    'Aconitum_carmichaelii2.jpg','Aubrieta_deltoidea0.jpg','Centaurea_montana0.jpg',
    'Coreopsis_verticillata4.jpg','Echinacea_purpurea1.jpg','Erysimum_cheiri1.jpg',
    'Euphorbia_epithymoides1.jpg','Iberis_sempervirens2.jpg','Lupinus_Russell_hybrids.jpg',
    'Cornflower_Centaurea_cyanus_Purple_Gem.jpg','Laurus_nobilis-leaves.jpg',
    'Verbascum_thapsus1.jpg','Clematis_Jackmanii_kz.jpg','Aquilegia_vulgaris_kz01.jpg',
    'Geranium_phaeum_kz1.jpg','Thymus_pulegioides_kz.jpg','Saponaria_officinalis_kz.jpg',
    'Carex_buchananii_kz.jpg','Achillea_ptarmica_kz.jpg','Berberis_thunbergii_kz1.jpg',
    'Weigela_florida_kz.jpg','Hypericum_Hidcote_kz.jpg','Leycesteria_formosa_kz.jpg',
    'Ligustrum_vulgare_kz.jpg','Lonicera_nitida_kz.jpg','Aucuba_japonica_kz.jpg',
    'Eucalyptus_gunnii_kz.jpg','Berberis_julianae_kz.jpg','Fallopia_baldschuanica_kz.jpg',
    'Hydrangea_anomala_petiolaris_kz.jpg','Rosa_nitida_kz.jpg','Diervilla_sessilifolia_kz.jpg',
    'Cornus_sericea_kz.jpg','Poncirus_trifoliata_kz.jpg',
    'Allium_giganteum_kz.jpg','Anemone_blanda_kz1.jpg','Scilla_siberica_kz.jpg',
    'Anemone_coronaria_kz.jpg','Mandevilla_splendens_kz.jpg','Pelargonium_zonale_kz.jpg',
    'Cordyline_australis_kz.jpg','Begonia_semperflorens_kz.jpg','Impatiens_walleriana_kz.jpg',
    'Osteospermum_cultivar_kz.jpg','Acer_pseudoplatanus_kz1.jpg','Laburnum_x_watereri_kz.jpg',
    'Populus_alba_kz1.jpg','Prunus_cerasifera_kz1.jpg','Cedrus_atlantica_kz.jpg',
    'Chamaecyparis_lawsoniana_kz.jpg','Pinus_mugo_kz.jpg','Thuja_occidentalis_kz.jpg',
    'Calystegia_sepium_kz.jpg','Cerastium_fontanum_kz.jpg','Elymus_repens_kz.jpg',
    'Persicaria_maculosa_kz.jpg','Poa_annua_kz.jpg','Pteridium_aquilinum_kz.jpg',
    'Rumex_obtusifolius_kz.jpg','Senecio_vulgaris_kz.jpg','Sonchus_arvensis_kz.jpg',
    'Urtica_urens_kz.jpg',
]

def make_prefix(fn):
    # Strip extension, split on underscore, take first 2 words, strip trailing digits
    base = re.sub(r'\.[^.]+$', '', fn)  # remove extension
    parts = base.split('_')
    # Take genus + species (first 2 parts), strip trailing digits from species
    p1 = parts[0] if parts else ''
    p2 = re.sub(r'\d+$', '', parts[1]) if len(parts) > 1 else ''
    if p2:
        return f'{p1}_{p2}'
    return p1

def search_commons(prefix, limit=5):
    params = urllib.parse.urlencode({
        'action': 'query', 'list': 'allimages',
        'aiprefix': prefix, 'ailimit': limit,
        'aiprop': 'title', 'format': 'json',
    })
    req = urllib.request.Request(f'{API}?{params}', headers={'User-Agent': 'PlantenpediaBot/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        return [img['title'].replace('File:', '') for img in data.get('query', {}).get('allimages', [])]
    except:
        return []

# Load existing replacements
with open('data/photo_replacements.json', encoding='utf-8') as f:
    existing = json.load(f)

replacements = existing['replacements']
still_missing = []

for fn in no_replacement:
    prefix = make_prefix(fn)
    results = search_commons(prefix, limit=5)
    good = [r for r in results if r.lower().endswith(('.jpg', '.png', '.jpeg'))]
    if good:
        replacements[fn] = good[0]
        print(f'OK  {fn}')
        print(f'    {good[0]}')
    else:
        # Try with just genus
        genus = fn.split('_')[0]
        results2 = search_commons(genus, limit=5)
        good2 = [r for r in results2 if r.lower().endswith(('.jpg', '.png', '.jpeg'))
                 and r.lower().startswith(genus.lower())]
        if good2:
            replacements[fn] = good2[0]
            print(f'OK~ {fn}')
            print(f'    {good2[0]}')
        else:
            still_missing.append(fn)
            print(f'??? {fn}')
    time.sleep(0.1)

# Save updated replacements
with open('data/photo_replacements.json', 'w', encoding='utf-8') as f:
    json.dump({'replacements': replacements, 'no_replacement': still_missing}, f, ensure_ascii=False, indent=2)

print(f'\nNog steeds geen vervanging ({len(still_missing)}):')
for fn in still_missing:
    print(' ', fn)
