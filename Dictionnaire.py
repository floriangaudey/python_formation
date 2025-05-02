# Initialisation de la dictionnaire

my_dict = {
    "key1": "value2",
    "key2": "value2",
}

print(type(my_dict))

# Exercice

ross = {
    "name": "Geller",
    "girlfriend": "Rachel",
}

print(ross["name"])

# Ajout d'un nouvel attribut

ross["sister"] = "Monica"
print(ross)

ross["girlfriend"] = "Emily"
print(ross)

# Exercice

warehouse_stocks = {"banana": 200, "lettuce": 20, "tomatoes": 50}
number_of_tomatoes = warehouse_stocks["tomatoes"]
print(number_of_tomatoes)

Florian_infos = {
    "age": 35,
    "year_in_company": 1,
    "salary": 42000,
}

dict_of_dict = {"Florian": Florian_infos, "Emma": {"age":33, "year_in_company":20, "salary": 100000}}
print(dict_of_dict["Emma"])
print(dict_of_dict["Emma"]["age"])

my_dict = {}
my_dict["test"] = ["list", "of", "strings"]
print(my_dict)

# Affiche les infos d'un dictionnaire

print(dict_of_dict.keys())
print(dict_of_dict.values())
print(dict_of_dict.items())

drilling_machine = {
    "machine_id": "DM-001",
    "name": "Deep Driller 3000",
    "location": {
        "latitude": 29.7355,
        "longitude": -95.3635,
        "region": "Gulf of Mexico",
        "country": "USA",
    },
}

print(drilling_machine["location"]["country"])

my_dict = {"key": [1, 2, 3]}

inside_list = my_dict["key"]  # returns [1, 2, 3]
number = inside_list[1]  # returns [1, 2, 3][1] which is 2
print(number)

lotr_movies = ["The Fellowship of The Ring", "The Two Towers", "The Return of The King"]
movies = ["Titanic", "Django", lotr_movies]
print(movies)
print(movies[2][2])

groceries = {
	"tomatoes": 5,
	"bananas": 3,
	"beef": "100g",
}

groceries = {
    "tomatoes": {"quantity": 5, "rayon": "vegetables"},
    "bananas": {"quantity": 3, "rayon": "vegetables"},
    "beef": {"quantity": "100g", "rayon": "butcher's shop"},
}

drilling_machine = ["DM-1", "DM-2"]


