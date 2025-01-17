vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

import csv

with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color', 'length'])
    for vegetable in vegetables:
         writer.writerow([vegetable['name'], vegetable['color'], len(vegetable['name'])])
    