#!usr/bin/python3

from Exercice_12.s_syracuse import suivant_syracuse

def altitude_syracuse(nombre: int)-> int:

    el_syracuse = []

    for index in range(1, nombre + 1):
        el_syracuse.append(suivant_syracuse(index))

    el_syracuse.sort()

    return el_syracuse[-1]
