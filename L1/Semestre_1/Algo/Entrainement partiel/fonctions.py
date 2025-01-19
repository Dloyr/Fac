#!/usr/bin/python3

from math import sqrt
from random import randint
def distance(coord_start: tuple[int, int], coord_end: tuple[int, int])-> float:
    return sqrt((coord_start[0]-coord_end[0])**2+(coord_start[1]-coord_end[1])**2)

print(distance((0,0), (0,1)))


def perimetre(list_coord: list[tuple[int, int]])-> float:
    return distance(list_coord[0], list_coord[1]) ** 2

carre = [(0,0),(0,1),(1,1),(1,0)]
print(perimetre(carre))

def plus_grande_distance(list_coord: list[tuple[int, int]])-> float:
    res = 0
    for i in range(len(list_coord)- 1):
        distance_2_coord = distance(list_coord[i], list_coord[i + 1])
        if distance_2_coord > res:
            res += distance_2_coord

    return res

print(plus_grande_distance(carre))
#EXERCICE 2
def alphabet(texte: str)-> list[str]:
    list_car = []

    for c in texte:
        if c not in list_car:
            list_car.append(c)

    return list_car

#print(alphabet("Dans la plaine rase, sous la nuit sans étoiles, ..."))

#EXERCICE 3
def permute_liste(liste: list[any])-> list[any]:
    new_liste = []
    while len(new_liste) != len(liste):
        alea_nmb = randint(0, len(liste)-1)

        if liste[alea_nmb] not in new_liste:
            new_liste.append(liste[alea_nmb])
        else:
            continue

    return new_liste


l1 = ["A", "B", "C", "D" ]
print(permute_liste(l1))

def dict_perm():
    list_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    list_permute = permute_liste(list_alphabet)
    dict_car = {}
    while len(list_alphabet) != len(dict_car):
        idx_alea = randint(0, len(list_alphabet)-1)

        if list_alphabet[idx_alea] not in dict_car.keys():
            dict_car[list_alphabet[idx_alea]] = list_permute[idx_alea]
        else:
            continue
    
    return dict_car

perm = dict_perm()

#print(perm)

def crypte(txt: str, perm: dict[str, str])-> str:
    crpt_txt =""

    for c in txt:
        if c in perm.keys():
            crpt_txt += perm[c]
        else:
            crpt_txt += c

    return crpt_txt

crpt_txt = crypte("CECI EST UN TEST", perm)
print(crpt_txt)

def invert_dict(perm: dict[str, str])-> dict[str, str]:
    decrypt_dict = {}

    for key, value in perm.items():
        decrypt_dict[value] = key

    return decrypt_dict

#print(invert_dict(perm))

def decrypte(txt: str, perm: dict[str, str])-> str:
    decrypte_dict = invert_dict(perm)

    return crypte(txt, decrypte_dict)

print(decrypte(crpt_txt, perm))