#!usr/bin/python3

def triangle_iso_croissant(taille: int)-> int:
    compteur_espace = taille

    print(" " *compteur_espace, end="")
    print("*")

    compteur_espace -= 1

    for y in range(1, taille):
        print(" " * compteur_espace, end='')
        print("*" * (2*y+1))

        compteur_espace -= 1

    return