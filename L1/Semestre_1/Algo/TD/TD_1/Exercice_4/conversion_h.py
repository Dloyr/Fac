#!usr/bin/python3

def conversion_heures(jours:int ,heures:int) -> int:
    """Convertir les jours en heures et y ajouter les heures"""
    total_heures = jours * 24 + heures

    print("Le total d'heures est de {:d}".format(total_heures))

    return total_heures