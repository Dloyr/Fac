#!usr/bin/python3

def plus_petit_diviseur(nombre: int)-> int:
    """Return le plus petit diviseur"""
    index = 1

    while index < nombre:
        index += 1
        if nombre % index == 0:
            return index
