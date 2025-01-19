#!usr/bin/python3

def annee_bissextile(année: int) -> str:
    """Fct pour savoir si une année est bissextile"""

    if année % 100 == 0:
        if année % 400 == 0:
            return True
        else:
            return False
    elif année % 4 == 0:
        return True
    else:
        return False