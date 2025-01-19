#!usr/bin/python3

from Fct_TP5 import *

def main():
    msg = input("Entrez votre message :\n ")
    mode =input_mode()
    method = input_methode()

    if method == "v" or method == "V":
        word_key = input("Entrez le mot-clé : ")
        if mode == "c" or mode == "C":
            print("Le message chiffré est : {}".format(vigenere(msg, mode, word_key)))
        else:
            print("Le message déchiffré est : {}".format(vigenere(msg, mode, word_key)))

        return vigenere(msg, mode, word_key)

    elif method == "c" or method == "C":
        key = int(input("Entrez la clé de chiffrement : "))
        if mode == "c" or mode == "C":
            print("Le message chiffré est : {}".format(cesar(msg, mode, key)))
        else:
            print("Le message déchiffré est : {}".format(cesar(msg, mode, key)))

        return cesar(msg, mode, key)

if __name__ == "__main__":
    main()
