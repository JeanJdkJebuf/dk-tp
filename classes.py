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
        #position en carrés
        self.carre=[]
    
    #fonction qui récupère la liste de la classe level.murs()
    def recup(self, liste) :
        #récupération des valeurs de la liste dans self.carre
        for x in liste :
            self.carre.append(x)
        

    #permet de faire bouger donkey
    def move(self,event) :
        "mouvement de dk"
        #dk descend
        if fonction.keypressed(pygame.K_DOWN, event) :
            if  self.position[1]+30>=450 :
                return self.position
            if  (self.position[0],self.position[1]+30) in self.carre :
                return self.position
            else :
                self.position=(self.position[0],self.position[1]+30,1)
                return self.position
            
        #dk remonte
        if fonction.keypressed(pygame.K_UP, event) :
            if self.position[1]-30<0 :
                return self.position
            if  (self.position[0],self.position[1]-30) in self.carre :
                return self.position
            else :
                self.position=(self.position[0],self.position[1]-30,2)
                return self.position

        #dk droite
        if fonction.keypressed(pygame.K_RIGHT, event) :
            if self.position[0]+30>=450 :
                return self.position
            if  (self.position[0]+30,self.position[1]) in self.carre :
                return self.position
            else :
                self.position=(self.position[0]+30,self.position[1],3)
                return self.position
        #dk gauche
        if fonction.keypressed(pygame.K_LEFT, event) :
            if self.position[0] == 0 :
                return self.position
            if  (self.position[0]-30,self.position[1]) in self.carre :
                return self.position
            else :
                self.position=(self.position[0]-30,self.position[1],4)
                return self.position
        
    def tourne(self, x):
        #chargement du skin de départ de dk ( droite)
        dkd= pygame.image.load(dk_droite).convert_alpha()
        #chargement du skin de départ de dk ( gauche)
        dkg= pygame.image.load(dk_gauche).convert_alpha()
        #chargement du skin de départ de dk ( haut)
        dkh= pygame.image.load(dk_haut).convert_alpha()
        #chargement du skin de départ de dk ( bas)
        dkb= pygame.image.load(dk_bas).convert_alpha()
        liste=[0,dkb,dkh,dkd,dkg]
        #renvoie le skin à update
        return liste[x]

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

    #fonction renvoie les tuples des murs
    def murs(self):
        #variable locale : murs
        murs=[]
        #conversion de niveau en une liste de tuples
        for ligne in range(len(self.liste)) :
            #pour chaque caractère dans la ligne
            for car in range(len(self.liste[ligne])) :
                #ajout du départ
                if self.liste[ligne][car] == "m" :
                    murs.append((car*30,ligne*30))
        return murs