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
    annio = int(input("Ingrese el a�o: "))

    if (annio %4 == 0 and annio %100 !=0) or (annio %400==0):
        print ("\nEl a�o es biciesto")
    else:
        print ("\nEl a�o no es biciesto")

    if annio %2 ==0:
        print("El a�o es par")
    else:
        printprint("El a�o no es par")

def ejer3():
    monto = float(input("Ingrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros")
    opcion =int(input("\nIngrese una opci�n; "))

    match opcion:
        case 1: print("Dolares: ", round((monto/3.75),0))
        case 2: print(f"Euros: , {monto/4.05:.2f}")
        case _: print("Opci�n incorrecta")

import math
def ejer04():
    print("Bienvenido al sistema de C�lculos de �reas de figuras geom�tricas\n")
    print("1. Cuadrado")
    print("2. Rect�ngulo")
    print("3. Tri�ngulo")
    print("4. c�rculo")

    opcion = int(input("Ingrese una opci�n: "))

    match opcion:
        case 1: 
            lado = int(input("Ingrese un lado: "))
            print("�rea: ", lado*lado)
        case 2:
            bse = int(input("Ingrese la base: "))
            alt = int(input("Ingrese la altura: "))
            print("�rea rect�ngulo: ", (bse*alt))
        case 3:
            bse1 = int(input("Ingrese la base: "))
            alt1 = int(input("Ingrese la altura: "))
            print("�rea tri�ngulo: ", (bse*alt)/2)
        case 4:
            radio = float(input("Ingrese el radio: "))
            print("�rea del c�ruclo: ", (round(math.pi * radio**2),2))

        case _: print("Opci�n incorrecta")
ejer04()


