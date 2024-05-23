from os import *
#Esta función se encargaría de pausar la ejecución del programa
def pausar():
    system("pause")
#se encargaría de limpiar la pantalla de la consola
def limpar_pantalla():
    system("cls")
#imprime el menu al incio del programa y muestra los numeros que ingreso el usuario
def menu(a:int,b:int):
    limpar_pantalla()
    print("    menu de opciones   ")
    print(f"A- ingrese el 1er operando A = {a} ")
    print(f"B- ingrese el 2do operando  B = {b}")
    print("C- eleguir operacion")
    print("D- mostrar resultado")
    print("E- Salir")

    return input("ingrese opcion: ").lower()


#imprime el menu cuando selecciona la case C
def menuOperaciones():
    print("------menu de operaciones-------")
    print("1- sumar")
    print("2- restar ")
    print("3- multiplicar")
    print("4- dividir")
    print("5- factorial")
    return input("ingrese opcion: ").lower()

#suma dos numeros
def sumar(numero1:int, numero2:int):
    return numero1 + numero2

# resta dos numeros
def restar(numero1:int, numero2:int):
    return numero1 - numero2

# hace la multiplicacion de dos numeros
def multiplicar(numero1:int, numero2:int):
    return numero1 * numero2

#divide entre dos numero
def dividir(numero1:int, numero2:int):
    try:
         dividir = numero1 / numero2
        
    except:
        print("no se puede dividir por  0")
        
    return dividir
# fatorea un numero
def factorial(n:int) -> int:
    fact = 1
    for i in range(1, n + 1): 
        fact *= i
    return fact

def factorialDos(n:int) -> int:
    return factorial(n)


# muestra un mensaje y espera que el usuario responda con "s" (sí) o "n" (no).
def pedir_confirmacion(mensaje:str)->bool:
    rta = input(mensaje).lower()
    return rta == "s"