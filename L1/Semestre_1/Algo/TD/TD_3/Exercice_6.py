#!usr/bin/python3

def somme_chiffres(nombre: int)-> int:
    somme = 0

    while nombre > 0:
        somme += nombre % 10 #Récupère l'unité
        nombre //= 10 #transforme la dizaine en unité

    return somme

print(somme_chiffres(1234))