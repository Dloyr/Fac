#!usr/bin/python3

#EXERCICE 1

def nbre_occ(s: str, c: str) -> int:
    """
    Retourne le nombre d'occurences d'un caractère dans une chaine
        - s: la chaine de caractères
        - c: le caractère à vérifier
    """
    cptr = 0

    for char in s:
        if char == c:
            cptr += 1

    return cptr

#print(nbre_occ("abracadabra", "a"))

#EXERCICE 2

def extrait(ch: str, deb: int, n: int)-> str:
    s_extrait = ""

    for index in range(deb, deb+n):
        if index < len(ch) and deb > 0:
            s_ext += ch[index]
        else:
            return s_extrait

    return s_extrait

#print(extrait("bonjour", 2, 4))

#EXERCICE 3

def premiers(s: str, n: int)-> str:

    s_premiers = ""

    for index in range(0, n):
        if index < len(s):
            s_premiers += s[index]
        else:
            return s_premiers

    return s_premiers

#print(premiers('bonjour', 2))

#EXERCICE 4

def derniers(s: str, n: int)-> str:

    s_derniers = ""

    for index in range(len(s) - n, len(s)):
        s_derniers += s[index]

    return s_derniers

#print(derniers("bonjour", 3))

#EXERCICE 5

def est_valide(mot: str, schema: str)-> bool:
    if len(mot) == len(schema):
        for i in range(0, len(schema)):
            if mot[i] == schema[i] or schema[i] == "?":
                continue
            else:
                return False
    else:
        return False

    return True

#print(est_valide("mmmmhhhhh", "m?m?"))

#EXERCICE 6

def est_prefixe(s_prefixe: str, s: str)-> bool:
    for i in range(len(s_prefixe)):
        if s[i] == s_prefixe[i]:
            continue
        else:
            return False

    return True

#print(est_prefixe("fi", "prefixe"))

#EXERCICE 7

def est_suffixe(s_suffixe: str, s:str)-> bool:
    length = len(s)
    index_s_su = 0

    for index in range(length - len(s_suffixe), len(s)):
        if s[index] == s_suffixe[index_s_su]:
            index_s_su += 1
            continue
        else:
            return False

    return True

#print(est_suffixe("suffixe", "suffixe"))

#EXERCICE 8 fix

def contient_dans_ordre(s_check: str, s:str)-> bool:
    s_extrait = ""
    compteur = 0

    for char_s in s:
        for char_sc in s_check:
            if char_s == char_sc:
                s_extrait += char_s

    for char in range(len(s_extrait)):
        if s_extrait[char] == s_extrait[char - 1]:
            continue

    return s_extrait

#print(contient_dans_ordre("aeiou","blableblibloblublublu"))

#EXERCICE 9

def miroir(s: str)-> str:
    reverse_s = ""
    length_s = len(s) - 1

    while length_s >= 0:
        reverse_s += s[length_s]
        length_s -= 1

    return reverse_s

#print(miroir("machin"))

#EXERCICE 10

def palindrome(s: str)-> bool:

    reverse_s = miroir(s)

    for char in range(len(s)):
        if s[char] == reverse_s[char]:
            continue
        else:
            return False

    return True

#print(palindrome("laval"))

def trie (ch: str)-> str:
    """
    Retourne une version normalisée de la string
        - pas d'espace au début et à la fin
        - pas de symboles
        - pas plus d'un espace à la suite
    """

    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    clean_str = ""
    length_ch = len(ch)

    for i in len(ch):
        if ch[i] in ALPHABET:
            clean_str += ch[i]
        elif ch[1] == " " or ch[length_ch] == " ":
            continue
        elif ch[i] == " " and ch[i + 1] == " ":
            clean_str += " "
        else:
            continue

    return clean_str

print(trie(" test  de l'espace "))
