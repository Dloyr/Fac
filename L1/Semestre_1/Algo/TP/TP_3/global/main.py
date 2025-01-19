#!usr/bin/python3

from fonction_TP3 import *

def main():
    print("======================EXERCICE 1======================")
    nombre = int(input("Saisir un nombre: "))

    ligne_etoiles(nombre)

    print("======================EXERCICE 2======================")
    côté = int(input("Saisir la taille du côté du carré: "))
nombre = int(input("Saisir un nombre: "))

    print(altitude_syracuse(nombre))

    carre(côté)

    print("======================EXERCICE 3======================")
    longueur = int(input("Saisir la largeur du rectangle: "))
    largeur = int(input("Saisir la longueur du rectangle: "))

    rectangle(longueur, largeur)

    print("======================EXERCICE 4======================")
    taille = int(input("Saisir la taille du triangle : "))

    triangle_rect_bg(taille)

    print("======================EXERCICE 5======================")
    taille = int(input("Saisir la taille du triangle: "))

    triangle_rect_hg(taille)

    print("======================EXERCICE 6======================")
    taille = int(input("Saisir la taille de la ligne: "))

    ligne_blancs(taille)

    print("======================EXERCICE 7======================")
    taille = int(input("Saisir la taille du triangle: "))

    triangle_rect_hd(taille)

    print("======================EXERCICE 8======================")
    taille = int(input("Saisir la taille du triangle: "))

    triangle_rect_bd(taille)

    print("======================EXERCICE 9======================")
    taille = int(input("Saisir la taille du triangle: "))

    triangle_iso_croissant(taille)

    print("======================EXERCICE 10======================")
    taille = int(input("Saisir la taille du triangle: "))

    triangle_iso_decroissant(taille)

    print("======================EXERCICE 11======================")
    taille = int(input("Saisir la taille du triangle: "))

    losange(taille)

    print("======================EXERCICE 12======================")
    nombre = int(input("Choissisez un nombre: "))

    print(suivant_syracuse(nombre))

    print("======================EXERCICE 13======================")
    nombre = int(input("Saisir un nombre: "))

    print(nb_etapes_syracuse(nombre))

    print("======================EXERCICE 14======================")
    nombre = int(input("Saisir un nombre: "))

    print(altitude_syracuse(nombre))

if __name__ == "__main__":
    main()
