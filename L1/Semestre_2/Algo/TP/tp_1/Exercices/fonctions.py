#!/usr/bin/python3

from random import randint

catalogue = {}

#EXERCICE 1
#=========================================================================================================================================

# QUESTION 1
def ajout_livre(auteur: str, annee: int, titre: str, prix: float, quantite: str, genre: str, catalogue: dict[str, any])-> dict[str, any]:
    """
    Ajoute un livre au sein du catalogue

    Arguments:
        - auteur: l'auteur
        - annee: l'année du livre
        - titre: le titre
        - prix: le prix
        - quantite: le nombre de livres disponibles
        - genre: le genre du livre
        - catalogue: le catalogue des livres

    Retourne: Le catalogue contenant le nouveau livre
    """
    livre = {
        "Auteur": auteur,
        "Année": annee,
        "Titre": titre,
        "Prix": prix,
        "Quantité": quantite
    }

    if genre not in catalogue:
        catalogue[genre] = {}
    if titre not in catalogue[genre]:
        catalogue[genre][titre] = livre

    return catalogue

# TEST
#==================================================================================
#ajout_livre("Jean-Paul Sartre", 1964, "Les mots", 13.5, 1020, "Roman", catalogue)
#print(catalogue)
#==================================================================================

# QUESTION 2
def estPresent(catalogue: str, titre: str)-> bool:
    """
    Vérifie si un livre est présent au sein du catalogue

    Arguments:
        - catalogue: le catalogue des livres
        - titre: le titre du livre

    Retourne:
        - True: si le livre est présent
        - False: si il ne l'est pas
    """
    for genre in catalogue.keys():
        if titre in catalogue[genre]:
            return True
        else:
            continue

    return False

# TEST
#========================================
#print(estPresent(catalogue, "Les mots"))
#========================================

# QUESTION 3
def afficher_livre(livre: dict[str, any])-> None:
    """
    Affiche le livre (Tout les détails le concernant)

    Argument:
        - livre: le livre à afficher

    Retourne: None
    """
    if estPresent(catalogue, livre):
        for genre in catalogue.keys():
            print(catalogue[genre][livre])
    else:
        print("Le livre n'est pas dans le catalogue.")

# TEST
#==========================
#afficher_livre("Les mots")
#==========================

 # QUESTION 4
def changer_prix(livre: dict[str, str | int], prix: float)-> None:
    """
    Changer le prix d'un livre

    Arguments:
        - livre: le livre à modifier
        - prix: le nouveau prix

    Retourne: None
    """
    for genre in catalogue.keys():
        catalogue[genre][livre]["Prix"] = prix

# TEST
#============================
#changer_prix("Les mots", 10)
#============================

# QUESTION 5
def ajoute_quantite(catalogue: dict[str, str | int], titre: str, qte: int)-> None:
    """
    Modifie la quantité d'un livre présent dans le catalogue

    Arguments:
        - catalogue: le catalogue
        - titre: le titre du livre à modifier
        - qte: la nouvelle quantité de livres

    Retourne: None
    """
    for genre in catalogue.keys():
        catalogue[genre][titre]["Quantité"] = qte

# TESTS
#============================================
#ajoute_quantite(catalogue, "Les mots", 1000)
#afficher_livre("Les mots")
#============================================

# QUESTION 6
def livres_auteur(catalogue: dict[str, str | int], nom_auteur)-> list[str]:
    """
    Liste tout les livres d'un auteur, présent dans le catalogue

    Arguments:
        - catalogue: le catalogue
        - nom_auteur: le nom de l'auteur

    Retourne: une liste des titres des livres 
    """
    liste_livres_auteur = []

    for genre in catalogue.keys():
        for catalogue[genre], informations in catalogue[genre].items():
            if informations["Auteur"] == nom_auteur:
                liste_livres_auteur.append(informations["Titre"])

    if not liste_livres_auteur:
        print("Le catalogue ne comporte pas de livre de cet auteur.")

    return liste_livres_auteur

# TESTS
#=========================================================================
#ajout_livre("Jean-Paul Sartre", 2025, "Test Q6", 5, 100, "TP", catalogue)
#print(livres_auteur(catalogue, "Jean-Paul Sartre"))
#=========================================================================

# QUESTION 7
def livres_annee(catalogue: dict[str, str | int], date: int)-> list[str]:
    """
    Liste tout les livres sortis à une date définie

    Arguments:
        - catalogue: le catalogue
        - date: la date d'éditiond des livres

    Retourne: La liste des livres édités à cette date
    """
    liste_livres_date = []

    for genre in catalogue.keys():
        for catalogue[genre], informations in catalogue[genre].items():
            if informations["Année"] == date:
                liste_livres_date.append(informations["Titre"])

    if not liste_livres_date:
        print("Le catalogue ne comporte pas de livre sortie à cette date.")

    return liste_livres_date

# TEST
#===================================
#print(livres_annee(catalogue, 202))
#===================================

# QUESTION 8
def le_plus_cher(catalogue: dict[str, dict[str, str | int]])-> str:
    """
    Affiche le livre le plus cher du catalogue

    Arguments:
        - catalogue: le catalogue

    Retourne: le titre du livre
    """
    prix = 0
    titre = ""

    for genre in catalogue.keys():
        for catalogue[genre], informations in catalogue[genre].items():
            if informations["Prix"] >= prix:
                prix = informations["Prix"]
                titre = informations["Titre"]

    return titre
# TEST
#==============================
#print(le_plus_cher(catalogue))
#==============================

# QUESTION 9
def genres_litteraires(catalogue: dict[str, dict[str, str | int]], nom_auteur: str)-> list[str]:
    """
    Filtre tout les livres suivant les genres

    Arguments:
        - catalogue: le catalogue
        - nom_auteur: le nom de l'auteur

    Retourne:
        - la liste: Si des livres de l'auteurs sont présents dans le catalogue
        - message d'erreur: Si il n'y a pas de livres
    """
    liste_genre_auteur = []

    for genre in catalogue.keys():
        for catalogue[genre], informations in catalogue[genre].items():
            if informations["Auteur"] == nom_auteur:
                if genre not in liste_genre_auteur:
                    liste_genre_auteur.append(genre)

    if not liste_genre_auteur:
        return "Il n'y a aucun livre de cet auteur dans le catalogue"

    return liste_genre_auteur

# TEST
#=======================================================
#print(genres_litteraires(catalogue, "Jean-PaulSartre"))
#=======================================================

# Question 10

def commande(catalogue: dict[str, dict[str, str | int]], liste_livres: list[str])-> None:
    """
    Permet de commander des livres

    Arguments:
        - catalogue: le catalogue
        - liste_livres: les livres à commander

    Retourne: None
    """
    titre = ""
    s_commande = True

    for genre in catalogue.keys():
        for catalogue[genre], informations in catalogue[genre].items():
            if informations["Titre"] in liste_livres:
                if informations["Quantité"] > 0:
                    informations["Quantité"] -= 1

                if informations["Quantité"] <= 0:
                    titre = informations["Titre"]
                    del catalogue[genre][titre]
                    print("'{}' n'est plus disponible".format(titre))
                    s_commande = False

    if s_commande:
        print("les livres dans la liste ont tous pu être commandé")

# TESTS
#===========================================
#print(catalogue)
#commande(catalogue,["Les mots", "Test Q6"])
#print(catalogue)
#===========================================

# EXERCICE 2
#=====================================================================================================
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

# TESTS
#============================
#liste = ['A', 'B', 'C', 'D']
#print(permuteListe(liste))
#============================

# EXERCICE 3
#=====================================================================================================
from string import ascii_uppercase

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

# EXERCICE 4
#=====================================================================================================
def crypte(txt: str, perm: dict[str, str])-> str:
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

# TESTS
#=======================================
#perm = dictPerm()
#txt = crypte("CECI EST UN TEST", perm)
#print("message crypté: {}".format(txt))
#=======================================

# EXERCICE 5
#=====================================================================================================
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

# TEST
#=======================
#print(invertDict(perm))
#=======================

#EXERCICE 6
#=====================================================================================================
def decrypte(txt: str, perm: dict[str, str])-> str:
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

# TEST
#=========================================================
#print("message décrypté: {}".format(decrypte(txt, perm)))
#=========================================================
