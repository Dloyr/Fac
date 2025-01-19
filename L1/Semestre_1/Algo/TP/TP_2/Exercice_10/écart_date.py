#!usr/bin/python3

from Exercice_9.debut_dmy import nbre_jours_debut_ere_jma

def nbre_jours_entre_deux_dates(jours_1: int, mois_1: int, année_1: int, jours_2: int, mois_2: int, année_2: int) -> int:
    total_jours_1ere_date = nbre_jours_debut_ere_jma(jours_1, mois_1, année_1)
    total_jours_2eme_date = nbre_jours_debut_ere_jma(jours_2, mois_2, année_2)

    if total_jours_1ere_date <= total_jours_2eme_date:
        return total_jours_2eme_date - total_jours_1ere_date
    else:
        return total_jours_1ere_date - total_jours_2eme_date
 