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



######################################################################################
#Boucle
######################################################################################
#boucle principale
while continuer_principale :
    #raffraichissement d'écran pour afficher l'image principale
    pygame.display.flip()
    #raffraichissment de la boucle à 30ms
    pygame.time.Clock().tick(30)
    #Fermeture de la boucle principale
    for event in pygame.event.get() :
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q :
            continuer_principale=0
