def ejer1(): #creando metodo ejer1
       nombre = input("Ingrese su nombreP: ")
       carrera = input("Ingrese su carrera: ")

       print(f"\n{nombre}, bienvenido a FA de {carrera}")

ejer1()

def ejer2():
    print("\"Pablo\"")

ejer2()

def ejer3():

    x = int(input("Ingrese el valor de  x: "))
    y = int(input("Ingrese el valor de y: "))

    print("Suma: ", (x+y))
    print("Resta: ", (x-y))
    print("Multiplicaci�n: ", (x*y))
    print("Divisi�n: ", (x/y))
       
ejer3()

import math #importando la librer�a math
def ejer4(): 
    
    num = float(input("Ingrese un n�mero decimal: "))

    print("Raiz 2: ", math.sqrt(num))
    print("Redondeado: ", round(num, 0))
    print("Al cubo: ", math.pow(num,3))
    print("Raiz 3: ", num**(1/3))

ejer4()

def ejer5():

    num = input("Ingrese n�mero")
    
    entero = int(num)
    deci = float(num)

    print("Resto: ", (entero%2))
    print("Divisi�n: ", (deci/3))

ejer5()

