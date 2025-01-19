#!usr/bin/python3

from Exercice_5.nbre_jours_mois import nbre_jours_mois
from Exercice_8.debut_ere import nbre_jours_debut_ere

def nbre_jours_debut_ere_jma(jours: int, mois_max: int, année_max: int) -> int:

    total_jours = 0
    total_jours += nbre_jours_debut_ere(année_max - 1)

    for mois in range(1, mois_max):
        total_jours += nbre_jours_mois(mois, année_max)

    return total_jours + jours
