#!/usr/bin/python3

HUMAIN = "X" # Le symbole de l’humain.
ORDI = "O" # Le symbole de l’ordinateur.
VIDE = " " # Le symbole de case vide.
T_PLATEAU = 3 # Taille du plateau de jeu

def init_plateau()-> list:
    plateau = [
        [VIDE, VIDE, VIDE],
        [VIDE, VIDE, VIDE],
        [VIDE, VIDE, VIDE]]

    return plateau

#print(init_plateau())

def print_plateau(plateau: list):
    délimiteur = "|"

    for ligne in range(T_PLATEAU):
        print(délimiteur.join(plateau[ligne]))

        if ligne < T_PLATEAU - 1:
            print("-" * (T_PLATEAU * 2 - 1))

plateau = init_plateau()
"""
print_plateau(plateau)
print()
plateau[0][1] = "X"
plateau[2][2]= "O"
print_plateau(plateau)
"""

def input_humain(plateau: list):
    try:
        x = int(input("Quelle ligne choisissez-vous ? (0 à {}) ".format(T_PLATEAU - 1)))
        y = int(input("Quelle colonne choisissez-vous ? (0 à {}) ".format(T_PLATEAU - 1)))

        if x < 0 or y < 0:
            print("ERREUR n°2: Les valeurs entrées sont négatives.")
            x, y = 0
            input_humain(plateau)
        elif x and y > T_PLATEAU:
            print("ERREUR n°3: Les valeurs entrées sont à l'extérieur du plateau")
            x, y = 0
            input_humain(plateau)
        elif plateau[x][y] != VIDE:
            print("ERREUR n°4: La position correspondante aux valeurs entrées n'est pas vide")
            x, y = 0
            input_humain(plateau)

    except ValueError:
        print("ERREUR n°1: Les valeurs entrées ne sont pas deux entiers")
        input_humain(plateau)

    return (x, y)

print(input_humain(plateau))