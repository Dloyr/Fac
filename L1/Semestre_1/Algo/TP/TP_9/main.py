#!/usr/bin/python3

from pygame import init, display, time, event, QUIT, KEYDOWN, K_ESCAPE
from dessin import dessine
def main():
    #Initialise screen
    init()

    fenetre = display.set_mode((1920, 1080))
    horloge = time.Clock()
    actif = True

    display.set_caption("Maisons")

    while actif:
        for process in event.get():
            if process.type == QUIT:
                actif = False
            elif process.type == KEYDOWN:
                if process.key == K_ESCAPE:
                    actif = False
        
        horloge.tick(60)
        dessine(fenetre)
        display.update()

    quit()

if __name__ == "__main__":
    main()