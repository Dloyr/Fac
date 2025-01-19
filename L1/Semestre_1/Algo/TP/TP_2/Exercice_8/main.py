#!usr/bin/python3

from debut_ere import nbre_jours_debut_ere

def main():
    année_max = int(input("L'année à convertir: "))

    print(nbre_jours_debut_ere(année_max))

if __name__ == "__main__":
    main()
