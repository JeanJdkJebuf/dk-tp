listes=['d000m0m0mmm0mmm', '0mm000m00000000', '00m0mm00mm0m0m0', '0m00000mmm0m0m0', '00mmmm0mm0m000m', 'm000mm00m0mmm00', 'm0m0mmmm00000mm', 'm0m0m0000mmm0m0', '000mm0mm0m000m0', 'm0mm00000m0mmm0', 'm000mmmm0m0000m', 'mmm0m0000mmm000', 'm000m0mmmmmm00m', 'm0mmm0m00000000', 'm00000mmm0mmmma']

def murs(liste) :
    murs=[]
    for ligne in range(len(liste)) :
        #pour chaque caractère dans la ligne
        for car in range(len(liste[ligne])) :
            #ajout du départ
            if liste[ligne][car] == "m" :
                murs.append((car*30,ligne*30))
    return murs

print(murs(listes))