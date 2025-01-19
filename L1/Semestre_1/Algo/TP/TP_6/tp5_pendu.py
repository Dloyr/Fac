# LOYER Dimitri
# groupe 5
#######################
# importations
#######################

from mots import MOTS
from figures_pendu import FIGURES_PENDU
import random

#######################
# fonctions
#######################
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def choisit_mot(list_words : list)-> list:
    """
    Fonction qui choisit un mot aléatoirement dans une liste donnée

        Argument:
            - list_words = la liste de mot

        Retourne: Le mot choisi aléatoirement dans la liste
    """
    return random.choice(list_words)

def est_dans(char: str, chain: str) -> bool:
    """
    Fonction qui vérifie si le caractère souhaité se trouve dans le mot

        Arguments:
            - char: Le caractère à vérifier
            - chain: Le mot

        Retourne:
            - True: Si le caractère fait parti du mot
            - False: Si le caractère n'en fait pas parti
    """
    if char in chain:
        return True

    return False

def input_lettre(db_char: str) -> str:
    """
    Fonction qui demande au joueur de choisir une lettre pour le pendu

        Arguments:
        - db_char: L'historique des lettres déjà utilisées
        
        Retourne:
            la lettre, si:
                    - Une seule de proposée
                    - C'est une lettre
                    - Elle n'a pas déjà était utilisé
        """

    letter = input("Proposez une lettre: ")

    if len(letter) > 1:
        print("Proposez une seule lettre, s'il vous plaît.")
        return input_lettre(db_char)
    elif letter not in ALPHABET:
        print("{} n'est pas une lettre.".format(letter))
        return input_lettre(db_char)
    elif letter in db_char:
        print("Vous avez déjà proposé cette lettre.")
        return input_lettre(db_char)
    else:
        db_char += letter
        return letter

#=======================ESPACE DESSIN PENDU=======================

def dessine_pendu(n: int):
    """
    Fct qui dessine le pendu correspondant à son numéro
    """

    print(FIGURES_PENDU[n])

def affiche_erreurs(error_str: str):
    """
    Fct qui affiche les mauvaises lettres entrées par le joueur

        Arguments: error_str: la liste des mauvaises lettres
    """
    print("Erreurs :")

    for c in error_str:
        print(c, end=" ")

    print()

def affiche_correctes(good_char: str, secret_word: str):
    """
    Fct qui affiche les bonne lettres trouvé en les plaçants dans le mot à trouver

        Arguments:
            - good_char: le bon caractère qui a été trouvé par le joueur
            - secret_word: le mot que le joueur doit retrouver (pour savoir ou placer la bonne lettre)

        Retourne: le mot dans son état actuel
    """
    actual_word = ""
    
    for char in secret_word:
        if char in good_char:
            actual_word += char + " "
        else:
            actual_word += "_ "
    
    print(actual_word)
    return actual_word

def gagne(word_player: str, secret_word: str)-> bool:
    """
    Fct qui vérifié si le mot composé par le joueur correspond au mot à trouver

        Arguments:
            - word_player: le mot du joueur
            - secret_word: le mot à trouver

        Retourne:
            - True : si les deux correspondent
            - False: si ils ne coresspondent pas
    """
    if word_player == secret_word:
        return True

    return False

#print(gagne("test", "test"))

def main():
    number_pendu = 0
    secret_word = choisit_mot(MOTS)
    error_str =" "
    good_letters = " "
    db_char = " "
    word_player = ""

    print("LE PENDU")

    while number_pendu < 6:
        dessine_pendu(number_pendu)
        affiche_erreurs(error_str)
        word_player = affiche_correctes(good_letters, secret_word)

        if not gagne(word_player.replace(" ", ""), secret_word):
            print()
            letter = input_lettre(db_char)
            db_char += letter

            if est_dans(letter, secret_word):
                good_letters += letter
            else:
                error_str += letter
                number_pendu += 1
        else:
            print("Vous avez gagné !\nLe mot secret était: {}".format(secret_word))
            break

    else:
        dessine_pendu(number_pendu)
        print("Vous avez perdu !\nLe mot secret était: {}".format(secret_word))


if __name__ == "__main__":
    main()