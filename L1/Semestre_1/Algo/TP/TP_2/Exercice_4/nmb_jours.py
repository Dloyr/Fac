#!usr/bin/python3

def nb_jours_annee(année: int) -> int:
    """Fct pour convertir l'année en nombre de jours"""

    if année % 100 == 0:
        if année % 400 == 0:
            return 366
        else:
            return 365
    elif année % 4 == 0:
        return 366
    else:
        return 365