# Ejercicio 1
# Condicionales

numero1 = int(input("Ingrese en Primer Numero: "))
numero2 = int(input('Ingrese en Segundo Numero: '))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos son pares")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print(f"El Primer Numero ({numero1}) Es Par")
elif numero1 % 2 != 0 and numero2 % 2 == 0:
    print(f"El segundo Numero ({numero2}) es Par")
elif numero1 % 2 != 0 and numero2 % 2 != 0:
    print("Ambos Numeros son impares")
