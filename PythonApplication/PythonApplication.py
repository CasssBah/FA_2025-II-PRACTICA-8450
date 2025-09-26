def menu():
    while True:
      pass
      print("\n1. Ejercicio 1")
      print("2. Ejercicio 2")
      print("3. Ejercicio 3")
      print("4. Ejercicio 4")
      print("5. Ejercicio 5")
      print("6. Salir")
      opcion = int(input("\nIngrese una opción: "))
      match opcion:
        case 1: ejer1()
        case 2: ejer2()
        case 3: ejer3()
        case 4: ejer4()
        case 5: ejer5()
        case 6: exit()
        case _: print("\nOpción incorrecta")

def ejer1(): #creando metodo ejer1
       nombre = input("\nIngrese su nombreP: ")
       carrera = input("\nIngrese su carrera: ")

       print(f"\n{nombre}, bienvenido a FA de {carrera}")

def ejer2():
    print("\"Pablo\"")

def ejer3():

    x = int(input("\nIngrese el valor de  x: "))
    y = int(input("\nIngrese el valor de y: "))

    print("\nSuma: ", (x+y))
    print("\nResta: ", (x-y))
    print("\nMultiplicación: ", (x*y))
    print("\nDivisión: ", (x/y))

import math #importando la librería math
def ejer4(): 
    
    num = float(input("Ingrese un número decimal: "))

    print("\nRaiz 2: ", math.sqrt(num))
    print("\nRedondeado: ", round(num, 0))
    print("\nAl cubo: ", math.pow(num,3))
    print("\nRaiz 3: ", num**(1/3))

def ejer5():

    num = input("\nIngrese número")
    
    entero = int(num)
    deci = float(num)

    print("\nResto: ", (entero%2))
    print("\nDivisión: ", (deci/3))

menu()

