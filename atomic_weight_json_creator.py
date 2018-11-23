import json
import re

with open("elements.json", "r") as f:
	elements = json.load(f)

symbol_json = {}

for element in elements['Elements']:
    p = re.compile(r'[^\d\.]')
    atomic_weight = elements['Elements'][element]['Atomic Weight']
    atomic_weight = re.sub(p, '', atomic_weight)

    symbol_json[elements['Elements'][element]['Symbol']] = float(atomic_weight)

with open("atomic_weights.json", "w") as f:
    json.dump(symbol_json, f, indent=2)