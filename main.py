import os
import keyboard #pour la gestion de l'entree clavier
from gamecolor import  Gamecolor
import time
from playsound import playsound
from classJoueur import Joueur
from fonctiondejeu import *
fps=9# le nombre d'image par seconde
#lecture_de_la_scene_a_travers_le_fichier_nom.ffscene
scene = getscene('depart.ffscene')
poslayer1=getjoueur1position(scene)
posplayer2=getjoueur2position(scene)
posobstacle=getobstacleposition(scene)
#creation_de_joueur_N°1
player1=Joueur()
player1.position=poslayer1
player1.id=1
player1.attakingrange=4
player1.defendingrange=2
player1.mouvementspeed=1/fps
player1.blokingtime=2/fps
#creation_de_joueur_N°2
player2 = Joueur()
player2.position=posplayer2
player2.id=2
player2.defendingrange=1
player2.attakingrange=3
player2.blokingtime=3/fps
startgame()
os.system('cls')
drawscene(poslayer1,posplayer2,len(scene),player1.score,player2.score)
time.sleep(1)
firstx = poslayer1
firsty = posplayer2
newx=poslayer1
newy=posplayer2
while(True):
    blockP1 = False
    blockP2 = False
    attakP1 = False
    attakP2 = False
    if keyboard.is_pressed('q'):
        newx=moveleftP1(newx, newy,player1.mouvementspeed, len(scene),player1.score,player2.score)
    if keyboard.is_pressed('d'):
        newx=moverightP1(newx, newy, player1.mouvementspeed, len(scene),player1.score,player2.score)
    if keyboard.is_pressed('left arrow'):
        newy=moveleftP2(newx, newy, 3, len(scene),player1.score,player2.score)
    if keyboard.is_pressed('right arrow'):
        newy=moverightP2(newx, newy, 3, len(scene),player1.score,player2.score)
    if keyboard.is_pressed('a'):
        newx=jumpleftP1(newx,newy,fps,len(scene),player1.score,player2.score)
    if keyboard.is_pressed('e'):
        newx=jumprightP1(newx,newy,fps,len(scene),player1.score,player2.score)
    if keyboard.is_pressed('l'):
        newy=jumpleftP2(newx,newy,fps,len(scene),player1.score,player2.score)
    if keyboard.is_pressed('m'):
        newy=jumprightP2(newx,newy,fps,len(scene),player1.score,player2.score)
    if keyboard.is_pressed('z'):
        apponnent = newy-newx
        if player1.attakingrange>= apponnent :
            drawattakP1(newx, newy, len(scene), player1.id, player1.score, player2.score, player1.mouvementspeed)
            time.sleep(1)
            os.system('cls')
            drawscene(newx,newy,len(scene),player1.score,player2.score)
            if keyboard.is_pressed('p'):
                blockP2=True
            if keyboard.is_pressed('o'):
                attakP2=True
            if blockP2==True:
                drawscene(firstx,firsty,len(),player1.score,player2.score)
                newx = firstx
                newy = firsty
            if attakP2==True:
                drawscene(firstx,firsty,len(),player1.score,player2.score)
                newx=firstx
                newy=firsty
            time.sleep(1)
            if attakP2==False & blockP2==False:
                time.sleep(0.4)
                os.system('cls')
                player1.score=player1.score+1
                drawscene(firstx,firsty,len(scene),player1.score,player2.score)
                newx = firstx
                newy = firsty
        else:
            drawsoftattakP1(newx,newy,player1.score,player2.score,len(scene),player1.id,player1.mouvementspeed)
            time.sleep(player1.blokingtime)
            os.system('cls')
            drawscene(newx,newy,len(scene),player1.score,player2.score)
    if keyboard.is_pressed('o'):
        apponnent = newy - newx
        if player2.attakingrange >= apponnent:
            drawattakP2(newx, newy, len(scene), player2.id, player1.score, player2.score, player2.mouvementspeed)
            time.sleep(1)
            os.system('cls')
            drawscene(newx, newy, len(scene), player1.score, player2.score)
            if keyboard.is_pressed('s'):
                blockP1 = True
            if keyboard.is_pressed('z'):
                attakP1 = True
            if blockP1 == True:
                drawscene(firstx, firsty, len(), player1.score, player2.score)
                newx = firstx
                newy = firsty
            if attakP1 == True:
                drawscene(firstx, firsty, len(), player1.score, player2.score)
                newx = firstx
                newy = firsty
            time.sleep(1)
            if attakP1 == False & blockP1 == False:
                time.sleep(player1.blokingtime)
                os.system('cls')
                player2.score = player2.score + 1
                drawscene(firstx, firsty, len(scene), player1.score, player2.score)
                newx = firstx
                newy = firsty

        else:
            drawsoftattakP2(newx, newy, player1.score, player2.score, len(scene), player2.id,player2.mouvementspeed)
            time.sleep(player2.mouvementspeed)
            os.system('cls')
            drawscene(newx, newy, len(scene), player1.score, player2.score)

    if player1.score==3 or player2.score==3:
        gameover()
        break




