# écrit dans un fichier (attention, cela écrase le texte quand on fait write)

fichier = open('ultima_verba.txt', 'w')
fichier.write("yo")

#lit dans un fichier

fichier = open('ultima_verba.txt', 'r')
print(fichier.read())
fichier.close()

fichier = open('test.txt', 'w')
fichier.write("Le lion ne s'associe pas avec le cafard")
fichier.close()

fichier = open('test.txt', 'r')
print(fichier.read())
fichier.close()

# ajouter un texte dans un fichier existant sans écraser le texte
fichier = open('test.txt', 'a')
fichier.write("\nVictor Hugo, Jersey, 2 décembre 1852\n")
fichier.close()

# faire un input : permet de faire une invite où on doit rentrer des informations. il faut utiliser le f pour que ce soit comme une variable et pas un string.

age = input("Insérez votre age: ")
print(f"vous avez {age} ans")

