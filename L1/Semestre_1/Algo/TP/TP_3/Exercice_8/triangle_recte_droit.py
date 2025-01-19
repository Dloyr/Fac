#!usr/bin/python3

def triangle_rect_bd(taille: int)-> int:

    compteur_espace = taille - 1

    for y in range(1, taille + 1):
        print(" " * compteur_espace, end='')
        print("*" * y)

        compteur_espace -= 1

    return
