#!usr/bin/python3

from liste_fct import numero_jour

def main():

    jours = int(input("Combien y a t'il de jours ? "))
    mois = int(input("Combien y a t'il de mois ? "))
    année = int(input("Combien y a t'il d'années ? "))

    print(numero_jour(jours, mois, année))

if __name__ == "__main__":
    main()
