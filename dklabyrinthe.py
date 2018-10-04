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
import fonction

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

#nom de la fenetre principale
pygame.display.set_caption(titre_fenetre)

#fond d'écran du jeu
ecran = pygame.image.load(fond_ecran).convert()

#chargement du skin de départ de dk ( droite)
dkd= pygame.image.load(dk_droite).convert_alpha()
#chargement du skin de départ de dk ( gauche)
dkg= pygame.image.load(dk_gauche).convert_alpha()
#chargement du skin de départ de dk ( haut)
dkh= pygame.image.load(dk_haut).convert_alpha()
#chargement du skin de départ de dk ( bas)
dkb= pygame.image.load(dk_bas).convert_alpha()

def tourne(x):
        #liste des valeurs à retourner avec 0 valeur nulle
        liste=[0,dkb,dkh,dkd,dkg]
        #renvoie le skin à update
        return liste[x]
######################################################################################
#Boucle
#######################################################################################
#boucle principale
while continuer_principale :
    #on colle l'image principale sur la fenêtre
    fen.blit(icone,place_icone)
    #raffraichissement d'écran pour afficher l'image principale
    pygame.display.flip()
    #raffraichissment de la boucle à 30ms
    pygame.time.Clock().tick(30)

    ################################################################
    #refresh de la position de donkey kong
    dkpos=(posit[0],posit[1],3)
    #chargement de la classe mouvement avec une position de départ
    dk=classes.mouvement(position=dkpos)
    #regard de donkey
    regard=tourne(dkpos[2])

    #évènements
    for event in pygame.event.get() :
        #lancement des niveaux
        if fonction.keypressed(pygame.K_F1, event) or fonction.keypressed(pygame.K_F2, event) :
            #modification de la variable jeu
            game=True
            

        #fonction qui fait quitter le programme    
        if event.type == pygame.QUIT or fonction.keypressed(pygame.K_q , event):
            continuer_principale=0

      
    while game :

        #raffraichissment de la boucle à 30ms
        pygame.time.Clock().tick(30)

        #on colle l'écran de jeu
        fen.blit(ecran, place_icone)

        #coller le skin de donkey à l'écran
        fen.blit(regard, (dkpos[0],dkpos[1]))

        #raffraichissement de l'écran
        pygame.display.flip()

        #évènements une fois dans la boucle
        for event in pygame.event.get() :

            #faire bouger donkey kong
            if event.type == pygame.KEYDOWN :
                #evenements
                if event.key == pygame.K_DOWN or event.key== pygame.K_UP or event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT :
                    #tuple qui remplace les valeurs
                    tupdonkey=dk.move(event)
                    dkpos=(tupdonkey[0],tupdonkey[1])
                    regard=tourne(tupdonkey[2])
            
            
            #pour quitter la boucle
            if fonction.keypressed(pygame.K_q , event) :
                game= False
                