#!usr/bin/python3

from écart_date import nbre_jours_entre_deux_dates

def main():
    jours_1 = int(input("Nombre de jours pour la première date: "))
    mois_1= int(input("Nombre de mois pour la première date: "))
    année_1 = int(input("Nombre d'année pour la première date: "))
    print()
    jours_2 = int(input("Nombre de jours pour la deuxième date: "))
    mois_2 = int(input("Nombre de mois pour la deuxième date: "))
    année_2 = int(input("Nombre d'année pour la deuxième date: "))

    print(nbre_jours_entre_deux_dates(jours_1, mois_1, année_1, jours_2, mois_2, année_2))

if __name__ == "__main__":
    main()