#!usr/bin/python3

from math import *

def aire_cercle(rayon:float) -> float:
    """Fct pour calculer l'aire d'un cercle"""

    aire_c = pi * (rayon ** 2)

    print("L'aire du cercle de rayon {:.1f} est de {:.1f}".format(rayon, aire_c))

    return aire_c

def aire_ellipse(rayon_1:float, rayon_2:float) -> float:
    """Fct pour calculer l'aire d'une ellipse"""

    aire_e = pi * rayon_1 * rayon_2

    print("L'aire de l'ellipse ayant pour premier rayon {:.1f} et pour deuxième rayon {:.1f} et de {:.1f}.".format(rayon_1, rayon_2, aire_e))

    return aire_e

def aire_tri_equi(coté:float) -> float:
    """Fct pour calculer l'air d'un triangle equilatéral"""

    aire_tri = (coté ** 2 * sqrt(3)) / 4

    print("L'aire du triangle ayant pour coté {:.1f} est de {:.1f}.".format(coté, aire_tri))

    return aire_tri

def vol_cone(rayon:float, hauteur:float) -> float:
    """Fct pour calculer le volume d'un cône"""

    volume =  pi * (rayon ** 2) * hauteur / 3

    print("Le volume du cône ayant pour rayon {:.1f} et pour hauteur {:.1f} est de {:.1f}".format(rayon, hauteur, volume))

    return volume

def vol_sphere(rayon:float) -> float:
    """Fct pour calculer le volume d'une sphère"""

    volume = 4 * pi * (rayon ** 3) / 3

    print("Le volume d'une sphère ayant pour rayon {:.1f} est de {:.1f}.".format(rayon, volume))

    return volume

def air_tri_arbitraire(coté_a:float, coté_b:float, C:float) -> float:
    """Calculer l'air d'un triangle arbitraire"""

    aire = 1 / 2 * coté_a * coté_b * sin(C)

    print("L'aire du triangle arbitraire ayant pour coté a {:.1f}, pour coté_b {:.1f} et pour C {:.1f} est de {:.1f}.".format(coté_a, coté_b, C, aire))

    return aire