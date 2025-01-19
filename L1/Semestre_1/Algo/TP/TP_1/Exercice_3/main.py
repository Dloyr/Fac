#!usr/bin/python3

from Math_fct import *

def main():
    rayon = float(input("Quel est le rayon du cercle ? "))

    aire_cercle(rayon)
    "--------------------------------TEST ELLIPSE--------------------------------"

    print()
    rayon = float(input("Quel est le 1er rayon de l'ellipse ? "))
    rayon_2 = float(input("Quel est le 2ème rayon de l'ellipse ? "))

    aire_ellipse(rayon, rayon_2)
    "--------------------------------TEST TRIANGLE EQUILATERAL--------------------------------"

    print()
    coté = float(input("Quel est la valeur du coté du triangle ? "))

    aire_tri_equi(coté)

    "--------------------------------TEST VOLUME CONE--------------------------------"

    print()
    rayon = float(input("Quel est le rayon du cône ? "))
    hauteur = float(input("Quelle est la hauteur du cône ? "))

    vol_cone(rayon, hauteur)
    "--------------------------------TEST VOLUME SPHERE--------------------------------"

    print()
    rayon = float(input("Quelle est la valeur du rayon de la sphère ? "))

    vol_sphere(rayon)
    "--------------------------------TEST AIRE TRIANGLE ARBITRAIRE--------------------------------"

    print()
    coté_a = float(input("Quelle est la valeur du coté a du triangle arbitraire ? "))
    coté_b = float(input("Quelle est la valeur du coté b du triangle arbitraire ? "))
    c = float(input("Quelle est la valeur de C du triangle arbitraire ? "))

    air_tri_arbitraire(coté_a, coté_b, c)

    return 0

if __name__ == "__main__":
    main()