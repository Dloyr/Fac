#!usr/bin/python3

from conversion import taux_conv

def main():
    monnaie_1 = float(input("Entrez le montant de la première monnaie: "))
    monnaie_2 = float(input("Entrez le montant de la deuxième monnaie: "))

    taux_conv(monnaie_1, monnaie_2)

if __name__ == "__main__":
    main()