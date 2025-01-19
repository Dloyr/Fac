#!usr/bin/python3

from conversion_temps import conversion_minutes

def main():
    jours = int(input("Combien de jours souhaitez-vous convertir ? "))
    heures = int(input("Combien d'heures souhaitez-vous convertir ? "))
    minutes = int(input("Combien de minutes souhaitez-vous convertir ? "))

    conversion_minutes(jours, heures, minutes)

if __name__ == "__main__":
    main()
