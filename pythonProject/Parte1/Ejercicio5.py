# Ejercicio 5
# Descuento en valor de compra

descuento = 0.15

valor = float(input("Ingrese el valor total de la compra: "))
valor = valor - (valor*descuento)
print(f"El valor total a pagar es de: {valor:.2f} pesos")
