#!usr/bin/python3

def jours(heures:int) -> int:
    conv_j = heures / 24
    j = int(conv_j)

    print("{:f} heures représente approximativement {:d} jours".format(heures, j))

    return j