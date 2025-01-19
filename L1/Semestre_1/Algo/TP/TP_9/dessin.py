#!/usr/bin/python3

from pygame import *
from couleur import *

def dessine(surface: tuple[int, int]):
    """
    Fonction qui dessine la scène

        Argument:
            - surface: la taille de la surface d'affichage
    """
    x = 100
    y = 550

    dessine_ciel(surface)
    dessine_soleil(surface)
    dessine_sol(surface)

    for maison in range(6):
        dessine_maisons(surface, x, y)
        x += 300

    x -= 1930
    y -= 250
    dessine_nuages(surface, x, y)

    x += 1100
    dessine_nuages(surface, x, y)

    x -= 500
    y -= 150
    dessine_nuages(surface, x, y)

    x += 1285
    y -= 75
    dessine_nuages(surface, x, y)

def dessine_ciel(surface):
    """
    Fonction qui dessine le ciel

        Argument:
            - surface: la taille de la surface d'affichage
    """
    position = (0, 0, 1920, 1080)

    draw.rect(surface, BLEU, position)

def dessine_soleil(surface):
    """
    Fonction qui dessine le soleil

        Argument:
            - surface: la taille de la surface d'affichage
    """
    position = (1600, 150)
    radius = 60

    draw.circle(surface, JAUNE, position, radius)
    draw.circle(surface, ORANGE, position, 50)

def dessine_sol(surface):
    """
    Fonction qui dessine le sol

        Argument:
            - surface: la taille de la surface d'affichage
    """
    position = (0, 680, 1920, 400)

    draw.rect(surface, VERT, position) #Herbe

    position = (0, 850, 1920, 75)

    draw.rect(surface, GRIS, position) #Chemin

def dessine_maisons(surface, x, y):
    """
    Fonction qui dessine les maisons

        Argument:
            - surface: la taille de la surface d'affichage
            - x: l'abscisse
            - y: l'ordonnée
    """
    longeur = 200
    largeur = 250
    position = (x, y, longeur, largeur)

    draw.rect(surface, VIOLET, position) # murs

    x += 10
    y += 10
    longeur = 75
    largeur = 75
    position = (x, y, longeur, largeur)

    draw.rect(surface, NOIR, position) # fenêtre  gauche de l'étage

    x += 105
    position = (x, y, longeur, largeur)

    draw.rect(surface, NOIR, position) # fenêtre droite de l'étage

    y += 115
    position = (x, y, longeur, largeur)

    draw.rect(surface, JAUNE, position) # fenêtre du rez-de-chaussée

    x -= 66
    radius = 27
    position = (x, y)

    draw.circle(surface, JAUNE, position, radius)#fenetre porte

    x -= 29
    longeur = 56
    largeur = 125
    position = (x, y, longeur, largeur)

    draw.rect(surface, ROUGE, position) #porte

    x += 2
    y += 63
    radius = 5
    position =(x, y)

    draw.circle(surface, NOIR, position, radius)#poignée

    y -= 190
    x -= 22
    vecteurs = [(x, y), (x + 100, y - 100), (x + 200, y)]

    draw.polygon(surface, NOIR, vecteurs) # toit

    x += 20
    y += 250

    for longeur in range(10):
        for largeur in range(10):
            draw.line(surface,GRIS, (x, y), (x + 55, y)) #chemin des maisons
            x += 1
            y += 1

def dessine_nuages(surface, x, y):
    """
    Fonction qui dessine les nuages

        Argument:
            - surface: la taille de la surface d'affichage
            - x: l'abscisse
            - y: l'ordonnée
    """
    draw.ellipse(surface, BLANC, (x, y, 100, 60))  # centre du nuage
    draw.ellipse(surface, BLANC, (x - 40, y + 10, 100, 60))  # partie gauche du nuage
    draw.ellipse(surface, BLANC, (x + 40, y + 10, 100, 60))  # partie droite du nuage



