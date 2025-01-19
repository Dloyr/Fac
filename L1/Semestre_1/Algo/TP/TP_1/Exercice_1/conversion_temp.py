#!usr/bin/python3

def celsius_to_fahr(celsius: float) -> float:
    """Fct pour convertir des celsius en fahreinhet"""

    fahreinhet = celsius * 9/5 + 32

    print("{:.1f}°C équivaut à {:.1f}°F.".format(celsius, fahreinhet))

    return fahreinhet