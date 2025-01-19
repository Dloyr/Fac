#!usr/bin/python3

def ligne_etoiles(number: int) -> int:
    """print a line"""

    for i in range(0, number):
        print("*", end='')

    print()
    return 1
