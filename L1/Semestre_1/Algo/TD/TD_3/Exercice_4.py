#!usr/bin/python3

def annee_bissextile(année: int) -> str:
    """Fct pour savoir si une année est bissextile"""

    if année % 100 == 0:
        if année % 400 == 0:
            return True
        else:
            return False
    elif année % 4 == 0:
        return True
    else:
        return False

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

print(nbre_jours_mois_pleins_depuis_1janvier(2, 2020))
