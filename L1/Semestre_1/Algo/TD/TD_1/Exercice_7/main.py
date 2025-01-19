#!/usr/bin/python3

from conversion_min_h import heure

def main():
    minutes = int(input("Combien de minutes souhaitez-vous convertir ? "))

    heure(minutes)

if __name__ == "__main__":
    main()