#!usr/bin/python3

from Exercice_4.nmb_jours import nb_jours_annee

def nbre_jours_debut_ere(année_max: int) -> int:
    """Calcule le nmb de j passé depuis le début de l'ère chrétienne"""
    nmb_jours = 0

    for année in range (1, année_max + 1):
        nmb_jours += nb_jours_annee(année)

    return nmb_jours
