#!usr/bin/python3

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
