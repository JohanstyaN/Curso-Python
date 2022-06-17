# Ejercicio 3
# Pedir Caracteres y Saber si son Vocales o no

# Ingreso de caracter

character = str(input("Ingrese Un Caracter: ")).lower()

# Declaramos Arreglo que almacene Vocales

vocales = ["a", "e", "i", "o", "u"]

# Ciclo que comparara si el caracter es una vocal

for value in range(len(vocales)):
    if character == vocales[value]:
        print(f"El caracter ({character}) es una vocal ({vocales[value]})")
        break
    elif value+1 == len(vocales):
        print(f"El caracter NO es una Vocal ({character})")


###############################################################################
# Otra Manera

print("Segunda Forma")

if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
    print(f"El caracter ({character}) es una vocal")
else:
    print(f"El caracter NO es una Vocal ({character})")
