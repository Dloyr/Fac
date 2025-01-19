#!/usr/bin/python3
from random import randint
from string import ascii_uppercase

# CRÉATION DE CODES
def permuteListe(liste: list[any])-> list[any]:
    """
    Permute les éléments d'une liste

    Arugment:
        - liste: la liste à permuter

    Retourne: La liste  permutée
    """
    temp = ""

    for index in range(len(liste) - 1):
        index_echange = randint(0, len(liste)- 1)
        temp = liste[index_echange]
        liste[index_echange] = liste[index]
        liste[index] = temp

    return liste

def dictPerm()-> dict[str, str]:
    """
    Permute les lettres de l'alphabet

    Retourne: L'alphabet permuté
    """
    liste_alphabet = []
    alphabet_permute = {}
    index = 0

    for lettre in ascii_uppercase:
        liste_alphabet.append(lettre)
        alphabet_permute[lettre] = ""

    permuteListe(liste_alphabet)

    for lettre in alphabet_permute.keys():
        alphabet_permute[lettre] = liste_alphabet[index]
        index += 1

    return alphabet_permute


def ajouter_un_code()-> dict[str, dict[str, str]]:
    """
    Permet d'ajouter un nouveau code d'encryptage dans la base de cryptage

    Retourne: Le nouveau code d'encryptage dans la base de cryptage
    """
    dict_codes = {}
    nom_code = input("Donnez le nom de votre nouveau code : ")
    dict_codes[nom_code] = dictPerm()
    print("Le nouveau code est : {}\n".format(dict_codes[nom_code]))

    return dict_codes

    
    
def afficher_les_codes(dict_codes: dict[str, dict[str, str]])-> None:
    """
    Affiche tout les codes de cryptages présents dans la base de cryptage

    Argument:
        - dict_codes: La base de cryptage

    Retourne: None
    """
    print("\nListe des codes disponibles :")
    
    for key in dict_codes.keys():
        print("{} : {}".format(key, dict_codes[key]))
        print()

    print()