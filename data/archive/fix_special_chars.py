import urllib.request, urllib.parse, json, sys, time
sys.stdout.reconfigure(encoding='utf-8')

API = 'https://commons.wikimedia.org/w/api.php'

targets = [
    ('Aster_×_frikartii_\'Mönch\'_3.jpg',          'Aster_frikartii'),
    ('Hosta_tardiana_\'Halcyon\'.jpg',               'Hosta_tardiana'),
    ('Leucanthemum_x_superbum_\'Becky\'.jpg',        'Leucanthemum_x_superbum'),
    ('Paeonia_lactiflora_\'Sarah_Bernhardt\'_1.jpg', 'Paeonia_lactiflora'),
    ('Pulmonaria_saccharata_\'Mrs_Moon\'.jpg',        'Pulmonaria_saccharata'),
    ('Salvia_nemorosa_\'Caradonna\'_kz02.jpg',       'Salvia_nemorosa'),
    ('Viola_x_wittrockiana_Blaue_Schönheit.jpg',     'Viola_x_wittrockiana'),
    ('Dahlia_x_hybrida_Nuit_d\'ete.jpg',             'Dahlia'),
    ('Crocus_chrysanthus_\'Blue_Bird\'_02.jpg',      'Crocus_chrysanthus'),
    ('Pennisetum_alopecuroides_\'Hameln\'.jpg',      'Pennisetum_alopecuroides'),
    ('Leucanthemum_vulgare_\'Maikonigin\'_kz.jpg',   'Leucanthemum_vulgare'),
    ('Cornus_alba_\'Sibirica\'_kz1.jpg',             'Cornus_alba'),
    ('Spiraea_nipponica_\'Snowmound\'_kz.jpg',       'Spiraea_nipponica'),
    ('Fuchsia_hybrida_hort_ex_Siebold_&_Voss.jpg',  'Fuchsia'),
    ('Hypericum_\'Hidcote\'_kz.jpg',                 'Hypericum_calycinum'),
    ('Clematis_\'Jackmanii\'_kz.jpg',                'Clematis_jackmanii'),
]

def search(prefix, limit=8):
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
    except Exception as e:
        print(f'  ERROR: {e}')
        return []

results = {}
for old_fn, prefix in targets:
    hits = search(prefix)
    good = [r for r in hits if r.lower().endswith(('.jpg', '.png', '.jpeg'))]
    if good:
        results[old_fn] = good[0]
        print(f'OK  {old_fn}')
        print(f'    -> {good[0]}')
    else:
        print(f'??? {old_fn}  (prefix={prefix})')
    time.sleep(0.15)

with open('data/special_char_replacements.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f'\nKlaar: {len(results)}/{len(targets)} vervangingen gevonden')
