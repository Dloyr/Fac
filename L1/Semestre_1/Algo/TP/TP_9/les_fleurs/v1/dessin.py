# -*- coding: utf-8 -*-

########################################
# dessin.py
#
########################################

# --- Importations de bibliotheques ---
import pygame
import couleurs
import math

def dessine(surf) :
    '''surface de dessin, int, int -> rien
    '''
    # Efface l'ecran
    surf.fill(couleurs.BLEU_CIEL)
    pygame.draw.rect(surf,couleurs.BEIGE,[0,200,600,400])
    # Dessine une fleur
    dessine_fleur(surf,(250,200))


def dessine_fleur(surf,coords: tuple[int,int]) :
    # les coordonnées représentent le poit d'origine en bas à gauche de la fleur
    # tige de la fleur de hauteur 60 - rayon du coeur de la fleur à 30 - épaisseur de la tige 6
    # dessin de la tige
    pygame.draw.line(surf,couleurs.VERT,(coords[0]+30,coords[1]),(coords[0]+30,coords[1]-60),6)
    # coordonnées du coeur de la fleur
    coeur = (coords[0]+30,coords[1] - 60 - 30)
    # les pétales
    dessine_les_petales(surf,coeur,30)
    # coeur de la fleur
    pygame.draw.circle(surf,couleurs.JAUNE,coeur,30)
    return


def dessine_les_petales(surf,coords: tuple[int,int],rayon: int) :
    ## coords centre du coeur de la fleur
    x0,y0 = coords
    # 8 pétales
    angle = 2*math.pi/8
    # base : distance entre les deux premiers points du polygone 
    base = math.sqrt((rayon*(1 - math.cos(angle)))**2 + (rayon*math.sin(angle))**2)
    # rayon d'un pétale 
    rayon_petale = base // 2
    for i in range(8) :
        # centre du pétale
        centre = (x0 + rayon * math.cos((i) * angle), y0 + rayon * math.sin((i)*angle))
        dessine_petale(surf,centre,rayon_petale)
    return

def dessine_petale(surf,coords,rayon) :
    pygame.draw.circle(surf,couleurs.BLANC,coords,rayon)
    return
