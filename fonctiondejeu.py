import time
import keyboard
import avatar as av
import os
from gamecolor import Gamecolor
from playsound import playsound
def startgame():
    while (True):
        os.system("cls")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("  " * 30 + Gamecolor.j3 + "PRESSE ENTER TO START " + Gamecolor.base)
        time.sleep(0.02)
        if keyboard.is_pressed('enter'):
            playsound('start.wav')
            break


def getscene(filename):
    scene = open(filename, "r")
    firstscene = scene.read()
    dispositionscene = firstscene.split()
    return dispositionscene


def getjoueur1position(scence):
    return scence.index("1")


def getjoueur2position(scene):
    return scene.index("2")


def getobstacleposition(scene):
    return scene.index("X")


def drawscene(x, y, z, score1, score2):
    y = y - x
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)

    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * y + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (y - 2) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (y + 2) + av.ventrep2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (y + 2) + av.ventrep2)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * y + av.bascorpp1)
    # z=z+3
    print(" " * 35 + av.pelouse * z)


def moverightP1(x, y, fps, z,score1, score2):
    newx = x + 1
    dist = y - newx
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    time.sleep(fps)
    os.system('cls')
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * dist + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 2) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 2) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    return (newx)


def moveleftP2(x, y, fps, z,score1, score2):
    newy = y - 1
    dist = newy - x
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    time.sleep(1 / fps)
    os.system('cls')
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * dist + av.headp2)
    if(x==y):
        print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 1) + av.corpposblokp2)
    else:
        print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 2) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 2) + av.ventrep2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 2) + av.ventrep2)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    return (newy)


def moveleftP1(x, y, fps, z,score1, score2):
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    newx = x - 1
    dist = y-newx
    time.sleep(fps)
    os.system('cls')
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * dist + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 2) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 2) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    return (newx)


def moverightP2(x, y, fps, z,score1, score2):
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    newy = y + 1
    dist = newy - x
    time.sleep(0.5)
    os.system('cls')
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * dist + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 2) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 2) + av.ventrep2)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    return (newy)


def jumpleftP2(x, y, fps, z,score1, score2):
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    dist = y - x
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * (x + dist) + av.headp2)
    print(" " * 35 + " " * x + av.headp1 + " " * (dist - 3) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist-2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * dist + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * dist + av.bascorpp1)
    print(" " * 35 + " " * x + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    dist = dist - 1
    print(" " * 35 + " " * (x + dist) + av.headp2)
    print(" " * 35 + " " * x + av.headp1 + " " * (dist - 3) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist-2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * dist + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * dist + av.bascorpp1)
    print(" " * 35 + " " * x + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    dist = dist - 1
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * (dist) + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 3) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist+1) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist+1) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    y = dist + x
    return y


def jumprightP2(x, y, fps, z,score1, score2):
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    dist = y - x
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * (x + dist) + av.headp2)
    print(" " * 35 + " " * x + av.headp1 + " " * (dist - 3) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist-2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * dist + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * dist + av.bascorpp1)
    print(" " * 35 + " " * x + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)

    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    dist = dist + 1

    print(" " * 35 + " " * (x + dist) + av.headp2)
    print(" " * 35 + " " * x + av.headp1 + " " * (dist - 3) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * dist + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * dist + av.bascorpp1)
    print(" " * 35 + " " * x + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    dist = dist + 1
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * (dist) + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 3) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist+1) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist+1) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    y = dist + x
    return y


def jumprightP1(x, y, fps, z,score1, score2):
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    dist = y - x
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 2) + av.headp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist - 1) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 1) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.ventrep1)
    print(" " * 35 + " " * x + "  " + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    dist = dist - 1
    x = x + 1
    print(" " * 35 + " " * x + av.headp1)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 2) + av.headp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist - 1) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 1) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.ventrep1)
    print(" " * 35 + " " * x + "  " + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    dist = dist - 1
    x = x + 1
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * (dist - 1) + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 3) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 1) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist + 1) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    return x


def jumpleftP1(x, y, fps, z,score1, score2):
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    dist = y - x
    time.sleep(1 / fps)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 2) + av.headp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist - 1) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist+1) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.ventrep1)
    print(" " * 35 + " " * x + "  " + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    dist = dist + 1
    x = x - 1
    print(" " * 35 + " " * x + av.headp1)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist - 2) + av.headp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist - 1) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist+1) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.ventrep1)
    print(" " * 35 + " " * x + "  " + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    dist = dist + 1
    x = x - 1
    time.sleep(1 / 2)
    os.system("cls")
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * (dist-1) + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (dist-3) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist+1) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (dist+1) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * dist + av.bascorpp1)
    print(" " * 35 + av.pelouse * z)
    return x + 1



def drawsoftattakP1(x, y, scorep1, scorep2, z, id,fps):
    y = y - x
    x = x
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    time.sleep(fps)
    os.system('cls')
    print(" " * 35 + "__" * affichescore + str(scorep1) + "||" + str(scorep2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * y + av.headp2)
    print(" " * 35 + " " * x + av.corposatakp1 + " " * (y - 2) + av.corpposblokp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (y+2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (y+2) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * y + av.bascorpp1)
    # z=z+3
    print(" " * 35 + av.pelouse * z)
    return 0
def drawsoftattakP2(x, y, scorep1, scorep2, z, id,fps):
    y = y - x
    x = x
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    time.sleep(fps)
    os.system('cls')
    print(" " * 35 + "__" * affichescore + str(scorep1) + "||" + str(scorep2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * y + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (y - 2) + av.corposatakp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (y+2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (y+2) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * y + av.bascorpp1)
    # z=z+3
    print(" " * 35 + av.pelouse * z)
    return 0
def drawattakP1(x, y, z, id, score1, score2, fps):
        if id == 1:
            y = y - x
            x = x
            if z % 2 == 0:
                affichescore = int(z / 2)
            else:
                affichescore = int((z - 1) / 2)
            time.sleep(fps)
            os.system('cls')
            print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" " * 35 + " " * x + av.headp1 + " " * y + av.headp2)
            print(" " * 35 + " " * x + "|__" + " " * (y - 2) + av.corpposblokp2)
            print(" " * 35 + " " * x + av.ventrep1 + " " * (y + 2) + av.ventrep1)
            print(" " * 35 + " " * x + av.ventrep1 + " " * (y + 2) + av.ventrep1)
            print(" " * 35 + " " * x + av.bascorpp1 + " " * y + av.bascorpp1)
            #  z=z+3
            print(" " * 35 + av.pelouse * z)


def drawattakP2(x, y, z, id, score1, score2, fps):
    y = y - x
    if z % 2 == 0:
        affichescore = int(z / 2)
    else:
        affichescore = int((z - 1) / 2)
    time.sleep(0.4)
    os.system('cls')
    print(" " * 35 + "__" * affichescore + str(score1) + "||" + str(score2) + "__" * affichescore)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" " * 35 + " " * x + av.headp1 + " " * y + av.headp2)
    print(" " * 35 + " " * x + av.corpposblokp1 + " " * (y - 2) + av.corposatakp2)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (y + 2) + av.ventrep1)
    print(" " * 35 + " " * x + av.ventrep1 + " " * (y + 2) + av.ventrep1)
    print(" " * 35 + " " * x + av.bascorpp1 + " " * y + av.bascorpp1)
    # z=z+3
    print(" " * 35 + av.pelouse * z)
def gameover():
    for i in range(3):
        os.system("cls")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("  " * 30 + Gamecolor.j3 + " GAME OVER " + Gamecolor.base)
        print("  " * 30 + Gamecolor.j3 + " GAME OVER " + Gamecolor.base)
        print("  " * 30 + Gamecolor.j3 + " GAME OVER " + Gamecolor.base)
        time.sleep(0.02)
    playsound('over.wav')


