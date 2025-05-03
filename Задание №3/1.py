import json
with open('config.json', 'r', encoding='utf-8') as fh:
    a = json.load(fh)
with open('patched_config.json', 'r', encoding='utf-8') as fh:
    b = json.load(fh)
additions = []
deletions = []
for key in b.keys():
    if key not in a:
        additions.append({'key': key, 'value': b[key]})
for key in a.keys():
    if key not in b:
        deletions.append({'key': key, 'value': a[key]})
updates = []
for key in a.keys():
    if key in b and a[key] != b[key]:
        updates.append({'key': key, 'from': a[key], 'to': b[key]})
result = {
    'additions': additions,
    'deletions': deletions,
    'updates': updates
}
with open('delta.json', 'w', encoding='utf-8') as fh:
    json.dump(result, fh, ensure_ascii=False, indent=4)
