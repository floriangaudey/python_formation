def my_function(x):
    output_string = f"vous avez inséré {x} dans la fonction"
    return output_string


print(my_function("salut"))  # résultat: "vous avez inséré salut dans la fonction"


def double(x):
    output = x * 2
    return output


print(double(21))  # résultat: 42
print(double("abc"))  # résultat: "abcabc"


def fonction_affine_maths(x):
    y = 4 * x + 2  # A = 4, b = 2
    return y


resultat = fonction_affine_maths(4)
print(resultat)  # résultat: 18


def fonction_qui_renvoie_toujours_la_meme_chose():
    return 42


response = fonction_qui_renvoie_toujours_la_meme_chose()
print(response)  # résultat: 42

# L'indentation est importante, si pas d'indentation, une erreur surviendra.

def ma_fonction():  # aucune identation
    print("salut")  # indentation de 4 espaces
    
def autre_fonction():
  print("yo")  # indentation de deux expaces
  
ma_fonction()
autre_fonction()

# Exercice 1

def hello_there():
    print("hello there")

hello_there()

# Exercice 2

def print_bonjour(x):
    return f"bonjour {x} !"

print(print_bonjour("Florian"))

# Exercice 3

def create_greeting(name):
    hello = "Hello {name} !"
    return hello

print(create_greeting("Florian"))

# Exercice 4

def jesus(pains, nb):
    qte = pains * nb
    return qte

print(jesus(3, 4))

# fonctions modernes (hints)

# Exercice 1

def multiply(x : int, y : int) -> float:
    return x * y

print(multiply(3,12))

# Exercice 2 

def jesus(pains : int, nb : int) -> float:
    qte = pains * nb
    return qte

print(jesus(3, 4))

# Exercice 3 

def divede_et_impera(x: int | float, y: int | float) -> int | float:
    return x / y 

print(divede_et_impera(4,3))

