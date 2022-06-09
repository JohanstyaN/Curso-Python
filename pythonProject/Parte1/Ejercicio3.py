# Ejercicio 3
# Cambio de Valor en variables


print("Primera Forma")

a = int(input("Escriba el Valor de a: "))
b = int(input("Escriba el Valor de b: "))

print(f"El valor de las variables son: {a} - {b}")

a ^= b
b ^= a
a ^= b

print(f"El valor de las variables son: {a} - {b}")

#####################################################

# Otra manera
print("Segunda Forma")

print(f"El valor de las variables son: {a} - {b}")
aux = a
a = b
b = aux
print(f"El valor de la variable auxiliar es {aux}")
print(f"El valor de las variables son: {a} - {b}")

#####################################################

# Otra Forma
print("Tercera Forma")

print(f"El valor de las variables son: {a} - {b}")
a, b = b, a
print(f"El valor de las variables son: {a} - {b}")
