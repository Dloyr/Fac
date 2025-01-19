#!usr/bin/python3

from conversion_h import conversion_heures

def main():
    jours = int(input("Combien de jours souhaitez-vous convertir ? "))
    heures = int(input("Combien d'heures voulez-vous ajouter ? "))

    conversion_heures(jours, heures)

if __name__ == "__main__":
    main()
