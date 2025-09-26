num =int(input("Ingrese un número positivo: "))
print()

while num<=0:
    num =int(input("\nError. Ingrese un número positivo."))

i = 1
while i<=12:
    print(f"\n{i} x {num} ={i*num}")
    i+=1