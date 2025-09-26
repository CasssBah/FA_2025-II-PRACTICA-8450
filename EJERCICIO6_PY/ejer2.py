sumap = sumai = 0
while  True:
    num = int(input("\nIngrese un número (0 salir): "))

    if (num<0):
        print("\nNúmero inválido. Ingrese nuevamente" )
        continue

    if num== 0:
        break

    if num%2 == 0:
        sumap+=num
    else:
        sumai+= num

print("\nSuma pares: ", sumap)
print("\nSuma de impares: ", sumai)