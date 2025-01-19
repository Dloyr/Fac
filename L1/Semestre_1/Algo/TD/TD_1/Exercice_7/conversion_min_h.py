#!usr/bin/python3

def heure(minutes:int) -> int:
    """Convertit des minutes en heures."""
    conversion = minutes / 60
    m = int(conversion)

    print("{:d} minutes équivalent à {:d} heures".format(minutes, m))

    return conversion
