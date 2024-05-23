from funciones_cal import *




flag_primero = False
flag_segundo = False
flag_tercero = False
factorial_operacion = False
seguir = "s"

num1 = "X"
num2 = "Y"

while seguir == "s":

    match menu(num1,num2):
        case "a":
            num1 = int(input("ingrese numero: "))
           
            flag_primero = True  
        case "b":            
            if flag_primero:
                num2 = int(input("ingrese numero: "))
                
                flag_segundo = True
            else:
                print("primero ingrese el 1er numero")
        case "c": 
            if flag_segundo:           
                match menuOperaciones():
                    case "1":
                        respuesta = sumar(num1,num2)
                        mensaje = "La suma es:"
                    case "2":
                        respuesta = restar(num1,num2)
                        mensaje = "La resta es:"
                    case "3":
                        respuesta = multiplicar(num1,num2)
                        mensaje = "La multiplicación es:"
                    case "4":
                        respuesta = dividir(num1,num2)
                        mensaje = "La división es:"
                    case "5":
                        respuestaFac= factorial(num1)
                        respuestaFacDos = factorialDos(num2)

                        mensaje = f"El factorial de A:{respuestaFac} y El factorial de B:{respuestaFacDos}"
                        factorial_operacion = True
                    case "6":
                        break
                flag_tercero = True
            elif flag_primero == False:
                print("primero ingrese el 1er numero")
            elif flag_segundo == False:
                print("primero ingrese el 2do numero")
            else:
                flag_primero = False
                flag_segundo = False
        case "d":
            if flag_tercero:
                if factorial_operacion:
                    print(f"{mensaje}")
                else:
                    print(f"{mensaje} {respuesta}")
            elif flag_primero == False:
                print("primero ingrese el 1er numero")
            elif flag_segundo == False:
                print("primero ingrese el 1er y el 2do numero")
            elif flag_tercero == False:
                print("primero eliga una operacion")
            else:
                flag_primero = False
                flag_segundo = False
                flag_tercero = False
                num1 = "X"
                num2 = "Y"      

        case "e":            
            if pedir_confirmacion("quieres salir? s / n: "):
                seguir = "n"
    pausar()

print("fin del programa")  