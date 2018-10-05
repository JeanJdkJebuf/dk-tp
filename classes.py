######################################################################################
#               classes pour le jeu dklabyrinthe
######################################################################################
from constantes import *
import fonction
import pygame
import json


#classe du personnage (déplacement )
class mouvement(object) :
    "cette classe permet le mouvement de donkey kong"
    def __init__(self,pos=dk_droite,position=(0,0)) :
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
            if  self.position[1]+30>=450 :
                return self.position
            else :
                self.position=(self.position[0],self.position[1]+30,1)
                return self.position
            
        #dk remonte
        if fonction.keypressed(pygame.K_UP, event) :
            if self.position[1]-30<0 :
                return self.position
            else :
                self.position=(self.position[0],self.position[1]-30,2)
                return self.position

        #dk droite
        if fonction.keypressed(pygame.K_RIGHT, event) :
            if self.position[0]+30>=450 :
                return self.position
            else :
                self.position=(self.position[0]+30,self.position[1],3)
                return self.position
        #dk gauche
        if fonction.keypressed(pygame.K_LEFT, event) :
            if self.position[0] == 0 :
                return self.position
            else :
                self.position=(self.position[0]-30,self.position[1],4)
                return self.position
    
#classe qui permet de générer le niveau
class level(object) :
    "cette classe permet de générer un niveau"
    def __init__(self,niveau) :
        #niveau à générer
        self.niveau=niveau
        self.liste=[]

    #Cette fonction retourne la liste de data2.json ( clé correspondante : key )
    def creer_une_liste(self):
        with open(self.niveau) as f:
            data = json.load(f)
            self.liste=data.get("liste")
        

    #cette fonction affiche les murs 
    def affiche(self,fenetre) :
        "cette fonction affiche les murs"
        #images à coller
        dkmur=pygame.image.load(mur).convert_alpha()
        dkarrivee=pygame.image.load(arrivee).convert_alpha()
        dkdepart=pygame.image.load(depart).convert_alpha()
        for ligne in range(len(self.liste)) :
            #pour chaque caractère dans la ligne
            for car in range(len(self.liste[ligne])) :
                #ajout du départ
                if self.liste[ligne][car] == "d" :
                    fenetre.blit(dkdepart,(car*30,ligne*30))
                #ajout de l'arrivée
                if self.liste[ligne][car] == "a" :
                    fenetre.blit(dkarrivee,(car*30,ligne*30))
                #ajout des murs
                if self.liste[ligne][car] == "m" :
                    fenetre.blit(dkmur,(car*30,ligne*30))
