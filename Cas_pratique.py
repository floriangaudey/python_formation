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

# conversion miles en km
specifications = drilling_machine_two["specifications"]["depth_capacity_miles"]
miles_to_km = specifications * 1.609
km_to_m = miles_to_km * 1000

drilling_machine_two["specifications"]["depth_capacity_miles"] = km_to_m

# conversion date brintannique en format français
date = drilling_machine_two["last_maintenance_date"]
Date_split = date.split("-")
date_Finale = Date_split[2]+"/"+Date_split[1]+"/"+Date_split[0]

drilling_machine_two["last_maintenance_date"] = date_Finale

date = drilling_machine_two["next_maintenance_due"]
Date_split = date.split("-")
date_Finale = Date_split[2]+"/"+Date_split[1]+"/"+Date_split[0]

drilling_machine_two["next_maintenance_due"] = date_Finale

# Créer la zone de contact 

contact_information = {
  "operator_company" : None,
  "contact_person" : None,
  "phone" : None,
  "email" : None,
}

drilling_machine_two["contact_information"] = contact_information

# uniformiser l'identifiant machine_id

id_letter, id_number = drilling_machine_two["machine_id"].split("-")
machine_id_number = id_number.zfill(3)
machine_id_uniforme = f"{id_letter}-{machine_id_number}"
drilling_machine_two["machine_id"] = machine_id_uniforme

print(drilling_machine_two)

