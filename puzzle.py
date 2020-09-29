from PIL import Image
import pygame
from pygame.locals import *
from random import shuffle
import time
#filename=input("entrez le file name de l'image : ")
filename='Edited-11.jpg'
im=Image.open(filename)

"""
            TO DO:

- rajouter tkinter selection image
- bouton reinitialiser
- fermeture auto à la victoire
- nettoyer le code

"""




#im.show()
x,y=im.size

#cas où l'image n'est pas horizontal
if(x<y):
    #rotate
    im.rotate(90)

compteur=1
for i in range(4):
    for j in range(5):
        xP=i*x/4
        yP=j*y/5
        x2P=(i+1)*x/4
        y2P=(j+1)*y/5
        nomDossier='Images/'
        im.crop((xP,yP,x2P,y2P)).save(nomDossier+str(compteur)+'.jpg')
        compteur+=1
        #att: on parcourt d'abord les colonnes et pas les lignes

pygame.init()
ecran = pygame.display.set_mode((1000,600))

ratio=200/x

imageInit=pygame.image.load(filename).convert_alpha()
imageInit=pygame.transform.scale(imageInit,(200,int(ratio*y)))


imgM=[]
size_case=[]
for i in range(1,21):
    tamp=pygame.image.load("Images/"+str(i)+".jpg").convert()
    ratio= 60 / tamp.get_width()
    if size_case==[]:
        size_case=[60,int(tamp.get_height()*ratio)]
    tamp=pygame.transform.scale(tamp,(60,int(tamp.get_height()*ratio)))
    imgM.append((tamp,i))


shuffle(imgM)
#fond = pygame.Surface((1000,600))
#ecran.fill((184,184,184))
#ecran.blit(fond,(0,0))

mat_grille=[[size_case,size_case,size_case,size_case],
            [size_case,size_case,size_case,size_case],
            [size_case,size_case,size_case,size_case],
            [size_case,size_case,size_case,size_case],
            [size_case,size_case,size_case,size_case]
            ]

mat_grilleC=[]

def PlaceImg(idximg,imgM):
    imgplace=0
    for img in imgM:
        if img[1]==idximg:
            imgplace=img[0]
            indice=img[1]
    return imgplace,indice

cx=500-60*2
cy=200
g=10
b=10
l=[]
for ligne in mat_grille:
    for colonne in ligne:
        #ecran.fill(pygame.Color(200,g,b),(cx,cy,size_case[0],size_case[1]))
        g+=10
        b+=10
        l.append([cx,cy])
        cx+=size_case[0]
    cy+=size_case[1]
    cx=500-60*2

def ResetEcran(ecran,l):
    time.sleep(1)
    carrenoir=pygame.Surface((size_case[0],size_case[1]))
    for value in l:
        ecran.blit(carrenoir,(int(value[0]),int(value[1])))


continuer=1
compteur=0
ordrePlace=[]
pygame.display.update()
while True:
    position=[]
    N=len(imgM)
    for i in range(N):
        if i<=9:
            y=50*i+50
            ecran.blit(imgM[i][0],(0,y))
            position.append((imgM[i][1],0,y))
        if i>9:
            x=1000-size_case[0]
            y=50*(i-10)+50
            ecran.blit(imgM[i][0],(x,y))
            position.append((imgM[i][1],x,y))
    ecran.blit(imageInit,(400,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
        if event.type ==MOUSEBUTTONUP and event.button==1:
                x=event.pos[0]
                y=event.pos[1]
                imgselec=0
                print(compteur)
                for i in range(len(position)):
                    if (x<(position[i][1]+size_case[0]) and x>(position[i][1])) and (y<(position[i][2]+size_case[1]) and y>(position[i][2])):
                        imgselec=position[i][0]
                        toplace,indice=PlaceImg(imgselec,imgM)
                        ordrePlace.append(indice)
                        coord=l[compteur]
                        ecran.blit(toplace,(int(coord[0]),int(coord[1])))                       
                        compteur+=1
                        pygame.display.flip()
                if compteur==20:
                    correct=[1,6,11,16,
                            2,7,12,17,
                            3,8,13,18,
                            4,9,14,19,
                            5,10,15,20]
                    print(ordrePlace)
                    if ordrePlace==correct:
                        print("Victoire")
                    elif ordrePlace != correct:
                        ResetEcran(ecran,l)
                        compteur=0
                        pygame.display.flip()
    pygame.display.flip()

                        




