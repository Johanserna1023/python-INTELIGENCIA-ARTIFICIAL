
#----IMPORTAR BIBLOTECA------
import time
import random
import os

#-----INICIO DEL JUEGO /SELECCION DE FICHA------

def inicio_juego():
    print("*****BIENVENIDO*******")
    time.sleep(1)
    while True:
        ficha = input("Seleccione Ficha : X / O\n")
        ficha = ficha.upper()
        if ficha=="X":
            humano = "X"
            ordenador = "O"
            break
        elif ficha=="O":
            humano = "O"
            ordenador = "X"
            break
        else:
            print("Por Favor, intruduce una ficha posible. ")
    return(humano,ordenador)


#-------CREACION DE TABLERO-----------

def tablero ():
    print("TRES EN RAYA / TIC TAC TOE")
    print()
    print("        |        |        ")
    print("1  {}     |2 {}    |3 {}     ".format(matriz[0],matriz[1],matriz[2]))
    print("        |        |        ")
    print("------------------------")
    print("        |        |        ")
    print("4  {}     |5 {}   |6 {}     ".format(matriz[3],matriz[4],matriz[5]))
    print("        |        |        ")
    print("-----------------------")
    print("        |        |        ")
    print("7  {}     |8 {}    |9 {}     ".format(matriz[6],matriz[7],matriz[8]))
    print("        |        |        ")

#------DEFINIR FINALES DE PARTIDA-------------
def empate(matriz):
    empate= True
    i = 0 
    while(empate== True and i<9):
        if matriz[i]== "":
            empate = False
        i= i+1
    return empate

def victoria (matriz):
    if (matriz[0]==matriz[1]==matriz[2]!=""or matriz[3]==matriz[4]==matriz[5]!=""or  matriz[6]==matriz[7]==matriz[8]!="" 
     or matriz[0]==matriz[3]==matriz[6]!="" or matriz[1]==matriz[4]==matriz[7]!=""or matriz[2]==matriz[5]==matriz[8]!=""or
        matriz[0]==matriz[4]==matriz[8]!=""or matriz[2]==matriz[4]==matriz[6]!= ""):
        return True
    else:
        return False


#----- MOVIMOENTOS--------HUMANO

def moviento_jugador():
    while True:
        posiciones = [0,1,2,3,4,5,6,7,8]
        casilla = int (input("Seleccione la Casilla:"))
        if casilla not in posiciones:
            print("Casilla no disponible")

        else:
            if matriz [casilla-1]=="":
                matriz [casilla-1]== humano
                break
            else:
                print("Casilla no disponible")

#-------MOVIMIENTOS ORDENADOR--------

def movimiento_ordenador():
    posicion =[0,1,2,3,4,5,6,7,8]
    casilla= 9
    parar = False

#------- ESTE ES EL CICLO FOR-------- 
    for i in posicion:
        copia= list(matriz)
        if copia[i]=="":
            copia[i]== ordenador
            if victoria(copia)==True:
                casilla= i

    if casilla==9:
        for j in posicion:
            if copia[j]=="":
                copia[j]== humano
            if victoria(copia)== True:
                casilla = j 

#-----ESTE ES EL CICLO WHILE------
    if casilla== 9 :
        while( not parar):
            casilla=random.randint(0, 8)
            if matriz[casilla]=="":
                parar=True
    matriz [casilla]= ordenador

#-------DESARROLLO DE LA PARTIDA------------

while True:

    matriz = [""]*9
    os.system("cls") # limpiar la pantalla al comenzar
    humano,ordenador = inicio_juego()
    partida = True
    ganador = 0

    while partida:
        ganador=ganador+1
        os.system("cls")
        tablero()

        if victoria(matriz):
            if ganador%2==0:
                print("**Gana el Juego***")
                print("****Fin del Juego**")
                print("\nReiniciando.....")
                time.sleep(5)
                partida=False
            else:
                print("**Gana el ordenador***")
                print("****Fin del Juego**")
                print("\nReiniciando.....")
                time.sleep(5)
                partida=False
        elif empate(matriz):
            print("**Empate***")
            print("****Fin del Juego**")
            print("\nReiniciando.....")
            time.sleep(5)
            partida=False

        elif ganador%2==0:
            print("El ordenador esta pensando")
            time.sleep(2)
            movimiento_ordenador()

        else:
             moviento_jugador()


