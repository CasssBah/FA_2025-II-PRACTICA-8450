g = input("Genere una contraseña: ")

print("\n------------------------------------------")
print("|           Valida tu contraseña          |")
print("|                                         |")
print("| 1. Ud. tiene 3 intentos                 |")
print("------------------------------------------\n")

intentos = 3

while (intentos >0):
    c= input("Ingrese la contraseña: ")

    if g ==c:
        print("\nAcceso concedido. Bienvenido al sistema.")
        break
    else:
        intentos -=1
        print(f"\nContraseña incorrecta. Intentos restantes {intentos}.")

else: print("\nAcceso denegado! Cerrando sistema")