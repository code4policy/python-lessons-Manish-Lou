import json
import csv

# Step 1: Read superheroes.json
with open('superheroes.json', 'r') as file:
    data = json.load(file)

# Step 2: Create an empty array for powers
powers = []

# Step 3: Loop through members and append powers to the powers array
for member in data['members']:
    powers.extend(member['powers'])  # Extend list with powers

# Print all powers
print("All Powers:", powers)

# Step 4 (Bonus): Get unique powers
unique_powers = list(set(powers))
print("Unique Powers:", unique_powers)

# Step 5: Write a flat CSV of members
csv_filename = 'superheroes.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'name', 'age', 'secretIdentity', 'powers', 
        'squadName', 'homeTown', 'formed', 'secretBase', 'active'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Loop through members and write each as a row
    for member in data['members']:
        writer.writerow({
            'name': member['name'],
            'age': member['age'],
            'secretIdentity': member['secretIdentity'],
            'powers': member['powers'],  # Powers as a list
            'squadName': data['squadName'],
            'homeTown': data['homeTown'],
            'formed': data['formed'],
            'secretBase': data['secretBase'],
            'active': data['active']
        })

# Bonus: Write one row per power
csv_filename_per_power = 'superheroes_per_power.csv'
with open(csv_filename_per_power, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'name', 'age', 'secretIdentity', 'power', 
        'squadName', 'homeTown', 'formed', 'secretBase', 'active'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Loop through members and write each power as a separate row
    for member in data['members']:
        for power in member['powers']:
            writer.writerow({
                'name': member['name'],
                'age': member['age'],
                'secretIdentity': member['secretIdentity'],
                'power': power,  # Each power in a separate row
                'squadName': data['squadName'],
                'homeTown': data['homeTown'],
                'formed': data['formed'],
                'secretBase': data['secretBase'],
                'active': data['active']
            })

print("CSV files created successfully!")
