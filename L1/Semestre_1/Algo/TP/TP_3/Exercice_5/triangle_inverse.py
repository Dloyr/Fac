#!usr/bin/python3

def triangle_rect_hg(taille: int)-> int:
    """Print un triangle inversé"""

    for y in range(taille, 0, -1):
        print("*" * y)

    return
