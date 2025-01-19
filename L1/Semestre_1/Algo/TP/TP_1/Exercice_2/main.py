#!usr/bin/python3

from Air_trapèze import air_trapèze

def main():
    hauteur = float(input("Quelle est la hauteur du trapèze ? "))
    largeur_inf = float(input("Quelle est la largeur_inf du trapèze ? "))
    largeur_sup = float(input("Quelle est la largeur_sup du trapèze ? "))

    air_trapèze(hauteur, largeur_inf, largeur_sup)

    return 0

if __name__ == "__main__":
    main()
