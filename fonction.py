import pygame
#création de la fenetre de jeu
def keypressed(touche, event):
    "fonction qui retourne true si l'event correspond"
    return event.type == pygame.KEYDOWN and event.key == touche