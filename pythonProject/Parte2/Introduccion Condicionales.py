# Introduccion


num = int(input("Digitar numero: "))

if num > 0:
    print("El numero es positivo")
elif num == 0:
    print("El numero es 0")
else:
    print("El numero es Negativo")

# Combinacion de Condicionales

edad = int(input("Ingrese su Edad: "))

if 0 < edad < 130:
    print("Edad Correcta")
    if edad >= 18:
        print("Es Mayor de Edad")
    else:
        print("No es Mayor de Edad")
else:
    print("La edad es incorrecta")
