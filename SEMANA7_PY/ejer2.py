import random

print("****************************************")
print("*       Bienvenido al adivinador       *")
print("* 1. Adivinar el número entre 1 y 20   *")
print("* 2. Tienes 3 Intentos                 *")
print("****************************************")

intentos = 3
secreto = random.randint(1,20)

while intentos >0:
    num = int(input("\nIngrese un número: "))
    if secreto == num:
        print("\nCorrecto! Adivinase el número.")
        break
    else:
        intentos -=1
        if num < secreto: 
            print(f"\nPista: El número es mayor. Intentos: {intentos}")
        else: 
            print(f"\nPista: El número es menor. Intentos: {intentos}")
else: print(f"\nNo lograste adivinar el número {secreto}")