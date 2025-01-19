#!/usr/bin/python3

#EXERCICE 1
def alphabet(mot: str)-> dict[str, int]:
    mot_décomposé = {}

    for lettre in mot:
        if lettre in mot_décomposé:
            mot_décomposé[lettre] += 1
        else:
            mot_décomposé[lettre] = 1

    return mot_décomposé

#print(alphabet("eborcb"))

def anagramme (mot_1: str, mot_2: str)-> bool:
    if mot_1 != mot_2:
        return alphabet(mot_1) == alphabet(mot_2)

#print(anagramme("bbroce", "eborcb"))
#print(anagramme("bbroce", "eborcbg"))

#EXERCICE 2
"""
On s'intéresse à ce qui se passe sous une cheminée :
Il y vit plusieurs enfants (ils ont tous un prénom différent)
Tcheminee = dico(string, string)
à un nom d'enfant , on fait correspondre le cadeau qui lui a été commandé
Exemple:
    {"Boris": "tortinette", "Alice": "rollers", "Elliot": "rape à fromage"}

Le contenue d'une hotte de père Noël :
THotte = dico(string, int)
pour chaque cadeau, sa quantité
L'exmple suivant servira à illustrer la première question:
"""
laHotte = {"rollers": 3, "trottinette": 1, "rape à fromage": 1, "anthologie de poesie francaise": 1}
uneCheminee = {"Borris": "trottinette", "Alice": "rollers", "Elliot": "rape à fromage"}

#Question 1
def donneCadeaux(uneCheminee: dict, laHotte: dict)-> bool:
    for cadeau in uneCheminee.values():
        if cadeau in laHotte.keys():
            laHotte[cadeau] -= 1
            if laHotte[cadeau] == 0:
                del(laHotte[cadeau])
        else:
            return False

    return True

#print(donneCadeaux(uneCheminee, laHotte))
#print(donneCadeaux(uneCheminee, laHotte))

# Question 2
"""
Toutes les cheminées ont une adresse:
TLesCheminees = dico(string, Tcheminee)
La clé est l'adresse de la cheminée, la valeur le dictionnaire qui 
associe à chaque enfant le cadeau qui lui a été commandé.
L'exemple suivant servira a illustrer toutes les fonctions:
"""
leschems = {"5 rue Decrombecque, Lens" : {"Luce": "rollers",
                                          "Suzanne": "anthologie de poesie francaise",
                                          "Marie": "rollers"},
            "12 rue Jean Souvraz, Lens": {"Boris": "trottinette",
                                          "Alice": "rollers",
                                          "Elliot": "rape a fromage"}}

#Question 2
def quelsEnfantsOntPourCadeau(leschems: dict[str, dict[str, str]], cadeau: str)-> list[str]:
    cadeaux = []

    for cheminée in leschems.values():
        for enfant, cad in cheminée.items():
            if cadeau == cad:
                cadeaux.append(enfant)
    return cadeaux

#print(quelsEnfantsOntPourCadeau(leschems, "rollers"))

#Question 3
def constitutionHotte(leschems: dict[str, str])-> dict[str, int]:
    hotte = {}
    for cheminée in leschems.values():
        for enfant, cadeau in cheminée.items():
            if cadeau not in hotte:
                hotte[cadeau] = 1
            else: 
                hotte[cadeau] += 1
    return hotte

#print(constitutionHotte(leschems))
