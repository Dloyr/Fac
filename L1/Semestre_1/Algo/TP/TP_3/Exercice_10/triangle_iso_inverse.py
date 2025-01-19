def triangle_iso_decroissant(taille: int)-> int:
    compteur_espace = 0

    for y in range(taille - 1, 0, -1):
        print( compteur_espace * " ", end="")
        print("*" * (2*y+1))

        compteur_espace += 1

    print(" " * compteur_espace, end="")
    print("*")

    return