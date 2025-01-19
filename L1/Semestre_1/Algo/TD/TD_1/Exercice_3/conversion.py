#!usr/bin/python3

def taux_conv(monnaie_1: int | float, monnaie_2: int | float) -> float:
    """Convertir les euros en dollars"""
    taux_conversion = monnaie_2 / monnaie_1

    print("Le taux de conversion est de {:.2f}".format(taux_conversion))

    return taux_conversion