#!/usr/bin/python3

def affiche_menu()-> int:
    """
    Affiche le menu de l'application

    Retourne: Le numéro du mode choisi
    """
    print("1 : Liste des codes disponibles.\n\
2 : Créer un nouveau code.\n\
3 : Crypter un texte.\n\
4 : Décrypter un texte.\n\
0 : Quitter l'application")

    reponse = int(input("Votre choix : "))
    print()

    return reponse
