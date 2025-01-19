#!usr/bin/python3

from compteur_syra import nb_etapes_syracuse

def main():
    nombre = int(input("Saisir un nombre: "))

    print(nb_etapes_syracuse(nombre))

if __name__ == "__main__":
    main()