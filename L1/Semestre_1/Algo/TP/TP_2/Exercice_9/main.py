#!usr/bin/python3

from debut_dmy import nbre_jours_debut_ere_jma

def main():
    jours = int(input("Nombre de jours: "))
    mois = int(input("Nombre de jours: "))
    année = int(input("Nombre de jours: "))

    print(nbre_jours_debut_ere_jma(jours, mois, année))

if __name__ == "__main__":
    main()