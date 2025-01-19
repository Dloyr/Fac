#!usr/bin/python3

from aire_étoile import etoile_six_branches

def main():
    c_tri_1 = float(input("Quelle est la valeur du coté du premier triangle ? "))
    c_tri_2 = float(input("Quelle est la valeur du coté du deuxième triangle ? "))

    etoile_six_branches(c_tri_1, c_tri_2)

    return 0

if __name__ == "__main__":
    main()