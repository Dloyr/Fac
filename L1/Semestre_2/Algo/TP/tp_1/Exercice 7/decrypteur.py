#!/usr/bin/python3

def invertDict(perm: dict[str, str])-> dict[str, str]:
    """
    Décrypte un alphabet crypté

    Argument:
        - perm: l'alphabet crypté

    Retourne: l'alphabet décrypté
    """
    decrypte_alphabet = {}

    for key, value in perm.items():
        decrypte_alphabet[value] = key

    return decrypte_alphabet

def decrypter_un_texte(txt: str, perm: dict[str, str])-> str:
    """
    Décrypte un texte crypté

    Arguments:
        - txt: le texte crypté
        - perm: l'alphabet décrypté

    Retourne: Le texte décrypté
    """
    decrypte_perm = invertDict(perm)
    decrypte_txt = ''

    for letter in txt:
        if letter in decrypte_perm:
            decrypte_txt += decrypte_perm[letter]
        else:
            decrypte_txt += letter

    return decrypte_txt