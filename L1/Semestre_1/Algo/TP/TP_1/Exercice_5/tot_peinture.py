#!usr/bin/python3

def qtt_peinture(aire_pièce:float) -> float:
    """Fct pour connaître le nombre de litre de peinture qu'il faut pour repeindre la pièce"""

    qtt = aire_pièce // 10
    around_qtt = int(qtt)

    print("La quantité de peinture nécessaire pour repeindre la pièce est de {:d}L.".format(around_qtt))

    return qtt