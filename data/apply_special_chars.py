import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/special_char_replacements.json', encoding='utf-8') as f:
    replacements = json.load(f)

script_path = 'data/verrijkingsscript.py'
with open(script_path, encoding='utf-8') as f:
    src = f.read()

count = 0
for old_fn, new_fn in replacements.items():
    new_fn_clean = new_fn.replace(' ', '_')
    if old_fn in src:
        src = src.replace(f'wiki("{old_fn}"', f'wiki("{new_fn_clean}"')
        count += 1
        print(f'OK  {old_fn}')
        print(f'    -> {new_fn_clean}')
    else:
        print(f'??? Niet gevonden: {old_fn}')

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'\n{count}/{len(replacements)} vervangingen toegepast')
