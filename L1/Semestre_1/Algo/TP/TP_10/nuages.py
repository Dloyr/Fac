import pygame
import random

def init(nombre):
    largeur, hauteur = 1920, 1080
    att = {
        "vit": 2,
        "lim": (largeur, hauteur),
        "objs": [(random.randint(0, largeur), random.randint(0, hauteur // 2)) for _ in range(nombre)]
    }
    return att

def dessine(att, surface):
    """
    Fonction qui dessine les nuages sur la surface donnée.

    Arguments :
        - att : Dictionnaire contenant les attributs des nuages.
        - surface : Surface Pygame où dessiner.
    """

    for (x, y) in att["objs"]:
        pygame.draw.ellipse(surface, (244, 254, 254), (x, y, 100, 60))

def met_a_jour(att):
    largeur, _ = att["lim"]
    for i, (x, y) in enumerate(att["objs"]):
        x += att["vit"]
        if x > largeur:
            x = -100  # Recommence à gauche de l'écran
            y = random.randint(0, att["lim"][1] // 2)
        att["objs"][i] = (x, y)
