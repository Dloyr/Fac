#!usr/bin/python3

def suivant_syracuse(nombre: int)-> int:
    if nombre % 2 == 0:
        return nombre // 2
    else:
        return 3 * nombre + 1
