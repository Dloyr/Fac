#!usr/bin/python3

from date_paque import dimanche_pascal

def main():
    année = int(input("Rentrez l'année: "))

    print(dimanche_pascal(année))

if __name__ == "__main__":
    main()
