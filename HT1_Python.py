## EJERCICIO 1
print("EJERCICIO 1")
print("")
num = int(input("Ingrese un número para la altura del triangulo: "))
for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print("")

## EJERCICIO 2
print("")
print("EJERCICIO 2")
print("")
num = int(input("Introduce un número entero positivo: "))
for i in range(num, -1, -1):
    print(i, end=", ")

## EJERCICIO 3
print("")
print("EJERCICIO 3")
print("")
num = int(input("Introduce un numero para ver si es primo: "))
for i in range(1, num):
    if num % i == 0:
        break
if (i + 1)  == num:
    print(str(num) + " es primo")
else: 
    print(str(num) + " no es primo")