import os 

def Menu ():


    os.system("clear")

    print("Menu Principal")
    print("1........facrturar")

    

while True:
    Menu()

    opcionMenu= input()

    if opcionMenu =="1":
        nombre=str()
        apellido=str()
        direccion=str()
        telefono=int()
        cedula=int()
        edad=int()
        print("Digite su Nombre:")
        nombre=input()
        print("Digite su Apellido:")
        apellido=input()
        print("Digite la Direccion de su nomicilio:")
        direccion= input()
        print("Digite su numero de telefonoco:")
        telefono=int(input())
        print("Digite su numeto de indetificacion:")
        cedula=int(input())
        print("Digite su Edad:")
        edad=int(input())
        print("Nombre:",nombre,"apellido:",apellido,"Direccion:",direccion,"Cedula:",cedula,"Edad",edad)
        print("Digite una Opcion del Menu......")
        



