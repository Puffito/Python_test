import numpy as np
from numpy import random

filas = 4
columnas = 5

def crearTablero(filas, columnas):
    
    tablero = np.full((filas, columnas),"0")
    tablero[random.randint(filas)][random.randint(columnas)] = "G"
    correcto = False
    
    while not correcto:
        filaMina = random.randint(filas)
        columnaMina = random.randint(columnas)
        if tablero[filaMina][columnaMina] == "0":
            tablero[filaMina][columnaMina] = "*"
            correcto = True        
    return tablero

def detectarMina(tablero, fila, columna):
    for x in range(-1,2):
        for y in range(-1,2):
            if (fila+x >= 0 and fila+x <= len(tablero)) and (columna+y >= 0 and columna+y < len(tablero[0])):
                if tablero[fila+x][columna+y] == "*":
                    print("¡Cuidado con la mina!")

tableroReal = crearTablero(filas,columnas)
tableroJugador = np.full((filas, columnas),"0")
finPartida = False

while not finPartida:
    print("Adivina en que coordenada está el tesoro, cuidado con la mina")
    filaEscogida = int(input("Introduce la fila (máx.4)"))
    columnaEscogida = int(input("Introduce la columna (máx.5)"))
    casilla = tableroReal[filaEscogida-1][columnaEscogida-1]
    if casilla == "G":
        print("¡¡¡Has encontrado el oro!!!")
        tableroJugador[filaEscogida-1][columnaEscogida-1] = "G"
        finPartida = True
    elif casilla == "*":
        print("BOOM!!! \nMoriches...")
        tableroJugador[filaEscogida-1][columnaEscogida-1] = "*"
        finPartida = True
    else :
        print("Solo hay agua...")
        tableroJugador[filaEscogida-1][columnaEscogida-1] = "X"
        detectarMina(tableroReal,filaEscogida-1,columnaEscogida-1)
    print(tableroJugador)