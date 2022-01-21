import os
import pathlib
import pandas as pd
from matplotlib.pyplot import barh, show
import matplotlib.pyplot as plt


def plataformas():
    dir = 'archivos/'
    contenido = os.listdir(dir)
    plataformas=[]
    for fichero in contenido:
        with open(dir + fichero, "r") as archivo:
           for linea in archivo:
              #print(linea)
              plataformas.append(linea.split(",")[3])
    #print (plataformas)
    #unique_list = list(dict.fromkeys(plataformas))
    #print(unique_list)
    names = ['PC', 'NintendoSwitch', 'PS5', 'PS4', 'Multi', 'XboxOne', 'XOne', 'Xbox360',
             'PlayStation3', 'GameCube',
             'Dreamcast', 'Nintendo64', 'SNES', 'PlayStation1', 'XboxSeries', 'Android', 'WiiU',
             'NES', '3DS', 'Arcade','GameBoyAdvance', 'Nintendo DS','Xbox']
    count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for p in plataformas:
        if p == 'PC':
            count[0]+=1
        if p == 'Nintendo Switch':
            count[1]+=1
        if p == 'PS5':
            count[2]+=1
        if p == 'PS4' or 'PlayStation 4' or 'PlayStaton 4':
            count[3]+=1
        if p == 'Multi':
            count[4] += 1
        if p == 'Xbox One':
            count[5] += 1
        if p == 'XOne':
            count[6] += 1
        if p == 'Xbox 360':
            count[7] += 1
        if p == 'PlayStation 3':
            count[8]+=1
        if p == 'GameCube':
            count[9]+=1
        if p == 'Dreamcast':
            count[10] += 1
        if p == 'Nintendo 64':
            count[11]+=1
        if p == 'SNES':
            count[12]+=1
        if p == 'PlayStation 1':
            count[13]+=1
        if p == 'Xbox Series':
            count[14] += 1
        if p == 'Android':
            count[15]+=1
        if p == 'Wii U':
            count[16] += 1
        if p == 'NES':
            count[17] += 1
        if p == '3DS':
            count[18] += 1
        if p == 'Arcade':
            count[19] += 1
        if p == 'Game Boy Advance':
            count[20] += 1
        if p == 'Nintendo DS':
            count[21] += 1
        if p == 'Xbox':
            count[22] += 1


    #print(count)
    plt.barh(names, count)
    # plt.show
    return names, count

def grafico():
    plt.barh(plataformas()[0], plataformas()[1])
    plt.show
    return


