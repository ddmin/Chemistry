import re 
import json

def find_molar_mass(compound):
    p = re.compile(r'([A-Z][a-z]?)([0-9]*)')
    matches = re.findall(p, compound)

    d = {}
    for match in matches:
        d.setdefault(match[0], 0)
        
        if match[1] != '':
            d[match[0]] += int(match[1])
        else:
            d[match[0]] += 1

    molarmass = 0
    for x, y in d.items():
        molarmass += elements[x] * y

    return molarmass

def mm(compound):
    
    p = re.compile(r'\((\w+)\)([0-9])*')
    matches = re.findall(p, compound)

    compound = re.sub(p, '', compound)

    molarmass = find_molar_mass(compound)

    for match in matches:
        if match[1] == '':
            n = 1
        else:
            n = int(match[1])

        molarmass += find_molar_mass(match[0]) * n

    return molarmass

with open("atomic_weights.json", "r") as f:
        elements = json.load(f)
