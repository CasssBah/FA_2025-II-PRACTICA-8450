def ejer01():
    edad = int(input("Ingrese una edad: "))

    if edad < 18:
        Print("Menor de edad")
    else:
        if edad >= 18 and edad <= 64:
            print("Adulto")
        else:
            print("Adulto mayor")

def ejer2():
    annio = int(input("Ingrese el año: "))

    if (annio %4 == 0 and annio %100 !=0) or (annio %400==0):
        print ("\nEl año es biciesto")
    else:
        print ("\nEl año no es biciesto")

    if annio %2 ==0:
        print("El año es par")
    else:
        printprint("El año no es par")

def ejer3():
    monto = float(input("Ingrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros")
    opcion =int(input("\nIngrese una opción; "))

    match opcion:
        case 1: print("Dolares: ", round((monto/3.75),0))
        case 2: print(f"Euros: , {monto/4.05:.2f}")
        case _: print("Opción incorrecta")

import math
def ejer04():
    print("Bienvenido al sistema de Cálculos de áreas de figuras geométricas\n")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. círculo")

    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1: 
            lado = int(input("Ingrese un lado: "))
            print("Área: ", lado*lado)
        case 2:
            bse = int(input("Ingrese la base: "))
            alt = int(input("Ingrese la altura: "))
            print("Área rectángulo: ", (bse*alt))
        case 3:
            bse1 = int(input("Ingrese la base: "))
            alt1 = int(input("Ingrese la altura: "))
            print("Área triángulo: ", (bse*alt)/2)
        case 4:
            radio = float(input("Ingrese el radio: "))
            print("Área del círuclo: ", (round(math.pi * radio**2),2))

        case _: print("Opción incorrecta")
ejer04()


