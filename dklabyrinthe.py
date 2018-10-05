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
    regard=dk.tourne(dkpos[2])

    #évènements
    for event in pygame.event.get() :
        #lancement des niveaux
        if fonction.keypressed(pygame.K_F1, event) or fonction.keypressed(pygame.K_F2, event) :
            #lancement de l'objet niveau
            if event.key==pygame.K_F1 :
                obj_lev=classes.level("n1.json")
                obj_lev.creer_une_liste()
            
            if event.key==pygame.K_F2 :
                obj_lev=classes.level("n2.json")
                obj_lev.creer_une_liste()
                
            #modification de la variable jeu
            game=True
            #création de la liste pour le mouvement
            #Ajout de la liste de tuples pour les murs
            #pour ainsi instancier les déplacements
            dk.recup(obj_lev.murs())
            

        #fonction qui fait quitter le programme    
        if event.type == pygame.QUIT or fonction.keypressed(pygame.K_q , event):
            continuer_principale=0

      
    while game :

        #raffraichissment de la boucle à 30ms
        pygame.time.Clock().tick(30)

        #on colle l'écran de jeu
        fen.blit(ecran, place_icone)

        #on colle les murs
        obj_lev.affiche(fen)

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
                    #update du tuple liées au skin de donkey
                    dkpos=(tupdonkey[0],tupdonkey[1])
                    #position de donkey update
                    regard=dk.tourne(tupdonkey[2])
            
            
            #revenir au niveau principal
            if fonction.keypressed(pygame.K_q , event) :
                game= False
            
            #si donkey atteinte les bananes, retour au niveau principal
            if dkpos == end :
                game = False
                