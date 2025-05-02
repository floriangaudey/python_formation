fruits = ["pommes", "poires", "citron"]
print(fruits)

its_easy_as = [1, 2, 3]
print(its_easy_as)

title = [4, "mariages", "et", 1, "enterrement"]
print(title)

lotr = ["La communauté de l'anneau", "Les deux tours", "Le retour du roi"]
movies = ["Titanic", "Django", lotr]
print(movies)

#renvoie la longueur d'une liste

my_list = [1, 2, 3]
print(len(my_list))

# slicing et indexing
print(my_list[0])
print(my_list[1:3])
print(my_list[-1])
print(my_list[1:])

#Concaténer des listes

# Concaène les 2 listes
nb = [1, 2 ,3]
my_double_list = nb + nb
print(my_double_list)

#tenter d'intégrer un nombre dans la liste (spoiler = ça ne marche pas)
#try_new_list = nb + 4
#print(try_new_list)

# ajoute un élément dans la liste

nb2 = [1, 2, 3]
nb2.append(4)
print(nb2)

# ajouter une liste à une autre liste avec append
my_list_append = [1, 2, 3]
my_list_append.append(my_list_append)
print(my_list_append)

# ajouter une liste à une autre liste avec extend

my_list_extend = [1, 2, 3]
my_list_extend.extend(my_list_extend)
print(my_list_extend)

# fonction del

list_del = [1, 2, 3]
del(list_del[-1])
print(list_del)

# remplace le dernier élément par une autre valeur

list_del[-1] = "ZERO!!"
print(list_del)

# on ne peut pas faire une suppression de valeur dans une chaine de caractère

#my_string = "123"
#del(my_string[-1])
#print(my_string)

#my_string = "123"
#my_string[-1] = "ZERO!!"
#print(my_string)

my_list = [2, 5, 3, 4, 10, 0]
my_list.sort()
print(my_list)

my_list = [2, 5, 3, 4, 10, 0]
my_list = sorted(my_list)
print(my_list)

groceries = ["tomatoes", "carrots", "bananas"]
groceries[1] = "burgers"
print(groceries)

groceries = ["tomatoes", "carrots", "bananas"]
groceries.reverse()
print(groceries)
