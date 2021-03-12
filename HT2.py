#Ejercicio1
print("EJERCICIO 1")
conta1 = input("Introduce la contraseña a almacenar: ")
print("")
password = input("Introduce tu contraseña para ingresar: ")
print("")
if conta1.lower() == password.lower():
    print("Contraseña correcta, bienvenido")
else:
    print("La contraseña incorrecta")
print("")

#Ejercicio2
print("EJERCICIO 2")
nombre = input("¿Cómo te llamas? ")
print("")
genero = input("¿Cuál es tu sexo (M o H)? ")
print("")
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)
print("")
print("Feliz día :)")