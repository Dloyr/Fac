#!usr/bin/python3

def euro_to_dollars(euro: int | float) -> float:
    dollars = euro * 1.29644

    print("{:.2f} euros is equal to {:.2f} dollars".format(euro, dollars))

    return dollars
