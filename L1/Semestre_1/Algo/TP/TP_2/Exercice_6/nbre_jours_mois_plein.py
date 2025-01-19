#!usr/bin/python3

from Exercice_5.nbre_jours_mois import nbre_jours_mois
from Exercice_3.annee_bis import annee_bissextile

def nbre_jours_mois_pleins_depuis_1janvier(max_mois: int, année: int) -> int:
    """Fct pour connaitre le nmb de jours passés depuis le 1er janviers"""

    mois = 0
    nmb_jours = 0

    for mois in range(max_mois):
        nmb_jours += nbre_jours_mois(mois, année)

    if annee_bissextile(année):
        nmb_jours -= 1
    else:
        if max_mois == 2:
            nmb_jours -= 2
        else:
            nmb_jours -= 1

    return nmb_jours
