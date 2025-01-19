#!usr/bin/python3

from Exercice_3.Math_fct import aire_tri_equi

def etoile_six_branches(c_tri_1:float, c_tri_2:float) -> float:
    aire_tri_1 = aire_tri_equi(c_tri_1)
    aire_tri_2 = aire_tri_equi(c_tri_2)

    aire_etoile = aire_tri_1 + aire_tri_2

    print("L'aire de l'étoile est de {:.1f}.".format(aire_etoile))

    return aire_etoile
