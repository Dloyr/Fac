#!/usr/bin/python3

def nmb_premier(nmb: int)-> True:
    """
    Test si un nombre est premier

    Argument:
        - nmb: nombre à tester

    Retourne : True ou False
    """

    if nmb % 1 == 0 and nmb % nmb == 0:
        return True
    
    return False

print(nmb_premier(6))