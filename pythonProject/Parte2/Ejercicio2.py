# Ejercicio2

num1 = int(input("Ingrese el valor del primer Numero: "))
num2 = int(input("Ingrese el valor del segundo Numero: "))
num3 = int(input("Ingrese el valor del Tercer Numero: "))

if num2 < num1:
    if num3 < num1:
        print(f"El Numnero mayor es {num1}")
    elif num3 > num1:
        print(f"El numero mayor es {num3}")
    elif num3 == num1:
        print(f"Los numeros mayores {num3} y {num1} son iguales")
elif num1 < num2:
    if num3 < num2:
        print(f"El numero mayor es {num2}")
    elif num3 > num2:
        print(f"El numero mayor es {num3}")
    elif num3 == num2:
        print(f"Los numeros mayores {num3} y {num2} son iguales")
elif num1 < num3:
    if num2 < num3:
        print(f"El numero mayor es {num3}")
    elif num2 > num3:
        print(f"El numero mayor es {num2}")
    elif num2 == num3:
        print(f"Los numeros mayores {num2} y {num3} son iguales")
elif num3 < num1:
    if num2 < num1:
        print(f"El numero mayor es {num1}")
    elif num2 > num1:
        print(f"El numero mayor es {num2}")
    elif num2 == num1:
        print(f"Los numeros mayores {num2} y {num1} son iguales")
elif num1 == num2 == num3:
    print("Los Numeros son iguales")

##################################################################
# Otra Manera

print("Segunda Manera")

if num1 >= num2 and num1 >= num3:
    print(f"El numero mayor es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El numero mayor es {num2}")
elif num3 >= num1 and num3 >= num2:
    print(f"El numero mayor es {num3}")

