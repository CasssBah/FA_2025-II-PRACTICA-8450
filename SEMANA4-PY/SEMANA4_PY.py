def menu():
  while True:
      pass
      print("\n1. Ejercicio 1")
      print("2. Ejercicio 2")
      print("3. Ejercicio 3")
      print("4. Ejercicio 4")
      print("5. Salir")
      opcion = int(input("\nIngrese una opción: "))
      match opcion:
        case 1: ejer01()
        case 2: ejer2()
        case 3: ejer3()
        case 4: ejer04()
        case 5: exit()
        case _: print("\nOpción incorrecta")

def ejer01():
    edad = int(input("\nIngrese una edad: "))

    if edad < 18:
        print("\nMenor de edad")
    else:
        if edad >= 18 and edad <= 64:
            print("\nAdulto")
        else:
            print("\nAdulto mayor")

def ejer2():
    annio = int(input("\nIngrese el año: "))

    if (annio %4 == 0 and annio %100 !=0) or (annio %400==0):
        print ("\nEl año es biciesto")
    else:
        print ("\nEl año no es biciesto")

    if annio %2 ==0:
        print("\nEl año es par")
    else:
        print("\nEl año no es par")

def ejer3():
    monto = float(input("\nIngrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros")
    opcion =int(input("\nIngrese una opción; "))

    match opcion:
        case 1: print("\nDolares: ", round((monto/3.75),0))
        case 2: print(f"\nEuros: , {monto/4.05:.2f}")
        case _: print("\nOpción incorrecta")

import math
def ejer04():
    print("Bienvenido al sistema de Cálculos de áreas de figuras geométricas\n")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. círculo")

    opcion = int(input("\nIngrese una opción: "))

    match opcion:
        case 1: 
            lado = int(input("\nIngrese un lado: "))
            print("\nÁrea: ", lado*lado)
        case 2:
            bse = int(input("\nIngrese la base: "))
            alt = int(input("\nIngrese la altura: "))
            print("\nÁrea rectángulo: ", (bse*alt))
        case 3:
            bse1 = int(input("\nIngrese la base: "))
            alt1 = int(input("\nIngrese la altura: "))
            print("\nÁrea triángulo: ", (bse*alt)/2)
        case 4:
            radio = float(input("\nIngrese el radio: "))
            print("\nÁrea del círuclo: ", (round(math.pi * radio**2),2))

        case _: print("\nOpción incorrecta")
menu()

