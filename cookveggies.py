import csv

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)


import json

with open('output/vegetables.json', 'w') as f:
    json.dump(vegetables, f)