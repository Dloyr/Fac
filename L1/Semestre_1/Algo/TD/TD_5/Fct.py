#!/usr/bin/python3

def somme(list_int: list)-> int:
    sum = 0

    for i in list_int:
        sum += i

    return sum

#print(somme([1, -2, 12]))

def multiples (l: list, m: int)-> list:
    mul = []

    for number in l:
        if number % m == 0:
            mul.append(number)

    return mul

#print(multiples([2, 67, 34, 25, -63], 2))

def indice(elt: int, l: list) -> int:

    for number in l:
        if elt == number:
            return 1
        

    return -1

#print(indice(67, [2, 67, 34, 67, 25, -63, 67]))
#print(indice(55, [2, 67, 34, 67, 25, -63, 67]))

def indices(elt: int, l: list)-> list:
    i_list = []

    for i in range(len(l)):
        if elt == l[i]:
            i_list.append(i)

    return i_list

#print(indices(67, [2, 67, 34, 67, 25, -63, 67]))
#print(indices(55, [2, 67, 34, 67, 25, -63, 67]))

def maximum(list_int: list)-> int:
    res = 0
    list_int.sort()

    if len(list_int) != 0:
        res = list_int[-1]

    return res

#print(maximum([2, 67, 34, 67, 24, -63, 67]))
#print(maximum([]))

def tous_pairs(list_int: list[int])-> list:
    list_pair = []

    for i in list_int:
        if i % 2 != 0:
            list_pair.append(i + 1)
        else:
            list_pair.append(i)

    return list_pair

#print(tous_pairs([2, 67, 34, 67, 25, -63, 67]))

#Exercice 7

NB_ETAGES = 11
TAILLE_SOLUTION = 13
BOUTONS_ASCENCEURS = [2, 3, 5, -4, -11]

def commence_et_se_termine_par_0(list_sol: list[int])-> bool:
    if list_sol[0] == 0 and list_sol[-1] == 0:
        return True
    else:
        return False

#print(commence_et_se_termine_par_0([0, 5, 1, 3, 8, 10, 6, 2, 4, 7, 9, 11, 0]))
#print(commence_et_se_termine_par_0([2, 5, 1, 3, 8, 10, 6, 2, 4, 7, 9, 11, 0]))
#print(commence_et_se_termine_par_0([0, 5, 1, 3, 8, 10, 6, 2, 4, 7, 9, 11, 3]))

def est_dans_batiment(list_sol: list[int])-> bool:
    for etage in list_sol:
        if etage >= 0 and etage <= NB_ETAGES:
            continue
        else:
            return False

    return True

#print(est_dans_batiment([0, 5, 1, 3, 8, 10, 6, 2, 4, 7, 9, 11, 0]))
#print(est_dans_batiment([0, 5, 1, 3, 8, 23, 6, 2, 4, 7, 9, 11, 0]))

def etage_tous_visites(list_sol: list[int])-> bool:
    for i in range(0,NB_ETAGES):
        if i in list_sol:
            continue
        else:
            return False
        
    return True

print(est_dans_batiment([0, 5, 1, 3, 8, 10, 6, 2, 4, 7, 9, 11, 0]))
print(est_dans_batiment([0, 5, 1, 3, 8, 10, 6, 2, 4, 7, 9, 0]))
