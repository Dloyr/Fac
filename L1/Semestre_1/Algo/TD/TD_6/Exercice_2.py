#!/usr/bin/python3

""" CORRECTION (LOL)
def plateau (liste:list)-> tuple[any, int]:
    val = liste[0]
    nb = 1
    val_courante = liste[0]
    nb_act = 1

    for i in range(1, len(liste)):
        if liste[i] == val_courante:
            nb_act += 1
            if nb_act > nb:
                nb = nb_act
                val = val_courante
        else:
            nb_act = 1
            val_courante = list[i]

    return (val,nb)        

"""
def plateau(list_nmb: list):
    """
    Identifie le plus long plateau de valeurs identiques dans une liste.

    Arguments :
        - list_nmb : Liste de nombres.

    Retourne :
        - Le plus long plateau sous la forme (valeur, longueur).
    """
    if not list_nmb:
        return None

    max_iteration = (list_nmb[0], 1)
    current_value = list_nmb[0]
    current_length = 1

    for i in range(1, len(list_nmb)):
        if list_nmb[i] == current_value:
            current_length += 1
        else:
            if current_length > max_iteration[1]:
                max_iteration = (current_value, current_length)
            current_value = list_nmb[i]
            current_length = 1

    if current_length > max_iteration[1]:
        max_iteration = (current_value, current_length)

    return max_iteration


print(plateau([1,2,2,1,1,1,1,3,3,2,2,2,2,2,2,3,3,1,1,1,1]))
