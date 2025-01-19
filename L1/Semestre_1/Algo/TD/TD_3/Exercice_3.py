#!usr/bin/python3

def somme_carres2(nmb_max1: int, nmb_max2: int) -> int:

    index_1 = 0
    index_2 = 0
    carre = 0

    while index_1 <= nmb_max1 or index_2 <= nmb_max2:
        carre += index_1 * index_2

        index_1 += 1
        index_2 += 1

    return carre - 1

print(somme_carres2(2, 5))