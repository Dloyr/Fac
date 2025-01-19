#!usr/bin/python3

#======================EXERCICE 1======================
def ligne_etoiles(number: int) -> int:
    """print a line"""
    for i in range(0, number):
        print("*", end='')

    print()
    return 1

#======================EXERCICE 2======================
def carre(coté: int) -> int:
    """Print square"""
    for i in range (0, coté):
        print(coté * "*")

    return 

#======================EXERCICE 3=======================
def rectangle(longueur: int, largeur: int)-> int:
    """Créer un rectangle"""
    for x in range(0, longueur):
        print("*" * largeur)

    return

#======================EXERCICE 4=======================
def triangle_rect_bg(taille: int)-> int:
    """Créer un triangle rectangle"""
    for y in range(1, taille + 1):
        print("*" * y)

    return

#======================EXERCICE 5=======================
def triangle_rect_hg(taille: int)-> int:
    """Print un triangle inversé"""
    for y in range(taille, 0, -1):
        print("*" * y)

    return

#======================EXERCICE 6=======================
def ligne_blancs(taille: int)-> int:
    """Print une ligne blanche"""
    print("'", end="")
    print(" " * taille, end="")
    print("'")

    return

#======================EXERCICE 7=======================
def triangle_rect_hd(taille: int)-> int:
    """Print un triangle orienté vers la droite"""
    compteur_espace = 0

    for y in range(taille, 0, -1):
        print( compteur_espace * " ", end="")
        print("*" * y)

        compteur_espace += 1

    return

#======================EXERCICE 8=======================
def triangle_rect_bd(taille: int)-> int:
    """Print un triangle rectangle en bas à droite"""
    compteur_espace = taille - 1

    for y in range(1, taille + 1):
        print(" " * compteur_espace, end='')
        print("*" * y)

        compteur_espace -= 1

    return

#======================EXERCICE 9=======================
def triangle_iso_croissant(taille: int)-> int:
    """Print un triangle isocèle la pointe vers le haut"""
    compteur_espace = taille

    print(" " *compteur_espace, end="")
    print("*")

    compteur_espace -= 1

    for y in range(1, taille):
        print(" " * compteur_espace, end='')
        print("*" * (2*y+1))

        compteur_espace -= 1

    return

#======================EXERCICE 10======================
def triangle_iso_decroissant(taille: int)-> int:
    """Print un triangle isocèle la pointe vers le bas"""
    compteur_espace = 0

    for y in range(taille - 1, 0, -1):
        print( compteur_espace * " ", end="")
        print("*" * (2*y+1))

        compteur_espace += 1

    print(" " * compteur_espace, end="")
    print("*")

    return

#======================EXERCICE 11======================
def losange(taille: int)-> int:
    """Print un losange"""
    triangle_iso_croissant(taille-1)
    triangle_iso_decroissant(taille)

    return

#======================EXERCICE 12======================
def suivant_syracuse(nombre: int)-> int:
    """Fct qui retourne la valeur suivante ds la suite de Syracuse"""
    if nombre % 2 == 0:
        return nombre // 2
    else:
        return 3 * nombre + 1

#======================EXERCICE 13======================
def nb_etapes_syracuse(nombre: int)-> int:
    """Fct qui compte le nombre de valeur ds la suite avant qu'elle ne soit = à 1"""
    compteur = 0

    while nombre != 1:
        nombre = suivant_syracuse(nombre)
        compteur += 1

    return compteur

#======================EXERCICE 14======================
def altitude_syracuse(nombre: int)-> int:
    """Retourne la valeur max au sein de la suite"""
    el_syracuse = []

    for index in range(1, nombre + 1):
        el_syracuse.append(suivant_syracuse(index))

    el_syracuse.sort()

    return el_syracuse[-1]
