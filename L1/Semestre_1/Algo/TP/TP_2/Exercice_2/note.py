#!usr/bin/python3

def mention(note: int | float) -> str:
    """Fct pour donner la mention équivalente à une note"""

    if note < 10:
        return "échec"
    elif note >= 10 and note < 12:
        return "passable"
    elif note >= 12 and note < 15:
        return "assez-bien"
    elif note >= 15 and note < 18:
        return "bien"
    else:
        return "très bien"

