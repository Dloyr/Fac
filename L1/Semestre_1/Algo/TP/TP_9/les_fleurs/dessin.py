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

def init(surf,larg,haut,nb_fleurs) :
    scene = {}
    scene['surface'] = surf
    scene['largeur'] = larg
    scene['hauteur'] = haut
    scene['nb_fleurs'] = nb_fleurs
    scene['les fleurs'] = creer_les_fleurs(larg,haut,nb_fleurs)
    return scene

def creer_les_fleurs(larg,haut,nb_fleurs) :
    les_couleurs = [couleurs.ROSE,couleurs.ROUGE,couleurs.ORANGE,couleurs.BLANC]
    liste_fleurs = []
    for i in range(nb_fleurs) :
        ajoute = False
        couleur_petales = les_couleurs[random.randint(0,len(les_couleurs)-1)]
        rayon = random.randint(20,40)
        x0 = random.randint(0,larg//20)*20
        y0 = random.randint((haut*2//3)//20,(int(haut*0.8))//20)*20 - rayon*2
        position = (x0,y0)
        nb_petales = random.randint(5,10)
        fleur = {'nb_petales' : nb_petales, 'coords': position, 'rayon' : rayon, 'couleur' : couleur_petales}
        for j in range(len(liste_fleurs)) :
            if liste_fleurs[j]['coords'][1] >= fleur['coords'][1] :
                liste_fleurs.insert(j,fleur)
                ajoute = True
        if not ajoute :
            liste_fleurs.append(fleur)
    return liste_fleurs

def met_a_jour(scene) :
    scene['les fleurs'] = creer_les_fleurs(scene['largeur'],scene['hauteur'],scene['nb_fleurs'])
    return scene



def dessine(scene) :
    '''dict : tous les paramètres du décor  -> rien
    '''
    # Efface l'ecran
    surf = scene['surface']
    surf.fill(couleurs.BLEU_CIEL)
    pygame.draw.rect(surf,couleurs.BEIGE,[0,scene['hauteur']*2//3,scene['largeur'],scene['hauteur']])
    # Dessine plusieurs fleurs
    for fleur in scene['les fleurs'] :
        dessine_fleur(surf,fleur)
    

def dessine_fleur(surf,fleur) :
    # tige de la fleur
    coords = fleur['coords']
    rayon = fleur['rayon']
    pygame.draw.line(surf,couleurs.VERT,(coords[0],coords[1]+rayon),(coords[0],coords[1]+rayon*3),6)
    # les pétales
    dessine_les_petales(surf,coords,rayon,fleur['nb_petales'],fleur['couleur'])
    # coeur de la fleur
    pygame.draw.circle(surf,couleurs.JAUNE,coords,rayon)

def dessine_les_petales(surf,coords,rayon,n,coul) :
    x0,y0 = coords
    sinus = []
    lines = []
    angle = 2*math.pi/n
    #base : distance entre (x0,0) et le premier point du polygone (premier point de la boucle for)
    base = math.sqrt((rayon*(1 - math.cos(angle)))**2 + (rayon*math.sin(angle))**2)
    for i in range(n) :
        centre = (x0+rayon*math.cos((i+1)*angle),y0+rayon*math.sin((i+1)*angle))
        dessine_petale(surf,centre,base/2,coul)
    return


def dessine_petale(surf,coords,rayon,coul) :
    pygame.draw.circle(surf,coul,coords,rayon)
    return
