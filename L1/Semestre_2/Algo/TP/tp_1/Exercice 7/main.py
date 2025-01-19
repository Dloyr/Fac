#!/usr/bin/python3

from menu import affiche_menu
from gestion_codes import afficher_les_codes, ajouter_un_code
from crypteur import crypter_un_texte
from string import ascii_uppercase
from decrypteur import decrypter_un_texte

def main():
    reponse = affiche_menu()
    dict_codes = {}
    txt_formate = ""
    txt_crypte = ""
    txt_decrypte = ""

    while reponse != 0:
        if reponse == 1:
            afficher_les_codes(dict_codes)
            reponse = affiche_menu()
        elif reponse == 2:
            dict_codes.update(ajouter_un_code())
            reponse = affiche_menu()
        elif reponse == 3:
            afficher_les_codes(dict_codes)
            code = input("Nom du code choisi : ")
            txt = input("Texte à crypter : ")

            if code not in dict_codes:
                print("ERREUR: Le code sélectionné n'existe pas")
                code = input("Veuillez en saisir un nouveau : ")
            else:
                crypteur = dict_codes[code]

            for letter in txt:
                if letter not in ascii_uppercase:
                    txt_formate += letter.upper()
                else:
                    txt_formate += letter

            txt_crypte = crypter_un_texte(txt_formate, crypteur)

            print("Le texte crypté est :\n{}".format(txt_crypte))
            print()

            reponse = affiche_menu()
        elif reponse == 4:
            afficher_les_codes(dict_codes)
            nom_code = input("Nom du code à choisir : ")

            if nom_code not in dict_codes:
                print("ERREUR: Le code sélectionné n'existe pas")
                nom_code = input("Veuillez en saisir un nouveau : ")
            else:
                code = dict_codes[nom_code]

            code = dict_codes[nom_code]
            txt_crypte = input("Texte à décrypter : ")
            txt_decrypte = decrypter_un_texte(txt_crypte, code)

            print("Le texte décrypté est :\n{}".format(txt_decrypte))
            print()

            reponse = affiche_menu()
        else:
            reponse = int(input("Votre choix : "))

    print("\nBye")
    return 0

if __name__ == "__main__":
    main()