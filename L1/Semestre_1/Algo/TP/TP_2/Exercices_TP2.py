#!usr/bin/python3

a = 6
print("a = 6, a pour type : {}".format(type(a)))
print()
b = a / 4
print("b = a / 4, a pour type : {}".format(type(b)))
print()
nom = "Dupont"
print("nom = 'Dupont', a pour type : {}".format(type(nom)))
print()
cond1 = a < b
print("cond1 = a < b, a pour type : {}".format(type(cond1)))

"""EXERCICE 2--------------------------------------------------------------------------------------------------------------------------"""

def mention(note: int | float) -> str:
    """Fct pour donner la mention équivalente à une note"""

    if note < 10:
        return "échec"
    elif note >= 10 and note < 12:
        return "passable"
    elif note >= 12 and note < 15:
        return "assez-bien"
    elif note >= 15 and note < 18:
        return "bien"
    else:
        return "très bien"

"""EXERCICE 3--------------------------------------------------------------------------------------------------------------------------"""

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

"""EXERCICE 4--------------------------------------------------------------------------------------------------------------------------"""

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

"""EXERCICE 5--------------------------------------------------------------------------------------------------------------------------"""

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

"""EXERCICE 6--------------------------------------------------------------------------------------------------------------------------"""

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

"""EXERCICE 7--------------------------------------------------------------------------------------------------------------------------"""

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

"""EXERCICE 8--------------------------------------------------------------------------------------------------------------------------"""

def nbre_jours_debut_ere(année_max: int) -> int:
    """Calcule le nmb de j passé depuis le début de l'ère chrétienne par rapport à une année"""

    nmb_jours = 0

    for année in range (1, année_max + 1):
        nmb_jours += nb_jours_annee(année)

    return nmb_jours

"""EXERCICE 9--------------------------------------------------------------------------------------------------------------------------"""

def nbre_jours_debut_ere_jma(jours: int, mois_max: int, année_max: int) -> int:
    """Calcule le nmb de j passé depuis le début de l'ère chrétienne  par rapport à une date complète"""

    total_jours = 0
    total_jours += nbre_jours_debut_ere(année_max - 1)

    for mois in range(1, mois_max):
        total_jours += nbre_jours_mois(mois, année_max)

    return total_jours + jours

"""EXERCICE 10--------------------------------------------------------------------------------------------------------------------------"""

def nbre_jours_entre_deux_dates(jours_1: int, mois_1: int, année_1: int, jours_2: int, mois_2: int, année_2: int) -> int:
    """Calcule le nombre de jours entre deux dates"""

    total_jours_1ere_date = nbre_jours_debut_ere_jma(jours_1, mois_1, année_1)
    total_jours_2eme_date = nbre_jours_debut_ere_jma(jours_2, mois_2, année_2)

    if total_jours_1ere_date <= total_jours_2eme_date:
        return total_jours_2eme_date - total_jours_1ere_date
    else:
        return total_jours_1ere_date - total_jours_2eme_date

"""EXERCICE 11--------------------------------------------------------------------------------------------------------------------------"""

def dimanche_pascal(année: int) -> int:
    """Fct pour calculer la date du dimanche pascal suivant l'année"""
    n = année % 19 # cyle de Méton
    c = année // 100 # centaine et rang de l'année
    u = année % 100 # centaine et rang de l'année
    s = c // 4 # siècle bissextile
    t = c % 4 # siècle bissextile
    p = (c + 8) // 25 # cycle de proemptose
    q = (c - p + 1) // 3 # proemptose
    e = (19 * n + c - s - q + 15) // 30 # épacte
    b = u // 4 # année bissextile
    d = u % 4 # année bissextile
    L = (2 * t + 2 * b - e - d + 32) % 7# lettre dominicale
    h = (n + 11 * e + 22 * L) // 451 # correction
    m = (e + L - 7 * h +114) // 31 # mois
    j = (e + L - 7 * h +114) % 31 # jours

    return m, j + 1
