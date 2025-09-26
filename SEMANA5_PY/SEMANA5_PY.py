def menu():
    while True:
        print("\n1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Salir")
        opcion = int(input("\nIngrese una opción: "))
        match opcion:
            case 1: ejer1()
            case 2: ejer2()
            case 3: exit()
            case _: print("\nOpción incorrecta")

def ejer1():
    edad = int(input("\nIngrese su edad: "))

    if edad >= 18:
        print("\nPuede votar")

        if edad>=25:
            print("\nCandidato para un cargo político")
        else:
            print("\nNo puede ser candidato para un cargo político")
    else:
        print("\nNo puede votar\nNo puede ejercer un cargo político.")

def ejer2():
    lado1 = int(input("\nIngrese lado1: "))
    lado2 = int(input("Ingrese lado2: "))
    lado3 = int(input("Ingrese lado3: "))

    if(lado1 == lado2 ==lado3):
        print("\nEQUILATERO")
    elif lado1 ==lado2 or lado1==lado3 or lado2==lado3:
        print("\nISÓSCELES")
    else:
        print("\nESCALENO")
menu()

