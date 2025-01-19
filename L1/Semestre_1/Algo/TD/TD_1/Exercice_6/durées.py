#!usr/bin/python3

from Exercice_5.conversion_temps import conversion_minutes

def difference_durees(j_1:int, h_1:int, m_1:int, j_2:int, h_2:int, m_2:int) -> int:
    tot_minutes_1 = conversion_minutes(j_1, h_1, m_1)
    tot_minutes_2 = conversion_minutes(j_2, h_2, m_2)

    diff_minutes = tot_minutes_1 - tot_minutes_2

    print("La différence de minutes entre les deux durées est de {:d} minutes".format(diff_minutes))

    return diff_minutes
