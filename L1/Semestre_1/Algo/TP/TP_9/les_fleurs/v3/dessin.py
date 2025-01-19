# -*- coding: utf-8 -*-

########################################
# dessin.py
#
########################################

# --- Importations de bibliotheques ---
import pygame
import couleurs
import random
import math
from typing import Any

def init(surf,larg,haut) :
    scene = {}
    scene['surface'] = surf
    scene['larg'] = larg
    scene['haut'] = haut
    scene['fleur'] = creer_une_fleur()
    return scene

def creer_une_fleur() -> dict[str,Any]:
    fleur = {}
    fleur['rayon'] = random.randint(20,40)
    fleur['coords'] = (250,200)
    fleur['nb_petales'] = random.randint(5,10)
    fleur['tige_haut'] = 60
    fleur['tige_epaisseur'] = 6
    les_couleurs = [couleurs.ROSE,couleurs.ROUGE,couleurs.ORANGE,couleurs.BLANC]
    fleur['couleur_petales'] = les_couleurs[random.randint(0,len(les_couleurs)-1)]
    return fleur

def met_a_jour(scene) :
    scene['fleur'] = creer_une_fleur()
    return scene


def dessine(scene) :
    '''surface de dessin, int, int -> rien
    '''
    surf = scene['surface']
    # Efface l'ecran
    surf.fill(couleurs.BLEU_CIEL)
    pygame.draw.rect(surf,couleurs.BEIGE,[0,scene['haut']//2,scene['larg'],scene['haut']])
    # Dessine une fleur
    dessine_fleur(surf,scene['fleur'])


def dessine_fleur(surf,fleur: dict[str,Any]) -> None :
    coords = fleur['coords']
    hauteur_tige = fleur['tige_haut']
    epaisseur_tige = fleur['tige_epaisseur']
    rayon = fleur['rayon']
    # tige de la fleur
    pygame.draw.line(surf,couleurs.VERT,(coords[0]+rayon,coords[1]),(coords[0]+rayon,coords[1]-hauteur_tige),epaisseur_tige)
    # coordonnées du coeur de la fleur
    coeur = (coords[0]+rayon,coords[1] - hauteur_tige - rayon)
    # les pétales
    dessine_les_petales(surf,coeur,rayon,fleur['nb_petales'],fleur['couleur_petales'])
    # coeur de la fleur
    pygame.draw.circle(surf,couleurs.JAUNE,coeur,fleur['rayon'])
    return


def dessine_les_petales(surf,coords: tuple[int,int], rayon: int, nb_petales: int, couleur: tuple[int,int,int]) -> None :
    x0,y0 = coords
    angle = 2*math.pi/nb_petales
    # base : distance entre les deux premiers points du polygone 
    base = math.sqrt((rayon*(1 - math.cos(angle)))**2 + (rayon*math.sin(angle))**2)
    # rayon d'un pétale 
    rayon_petale = base // 2
    for i in range(nb_petales) :
        centre = (x0 + rayon * math.cos((i) * angle), y0 + rayon * math.sin((i)*angle))
        dessine_petale(surf,centre,rayon_petale,couleur)
    return

def dessine_petale(surf,coords :tuple[int,int], rayon :int, couleur :tuple[int,int,int]) -> None :
    pygame.draw.circle(surf,couleur,coords,rayon)
    return
