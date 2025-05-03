import json
with open('config.json', 'r', encoding='utf-8') as fh:
    config = json.load(fh)
with open('delta.json', 'r', encoding='utf-8') as fh:
    delta = json.load(fh)
print(delta['updates'])
for addition in delta['additions']:
    key = addition['key']
    value = addition['value']
    config[key] = value
for deletion in delta['deletions']:
    key = deletion['key']
    config.pop(key) 
print(config)
for _ in delta['updates']:
    k = _['key']
    val = _['to']
    config[k] = val
with open('res_patched_config.json', 'w', encoding='utf-8') as fh:
    json.dump(config, fh, ensure_ascii=False, indent=4)
