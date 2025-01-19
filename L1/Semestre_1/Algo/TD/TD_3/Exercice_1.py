#!usr/bin/python3

def fact(n):
    """Vérification que l'entrée est un entier positif"""

    if n < 0:
        return "Le nombre doit être un entier positif"
    elif n == 0:
        return 1

    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

#test
print(fact(1))