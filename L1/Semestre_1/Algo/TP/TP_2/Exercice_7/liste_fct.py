#!usr/bin/python3

from Exercice_6.nbre_jours_mois_plein import nbre_jours_mois_pleins_depuis_1janvier
from Exercice_3.annee_bis import annee_bissextile

def numero_jour(jours: int, mois: int, année: int) -> int:
    """Fct pour connaître le nombres de jours passées depuis le 1er Janviers, jusqu'à la date souhaitée"""

    mois_pleins = mois - 1
    total_jours = nbre_jours_mois_pleins_depuis_1janvier(mois_pleins, année) + jours + 1

    if annee_bissextile(année):
        total_jours += 1
    else:
        if mois_pleins == 2:
            total_jours += 2
        else:
            total_jours += 1

    return total_jours
