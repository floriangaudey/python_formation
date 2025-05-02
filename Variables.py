# Variabilisation

# les nombres ne peuvent pas être une variable

a = 12
b = 34
c = 56
y = a * b + c
print(y)

# Ajoute le nombre à la variable existante

x = 2
print(x)
x += 1
print(x)
x += 3
print(x)

# Exercice de calcul du CA

daily_rate = 500
worked_days = 20
revenue = daily_rate * worked_days
print(revenue)

# insérer une variable dans un string (appelé f-string pour formatted string)

name = "Florian"
greeting = f"hello {name}"
print(greeting)

ma_boite = "de l'oseille"
my_string = f"ma boite contient {ma_boite}"
print(my_string)

# On ne peut pas effacer des fonctions existantes

# print = "je viens d'effacer la fonction print!!!"
# print("test")
# print(print)

# Exercice date
date = "2024/12/25"
day = date[-2:]
month = date[5:7]
year = date[:4]
format_date = f"{day}-{month}-{year}"
print(format_date)


# mini-exercice

machine_id = "DM-2"
machine_id_part_2 = machine_id[-1].zfill(3)
machine_id_part_1 = machine_id[:3]
new_id = f"{machine_id_part_1}{machine_id_part_2}"
print(new_id)

# Mini-quizz

#print(42[0])
#print("42"[2])
print("tom marvolo riddle"[:3])
print("django".capitalize())
print("Da Vinci Code"[-4:].lower())
print("2024-12-25".split("-"))
print("7".zfill(3))
