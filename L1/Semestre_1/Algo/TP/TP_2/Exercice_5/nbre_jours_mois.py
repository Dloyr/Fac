#!usr/bin/python3
from Exercice_3.annee_bis import annee_bissextile

def nbre_jours_mois(n_mois: int, année: int) -> int:
    """Fct pour connaître le nombre de jours dans un mois suivant l'année"""

    if n_mois == 1 or n_mois == 3 or n_mois == 5 or n_mois == 7 or  n_mois == 8 or n_mois == 10:
            return 31
    elif n_mois == 2:
        if annee_bissextile(année):
            return 29
        else:
            return 28

    else:
        return 30
