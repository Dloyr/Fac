#!usr/bin/python3

def aire_piece(l_mur_1_2: float, L_mur_1_2:float, l_mur_3_4: float, L_mur_3_4: float) -> float:
    """Fct pour calculer l'air totale de la pièce"""

    aire_mur_1_2 = L_mur_1_2 * l_mur_1_2
    aire_mur_3_4 = L_mur_3_4 * l_mur_3_4
    aire_plafond = L_mur_1_2 * l_mur_3_4

    aire_pièce = aire_mur_1_2 + aire_mur_3_4 + aire_plafond

    print("L'aire totale de la pièce est de {:.1f}".format(aire_pièce))

    return aire_pièce