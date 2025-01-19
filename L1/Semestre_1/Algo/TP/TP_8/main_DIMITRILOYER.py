#!/usr/bin/python3

from Fonctions_tp8_DIMITRILOYER import *

"""
nom: LOYER
prénom: Dimitri
Groupe: L1 Informatique groupe 5-1
"""

def main():
#****VARIABLES****
    ma_cuisine = {}
    mes_courses = {}
    gateau_choc = {"oeufs":4,"sucre":150,"farine":80,"beurre":200,"chocolat":200}
    quatre_quarts = {"oeufs":4,"sucre":250,"farine":250,"beurre":250}
    les_recettes = {"omelette" :{ "oeufs": 4, "lait (en cl)": 5}, "soupe" : {"poireau": 4, "pommes de terre": 2}, "fondant au chocolat" : gateau_choc, "quatre-quarts" : quatre_quarts}
#*****************

    print("==== TESTS DE LA FONCTION DE L'EXERCICE 1 ====")
    ma_cuisine = ajoute_produit(ma_cuisine, 'chocolat', 50)

    print(ma_cuisine)

    ma_cuisine = ajoute_produit(ma_cuisine, 'margarine', 250)
    ma_cuisine = ajoute_produit(ma_cuisine, 'oeufs', 6)

    print(ma_cuisine)

    ma_cuisine = ajoute_produit(ma_cuisine, 'chocolat', 100)

    print(ma_cuisine)

#==================================================================================
    print("\n==== TESTS DE LA FONCTION DE L'EXERCICE 2 ====")
    print(produits_presents(ma_cuisine, ["chocolat","oeufs"]))
    print(produits_presents(ma_cuisine, ["chocolat","oeufs","beurre","sucre"]))

#==================================================================================
    print("\n==== TESTS DE LA FONCTION DE L'EXERCICE 3 ====")
    print(present_en_qte(ma_cuisine, "beurre", 100))
    print(present_en_qte(ma_cuisine, "chocolat", 100))
    print(present_en_qte(ma_cuisine, "oeufs", 8))

#==================================================================================
    print("\n==== TESTS DE LA FONCTION DE L'EXERCICE 4 ====")
    mes_courses = ajoute_produit(mes_courses, "bananes", 5)
    mes_courses = ajoute_produit(mes_courses, "sucre", 800)
    mes_courses = ajoute_produit(mes_courses, "farine", 80)
    ma_cuisine = ranger_les_courses(mes_courses, ma_cuisine)

    print(ma_cuisine)

#==================================================================================
    print("\n==== TESTS DE LA FONCTION DE L'EXERCICE 5 ====")
    print(recette_possible(ma_cuisine, les_recettes["soupe"]))
    print(recette_possible(ma_cuisine, gateau_choc))

#==================================================================================
    print("\n==== TESTS DE LA FONCTION DE L'EXERCICE 6 ====")
    print(les_recettes_possibles({"oeufs":4, "sucre":350, "farine":300,"chocolat":200, "beurre":250}, les_recettes))

#==================================================================================
    print("\n==== TESTS DE LA FONCTION DE L'EXERCICE 7 ====")
    print(courses_pour_recette(ma_cuisine, gateau_choc))
    print(courses_pour_recette(ma_cuisine, les_recettes["soupe"]))

#==================================================================================
    print("\n==== TESTS DE LA FONCTION DE L'EXERCICE 8 ====")
    print(tous_les_ingredients(les_recettes))

#==================================================================================
    print("\n==== TESTS DE LA FONCTION DE L'EXERCICE 9 ====")
    print(toutes_les_courses(ma_cuisine, les_recettes))
    print()

if __name__ == "__main__":
    main()
