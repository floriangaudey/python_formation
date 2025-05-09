# les tuples ne sont pas modifiables, donc on les utilise en tant que liste lorsque ça ne bouge pas
my_tuple = ("no_change_is_possible", "this_thing_is_fixed")

print(my_tuple)

# Exercice

drilling_machine_two = {
  "machine_id": "DM-2",
  "name": "Land Rover 200",
  "location": {
    "latitude": 37.7749,
    "longitude": -107.9090,
    "region": "San Juan Basin",
    "country": "USA"
  },
  "status": "Under Maintenance",
  "specifications": {
    "type": "Onshore",
    "depth_capacity_miles": 7,
    "drilling_speed_miles_per_day": 0.3,
    "crew_size": 25,
    "power_source": "Electric"
  },
  "last_maintenance_date": "2024-07-15",
  "next_maintenance_due": "2025-01-15"
}

latitude = drilling_machine_two["location"]["latitude"]
longitude = drilling_machine_two["location"]["longitude"]

coordinates = (latitude, longitude)

drilling_machine_two["location"]["coordinates"] = coordinates

print(drilling_machine_two)

# le set sert à nettoyer les éléments en doublons qu'on a trouvé

my_set = {"element1", "element2"}

transactions = {
    "TR1" : "ID001",
    "TR2" : "ID002",
    "TR3" : "ID001",
}

print(transactions.values())
print(set(transactions.values()))
print(list(set(transactions.values())))

# utilisation de set pour comparer des structures de listes

colonnes_excel = ["nom", "prenom", "adresse", "ville", "code_postal"]
colonnes_excel2 = ["nom", "prenom", "adress", "ville", "postal_code"]

print(set(colonnes_excel) - set(colonnes_excel2))
print(set(colonnes_excel2) - set(colonnes_excel))

print(set(colonnes_excel).symmetric_difference(colonnes_excel2))

