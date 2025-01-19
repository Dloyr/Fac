# -*- coding: utf-8 -*-

# --- Importations de bibliotheques ---
import pygame
import couleurs
import dessin


def main() :
    '''rien -> rien
    '''
    # --- Initialise Pygame ---
    pygame.init()
    # --- Ouvre la fenetre de l'application ---
    surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("C'est le printemps")
    # --- Initialise l'horloge ---
    horloge = pygame.time.Clock()
    # --- Boucle principale ---
    # Tant que le programme n’est pas termine :
    terminer = False
    scene = dessin.init(surface,600,400,20)
    while not terminer :
        # --- Traite les evenements ---
        # Pour chaque evenement detecte
        for event in pygame.event.get() :
            # Si l'utilisateur a clique sur fermer fenetre
            if event.type == pygame.QUIT :
                terminer = True
            elif event.type == pygame.KEYDOWN :
                dessin.met_a_jour(scene)
        # --- Ajuste la vitesse de la boucle (40 FPS) ---
        horloge.tick(40)
        # Met à jour les objets
        # --- Dessine les objets ---
        dessin.dessine(scene)
        # --- Mise à jour de l'affichage ---
        pygame.display.update()
        
    # --- Termine Pygame ---
    pygame.quit()


if __name__ == "__main__" :
    main()
    
