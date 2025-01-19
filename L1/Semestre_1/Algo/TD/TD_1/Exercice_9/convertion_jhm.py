#!usr/bin/python3

from Exercice_7.conversion_min_h import heure
from Exercice_8.Jours import jours

def convertion_jhm(minutes:int) -> int:

    tot_heures = heure(minutes)
    tot_jours = jours(tot_heures)
    minutes = minutes % 60

    print("{:d} minutes équivalent à {:d} jours, {:f} heures et {:d} minutes".format(minutes, tot_jours, tot_heures, minutes))

    return tot_jours, tot_heures, minutes