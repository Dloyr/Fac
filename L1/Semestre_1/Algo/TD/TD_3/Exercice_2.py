#!usr/bin/python3

def somme_carres(max_nmb: int) -> int:
    nmb = 1
    carre = 0

    for nmb in range( max_nmb + 1):
        carre += nmb * nmb

    return carre

print(somme_carres(10))