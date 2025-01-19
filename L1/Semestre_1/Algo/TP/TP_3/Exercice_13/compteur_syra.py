#!usr/bin/python3

from Exercice_12.s_syracuse import suivant_syracuse

def nb_etapes_syracuse(nombre: int)-> int:
    compteur = 0

    while nombre != 1:
        nombre = suivant_syracuse(nombre)
        compteur += 1

    return compteur


