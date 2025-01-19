#!usr/bin/python3

def triangle_rect_hd(taille: int)-> int:
    """Print un triangle orienté vers la droite"""
    compteur_espace = 0

    for y in range(taille, 0, -1):
        print( compteur_espace * " ", end="")
        print("*" * y)

        compteur_espace += 1

    return