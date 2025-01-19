#!usr/bin/python3

def conversion_minutes(jours:int, heures:int, minutes:int) -> int:
    conversion_heures = jours * 24 + heures
    conversion_minutes = conversion_heures * 60 + minutes

    print("Au total, il y a {:d} minutes dans {:d} jours, {:d} heures et {:d} minutes".format(conversion_minutes, jours, heures, minutes))

    return conversion_minutes