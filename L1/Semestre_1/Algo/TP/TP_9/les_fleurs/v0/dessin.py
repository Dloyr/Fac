# -*- coding: utf-8 -*-

########################################
# dessin.py
# v0
########################################

# --- Importations de bibliotheques ---
import pygame
import couleurs

def dessine(surf) :
    '''surface de dessin -> rien
    '''
    # Efface l'ecran
    surf.fill(couleurs.BLEU_CIEL)
    pygame.draw.rect(surf,couleurs.BEIGE,[0,200,600,200])
    
