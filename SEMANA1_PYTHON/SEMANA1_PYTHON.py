def ejer1():
    nombre = input("Introduzca su nombreP: ")
    carrera = input("Ingrese su carrera: ")

    print (f"\n{nombre}, Bienvenido al curso de Fundamentos de Algoritmos de {carrera}")

ejer1()

def ejer2():

    print("\"Jeremy\"")

ejer2()

def ejer3():
    x = int(input("Ingrese el valor de x: "))
    y = int(input("Ingrese el valor de y: "))

    print ("Suma: ", (x+y))
    print ("Resta: ", (x-y))
    print ("Multiplicación: ", (x*y))
    print ("División: ", (x/y))

ejer3()

import math #Importar libreria math

def ejer4():
    num = float(input("Ingrese un número decimal: "))

    print("Raiz 2: ", math.sqrt(num))
    print("Redondeado: ", round(num,0))
    print("Cubo: ", math.pow(num,3))
    print("Raiz 3: ", math.pow(num,1/3))

ejer4()

def ejer5():
    num =input("Escriba un numero(texto): ")

    entero = int(num)
    deci = float(num)

    print("Resto: ",(entero%2))
    print("División: ", (deci/3))

ejer5()