######################################################################################
#               classes pour le jeu dklabyrinthe
######################################################################################
import constantes
import fonction
import pygame

#classe du personnage (déplacement )
class mouvement(object) :
    "cette classe permet le mouvement de donkey kong"
    def __init__(self,pos=constantes.dk_droite,position=(0,0)) :
        "les variables de classe"
        #pose de donkey        
        self.pos=pos
        #position
        self.position=position
        #position en carrés ( à compléter )
        #à combiner avec le fichier de niveaux pour voir si déplacement possible ou non )
        #self.carre=carre

    #permet de faire bouger donkey
    def move(self,event) :
        "mouvement de dk"
        #dk descend
        if fonction.keypressed(pygame.K_DOWN, event) :
            self.position=(self.position[0],self.position[1]+30,1)
            return self.position
        #dk remonte
        if fonction.keypressed(pygame.K_UP, event) :
            self.position=(self.position[0],self.position[1]-30,2)
            return self.position
        #dk droite
        if fonction.keypressed(pygame.K_RIGHT, event) :
            self.position=(self.position[0]+30,self.position[1],3)
            return self.position
        #dk gauche
        if fonction.keypressed(pygame.K_LEFT, event) :
            self.position=(self.position[0]-30,self.position[1],4)
            return self.position
    
    #permet de repositionner donkey ( son skin)
    