import numpy as np
from numpy import random

tablero = np.full((3,3)," ")

def mostrarTablero():
    for x in tablero:
        print(x)
        
def jugadaPC():
    while True:
        fila = random.randint(0,len(tablero))
        columna = random.randint(0,len(tablero))
        if tablero[fila,columna] == " ":
            tablero[fila][columna] = "O"
            break
    if checkVictoria(): 
        print("Gana la maquina")
        return True
    return checkLleno()  

def checkTablero(fila,columna):
    if tablero[fila][columna] != " ":
        print("La casilla está ocupada")
    else:
       tablero[fila][columna] = "X"
    if checkVictoria():
        print("¡¡¡Has ganado!!!")
        return True 
    return checkLleno()

def checkVictoria():
    for i in range(3):
        if tablero[i][0]!= " ":
            if tablero[i][0] == tablero[i][1] == tablero[i][2]: return True
        if tablero[0][i] != " ":
            if tablero[0][i] == tablero[1][i] == tablero[2][i]: return True
    if tablero[1][1] != " ":
        return (tablero[0][0] == tablero[1][1] == tablero[2][2]) or (tablero[2][0] == tablero[1][1] == tablero[0][2])
    return False 

def checkLleno():
    if tablero.__contains__(" "): return False
    print("Fin de la Partida")
    return True    
    
def main():
    print("Bienvenido al Tres en Raya")
    while True:
        mostrarTablero()
        fila = int(input("Elige la fila para colocar una X"))
        columna = int(input("Elige la columna para colocar la X"))
        if checkTablero(fila,columna):
            break
        else:
            jugadaPC()
    mostrarTablero()
    print("Gracias por jugar")

if __name__=="__main__":
    main()