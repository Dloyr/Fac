#!/usr/bin/python3

def crypter_un_texte(txt: str, perm: dict[str, str])-> str:
    """
    Crypte un texte

    Arguments:
        - txt: le texte à crypter
        - perm: le dictionnaire de cryptage

    Retourne: Le texte crypté
    """
    txt_crypte = ""

    for letter in txt:
        if letter in perm:
            txt_crypte += perm[letter]
        else:
            txt_crypte += letter

    return txt_crypte