import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/photo_replacements.json', encoding='utf-8') as f:
    data = json.load(f)

replacements = data['replacements']

script_path = 'data/verrijkingsscript.py'
with open(script_path, encoding='utf-8') as f:
    src = f.read()

original = src
count = 0

for old_fn, new_fn in replacements.items():
    # Normalize new filename: spaces -> underscores
    new_fn_clean = new_fn.replace(' ', '_')
    if old_fn in src:
        src = src.replace(f'wiki("{old_fn}"', f'wiki("{new_fn_clean}"')
        count += 1
        print(f'Vervangen: {old_fn}')
        print(f'       -> {new_fn_clean}')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'\n{count} vervangingen toegepast in verrijkingsscript.py')
unchanged = len(replacements) - count
if unchanged:
    print(f'{unchanged} niet gevonden in script (mogelijk al correct of ander format)')
