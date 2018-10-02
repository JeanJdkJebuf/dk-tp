######################################################################################
#           Jeu Donkey Kong Labyrinthe
#       Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers le labyrinthe
######################################################################################
#           Script Python
#       Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
######################################################################################


######################################################################################
#importation des modules
######################################################################################
from constantes import *
import classes
import pygame

######################################################################################
#initialisation de pygame
######################################################################################
pygame.init()

######################################################################################
#création de la fenêtre principale
######################################################################################
#dimensions de la fenetre principale, le coté est un carré
fen=pygame.display.set_mode((cote_fenetre,cote_fenetre))
#ajout de l'image principale
icone = pygame.image.load(image_icone).convert()
#on colle l'image principale sur la fenêtre
fen.blit(icone,place_icone)
#nom de la fenetre principale
pygame.display.set_caption(titre_fenetre)
#raffraichissement d'écran pour afficher l'image principale
pygame.display.flip()


######################################################################################
#Boucle
######################################################################################
#boucle principale
while continuer_principale :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            continuer_principale=0
