import os
os.system("cls")
from random import *

nombre = input("Ingrese su nombre: ")

print()
print("-----------------------------------------------")
print(f"Hola {nombre}")
print("He pensado un número del 1 al 100")
print("Tienes solo 8 intentos para adivinarlos")
print("-----------------------------------------------")

numero = 0
num = randint(1,100)
opc = 8

while opc > 0:
    print()
    numero = int(input("Ingresa el número: "))
    opc -= 1
    if numero > 100 or numero < 1:
        print("-----------------------------------------------")
        print("Ingresastes un número invalido")
        print("Vuelva a intentarlo")
        print(f"Te quedan {opc} intentos")
        print("-----------------------------------------------")
        print()
    elif numero < num:
        print("-----------------------------------------------")
        print("El número ingresado es menor al número elegido")
        print("Vuelva a intentarlo")
        print()
        print(f"Te quedan {opc} intentos")
        print("-----------------------------------------------")
    elif numero > num:
        print("-----------------------------------------------")
        print("El número ingresado es mayor al número elegido")
        print("Vuelva a intentarlo")
        print(f"Te quedan {opc} intentos")
        print("-----------------------------------------------")
        print()
    elif numero == num:
        print("-----------------------------------------------")
        print(f"El número {numero} es correcto")
        print(f"Lo lograstes en el intento {opc}")
        print(f"¡¡¡      Felicidades {nombre}     !!!")
        print("-----------------------------------------------")
        print()
        break
if numero != num:
    print("-----------------------------------------------")
    print(f"Lo siento, se han agotado los intento")
    print(f"El número secreto era {num}")
    print("-----------------------------------------------")
    print()

