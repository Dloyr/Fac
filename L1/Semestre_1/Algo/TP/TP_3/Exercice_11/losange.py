#!usr/bin/python3

from Exercice_9.tri_iso import triangle_iso_croissant
from Exercice_10.triangle_iso_inverse import triangle_iso_decroissant

def losange(taille: int)-> int:

    triangle_iso_croissant(taille-1)
    triangle_iso_decroissant(taille)

    return