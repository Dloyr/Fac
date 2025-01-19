#!usr/bin/python3

from nbre_jours_mois import nbre_jours_mois

def main():
    n_mois = int(input("Quelle est le numéro du mois ? "))
    année = int(input("Quelle est l'année ? "))

    print(nbre_jours_mois(n_mois, année))

if __name__ == "__main__":
    main()