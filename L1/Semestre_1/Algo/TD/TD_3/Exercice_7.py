#!usr/bin/python3

def nombre_ordonne(nombre: int)-> bool:
    """Vérifie si tout les chiffres sont dans l'ordre croissant"""
    liste_nmb = []

    while nombre > 0:
        liste_nmb.append(nombre % 10) #Récupère l'unité
        nombre //= 10 #transforme la dizaine en unité

    liste_nmb.reverse()

    for index in range(len(liste_nmb)-1):
        if liste_nmb[index] > liste_nmb[index + 1]:
            return False

    return True

print(nombre_ordonne(12234))

"""CORRECTION

        while n // 10 == 0:
            a = n % 10
            n = n // 10
            b = n % 10
            if a < b:
                return False

        return True"""
