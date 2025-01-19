#!/usr/bin/python3

from random import randint
helmut = {
    "ptsVie": 100,
    "force": 6,
    "adresse": 75,
    "nbCoups": 3,
    "armure": 30
}

olga = {
    "ptsVie": 98,
    "force": 8,
    "adresse": 90,
    "nbCoups": 2,
    "armure": 35
}

irina = {
    "ptsVie": 100,
    "force": 2,
    "adresse": 55,
    "nbCoups": 2,
    "armure": 20
}

boris = {
    "ptsVie": 100,
    "force": 3,
    "adresse": 30,
    "nbCoups": 3,
    "armure": 15
}

def est_vivant(guerrier: dict[str, int]):
    if guerrier["ptsVie"] > 0:
        return True

    return False

#print(est_vivant(helmut))

def donne_un_coup(guerrier: dict[str, int]):
    reussite = randint(1, 100)
    if not est_vivant(guerrier):
        return 0
    elif reussite <= guerrier["adresse"]:
        return guerrier["force"]

    return 0

#print(donne_un_coup(olga))

def prend_un_coup(guerrier: dict[str, int], coup: int):
    degat = guerrier["force"] * (round(1 - guerrier["armure"] / 100))
    guerrier["ptsVie"] -= degat

#prend_un_coup(helmut, 8)
#print(helmut)

def attaque(guerrier_1: dict[str, int], guerrier_2: dict[str, int]):
    perso_1 = 1
    perso_2 = 2
    tour_du_joueur = 3 - perso_2
    if not est_vivant(guerrier_1):
        return

    if tour_du_joueur == perso_1:
        for coup in range(guerrier_1["nbCoups"]):
            prend_un_coup(guerrier_2, donne_un_coup[guerrier_1])
            if not est_vivant(guerrier_2):
                return
            tour_du_joueur = 3 - perso_1
    elif tour_du_joueur == perso_2:
