#!/usr/bin/python3

#EXERCICE 1 =======================================================================

LETTRES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ACCENTS = "àâäèéêëı̂ı̈òôöùûüç"
CHIFFRES = "0123456789"
SYMBOLES = "\",.!?:; \n\t&'\\’@%+-/\\*_()[]{}"
ALPHABET = LETTRES + ACCENTS + CHIFFRES
ALLCHAR = LETTRES + ACCENTS + CHIFFRES + SYMBOLES

#EXERCICE 2 =======================================================================

def input_mode():
    """
    Fct qui permet à l'utilisateur de définir le mode

        Retourne : la commande du mode sélectionné
    """

    mode = input("Voulez-vous chiffrer ou déchiffrer un message (c/d) ? ")

    if mode == "c" or mode == "d" or mode == "C" or mode == "D":
        return mode

    print("Clé invalide !")
    input_mode()


#EXERCICE 3 =======================================================================

def input_cle():
    """
    Fct qui permet à l'utilisateur de définir la clé de chiffrement

        Retourne: la valeur de la clé
    """

    cle = int(input("Entrez la clé de chiffrement (1 - {}) : ".format(len(ALPHABET))))

    if 0 < cle and cle <= len(ALPHABET):
        return cle
    else:
        print("Clé invalide !")
        input_cle()


#EXERCICE 4 =======================================================================

def pos(c: str)-> int:
    """
    Fct qui permet de connaître la position d'un caractère au sein de notre constante
    
        Paramètres:
            - c: la lettre dont on cherche sa position

        Retourne :
            - la position du caractère, si il existe dans la constante
            - (-1) si il ne fait pas parti de la constante
            """

    compteur = 0

    if c in ALLCHAR:
        for caractère in ALLCHAR:
            if caractère != c:
                compteur += 1
            elif caractère == c:
                break
    else:
        return -1

    return compteur

#EXERCICE 5 =======================================================================

def car(n: int)-> str:
    """
    Fct qui permet de trouver le caractère correspondant à la position donnée, au sein de la constante
    
        Argument:
            - n: la position du caractère
    
        Retourne: le caractère
    """

    return ALLCHAR[n]

#EXERCICE 6 =======================================================================

def chiffre_car(c: str, n:int)-> str | int:
    """
    Fct qui permet de remplacer un caractère par un autre par rapport à une valeur de déplacement

        Paramètres:
            - c: le caractère à remplacer
            - n: le nombre de déplacements
            
        Retoune: le nouveau caractère
        """

    char_deb_pos = pos(c)
    new_pos =  (char_deb_pos + n) % len(ALLCHAR)

    return car(new_pos)

#EXERCICE 6 =======================================================================

def cesar(message: str, mode: str, clé: int)-> str:
    """
    Fct qui permet de chiffrer, ou déchiffrer un message en modifiant chaques caractères par rapport à une clé donnée

        Paramètres:
            - message: le message à crypter ou décrypter
            - mode: définit le mode d'utilisation (cryptage ou décryptage)
            - clé: la clé de cryptage, ou de décryptage

        Retourne: le message crypté, ou le message décrypté
    """

    message_crypte = ""
    message_decrypte = ""

    if mode == "c" or mode =="C":
        for char in message:
            message_crypte += chiffre_car(char, clé)

        return message_crypte
    else:
        for char in message:
            new_pos = (pos(char) - clé) % len(ALLCHAR)
            char_decrypte = car(new_pos)
            message_decrypte += char_decrypte

        return message_decrypte

#EXERCICE 7 =======================================================================

def input_methode():
    """
    Fct qui permet à l'utilisateur de choisir si il veut utiliser le code de Cesar ou de Vigenere

        Retourne: la lettre correspondante au code souhaité
    """

    mode = input("Quelle méthode voulez-vous utiliser: Cesar (c) ou Vigenere (v) ? ")

    if mode == "c" or mode == "C" or mode == "v" or mode == "V":
        return mode

    print("Option invalide ! ")
    input_methode()

#EXERCICE 8 =======================================================================

def vigenere(message: str, mode: str, mot_cle: str)-> str:
    """
    Fct qui permet de chiffrer, ou déchiffrer un message en modifiant chaques caractères par rapport à un mot-clé donnée

        Paramètres:
            - message: le message à crypter ou décrypter
            - mode: définit le mode d'utilisation (cryptage ou décryptage)
            - mot-clé: le mot-clé de cryptage, ou de décryptage

        Retourne: le message crypté, ou le message décrypté
    """

    msg_crypte = ""
    msg_decrypte = ""

    if mode == "c" or mode == "C":
        for caractère in message:
            msg_crypte += chiffre_car(caractère, pos(mot_cle))


        return msg_crypte
    else:
        for char in message:
            new_pos = (pos(char) - pos(mot_cle)) % len(ALLCHAR)
            char_decrypte = car(new_pos)
            msg_decrypte += char_decrypte

        return msg_decrypte
