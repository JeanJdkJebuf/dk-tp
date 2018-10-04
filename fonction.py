#importation des modules
import pygame

#création de la fenetre de jeu
def keypressed(touche, event):
    "fonction qui retourne true si l'event correspond"
    return event.type == pygame.KEYDOWN and event.key == touche


#fonction si la touche F1 est pressée
def jeu1() :
    "fonction qui lance la boucle de jeu1"
