import pygame
from dessin import dessine
import nuages

def init():
    pygame.init()
    surface = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Allers-Retours")
    horloge = pygame.time.Clock()
    scene = {
        "surface": surface,
        "horloge": horloge,
        "dim_fen": (1920, 1080),
        "terminer": False,
        "nuages": nuages.init(4) 
    }
    return scene

def boucle(scene):
    while not scene["terminer"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scene["terminer"] = True
        nuages.met_a_jour(scene["nuages"])
        dessine(scene["surface"], scene)
        pygame.display.update()
        scene["horloge"].tick(60)

def quitte():
    pygame.quit()
