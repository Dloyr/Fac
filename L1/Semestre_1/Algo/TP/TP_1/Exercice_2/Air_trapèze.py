#!usr/bin/python3

def air_trapèze(hauteur:float, largeur_inf:float, largeur_sup:float) -> float:
    """Fct pour calculer l'air d'un trapèze"""

    Res_air = 1/2 * (largeur_inf + largeur_sup) * hauteur

    print("L'air du trapèze faisant {:.1f} de hauteur, {:.1f} de largeur inférieur et {:.1f} de largeur supérieur est de {:.1f}".format(hauteur, largeur_inf, largeur_sup, Res_air))

    return air_trapèze