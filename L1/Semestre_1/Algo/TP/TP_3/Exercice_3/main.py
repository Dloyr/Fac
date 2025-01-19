#!usr/bin/python3

from rectangle import rectangle

def main():
    longueur = int(input("Saisir la largeur: "))
    largeur = int(input("Saisir la longueur: "))

    rectangle(longueur, largeur)

if __name__ == "__main__":
    main()
