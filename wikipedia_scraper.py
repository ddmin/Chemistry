from bs4 import BeautifulSoup as soup 
import requests
import re
import json

site = "https://en.wikipedia.org/wiki/List_of_chemical_elements"
r = requests.get(site).text
s = soup(r, 'lxml')

table = s.find('table', {"class":"wikitable sortable collapsible"})
table_data = table.find_all('td')

elements = [table_data[x:x+13] for x in range(0,len(table_data),13)]
elements.pop(-1)

elements_json = {"Elements": {}}
for x in elements:
	p = re.compile(r'\[\D+\]')
	for n, y in enumerate(x):
		y = y.text
		x[n] = re.sub(p, '', y)

	d = {
		"Atomic Number": x[0],
		"Symbol": x[1],
		"Etymology": x[3],
		"Group": x[4],
		"Period": x[5],
		"Atomic Weight": x[6],
		"Density": x[7],
		"Melting Point": x[8],
		"Boiling Point": x[9],
		"Specific Heat": x[10],
		"Electronegativity": x[11],
		"Abundance": x[12][:-1]
		}

	elements_json["Elements"][x[2]] = d

with open("elements.json", "w") as f:
	json.dump(elements_json, f, indent=2)