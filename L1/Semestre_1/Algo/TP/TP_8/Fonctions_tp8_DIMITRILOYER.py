#!/usr/bin/python3

"""
nom: LOYER
prénom: Dimitri
Groupe: L1 Informatique groupe 5-1
"""

# EXERCICE 1 ===============================================================================
def ajoute_produit(stock: dict, ingredient: str, quantite: int)-> dict:
    """
    Fonction qui ajoute un nouveau ingredient dans les stocks

        Arguments:
            - stock : le dictionnaire dans lequel on va ajouter les nouveaux éléments
            - ingredient: les ingredient a ajouter (la cle)
            - quantite: le quantite a ajouter pour un ingredient (la valeur)

        Retourne: un dictionnaire contenant les nouveaux stocks
    """
    if ingredient in stock:
        stock[ingredient] += quantite
    else:
        stock[ingredient] = quantite

    return stock

# EXERCICE 2 ===============================================================================
def produits_presents(stock: dict, liste_ingredients: list)-> bool:
    """
    Fonction qui verifie si des ingredients sont deja presents dans les stocks

        Arguments:
            - stock: le dictionnaire comportant les stocks
            - liste_ingredients: une liste des ingredients a verifier

        Retourne:
            - True: si l'ingredient est présent
            - False: si l'ingredient ne l'est pas
    """
    for ingredient in liste_ingredients:
        if ingredient in stock:
            continue
        else:
            return False

    return True

# EXERCICE 3 ===============================================================================
def present_en_qte(stock: dict, ingredient: str, quantite: int)-> bool:
    """
    Fonction qui verifie si un ingredient est en quantite suffisante dans les stocks

        Arguments:
        - stock : le dictionnaire comportant les stocks
        - ingredient: l'ingredient a verifier (la cle)
        - quantite: la quantite a avoir (la valeur)

        Retourne:
            - True: si l'ingredient est en quantite suffisante
            - False: si il ne l'est pas
    """
    if ingredient in stock and stock[ingredient] >= quantite:
        return True

    return False

# EXERCICE 4 ===============================================================================
def ranger_les_courses(courses: dict, stock: dict)-> dict:
    """
    Fonction qui ajoute les ingredients des courses au seins des stocks

        Arguments:
            - courses: le dictionnaires comportant les ingredients venant d'etre achetes
            - stock: le dictionnaire comportant les stocks

        Retourne: un dictionnaire comportant les ingredients des courses et des stockes
    """
    if courses.items not in stock:
        nouveau_stock = {**stock, **courses}

    return nouveau_stock

# EXERCICE 5 ===============================================================================
def recette_possible(stock: dict, recettes: dict)-> bool:
    """
    Fonction qui verifie si une recette et faisable avec les stocks actuels

        Arguments:
            - stock: le dictionnaire comportant les stocks
            - recettes: le dictionnaire comportant les recettes

        Retourne:
            - True: si la recette est faisable
            - False: si la recette n'est pas faisable
    """
    for ingredient, quantite in recettes.items():
        if present_en_qte(stock, ingredient, quantite):
            continue
        else:
            return False

    return True

# EXERCICE 6 ===============================================================================
def les_recettes_possibles(stock: dict, recettes: dict)-> list:
    """
    Fonction qui liste toute les recettes possibles suivant les stocks

        Arguments:
            - stock: le dictionnaire comportant les stocks
            - recettes: le dictionnaire comportant les recettes
        
        Retourne: une liste des recettes faisables
    """
    recettes_faisables = []

    for ingredient, quantite in recettes.items():
        if recette_possible(stock, quantite):
            recettes_faisables.append(ingredient)

    return recettes_faisables

# EXERCICE 7 ===============================================================================
def courses_pour_recette(stock: dict, recette: dict)-> dict:
    """
    Fonction pour ajouter les produits manquant d'une recette, a une liste de courses

        Arguments:
            - stock: le dictionnaire comportant les stocks
            - recette: le dictionnaire comportant les ingredients et leurs quantite pour une recette

        Retourne: le dictionnaire de courses, mit a jour
    """
    courses = {}
    for ingredient, quantite in recette.items():
        if ingredient not in stock:
            courses[ingredient] = quantite
        if present_en_qte(stock, ingredient, quantite) == False and ingredient in stock:
            courses[ingredient] = quantite - stock[ingredient]

    return courses

# EXERCICE 8 ===============================================================================
def tous_les_ingredients(dict_recettes: dict)-> dict:
    """
    Fonction qui rassemble tous les ingredients des recettes prevues pour le repas

        Arguments:
            - dict_recettes: le dictionnaire des recettes prevues pour le repas

        Retourne: un dictionnaire contenant tous les ingredients requis pour le repas
    """
    dict_ingredients = {}

    for recette, ingredients in dict_recettes.items():
        for ingredients, quantite in ingredients.items():
            ajoute_produit(dict_ingredients, ingredients, quantite)

    return dict_ingredients

# EXERCICE 9 ===============================================================================
def toutes_les_courses(stock: dict, recettes: dict)-> dict:
    """
    Fonction qui verifie les stock et nous donne la liste des course a faire pour preparer le repas

        Arguments:
            - stock: le dictionnaire comportant les stocks
            - recettes: le dictionnaire comportant les recettes

        Retoune: un dictionnaire comportant la liste des courses a faire
    """
    ingredients_des_recettes = tous_les_ingredients(recettes)

    return courses_pour_recette(stock, ingredients_des_recettes)
