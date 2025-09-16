def ejer1():
    edad = int(input("Ingrese su edad: "))

    if edad >= 18:
        print("Puede votar")

        if edad>=25:
            print("Candidato para un cargo político")
        else:
            print("No puede ser candidato para un cargo político")
    else:
        print("No puede votar\nNo puede ejercer un cargo político.")

def ejer2():
    lado1 = int(input("Ingrese lado1: "))
    lado2 = int(input("Ingrese lado2: "))
    lado3 = int(input("Ingrese lado3: "))

    if(lado1 == lado2 ==lado3):
        print("EQUILATERO")
    elif lado1 ==lado2 or lado1==lado3 or lado2==lado3:
        print("ISÓSCELES")
    else:
        print("ESCALENO")

        


ejer1()

