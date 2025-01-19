#!usr/bin/python3

from aire_pièce import aire_piece
from tot_peinture import qtt_peinture

def main():
    l_mur_1_2= float(input("Quelle est la largeur du premier et deuxième murs ? "))
    L_mur_1_2 = float(input("Quelle est la longueur du premier et deuxième murs ? "))
    l_mur_3_4 = float(input("Quelle est la largeur du troisième et quatrième murs ? "))
    L_mur_3_4 = float(input("Quelle est la longueur du troisième et quatrième murs ? "))

    aire = aire_piece(l_mur_1_2, L_mur_1_2, l_mur_3_4, L_mur_3_4) 
    qtt_peinture(aire)

    return 0

if __name__ == "__main__":
    main()