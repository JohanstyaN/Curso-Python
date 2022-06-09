# Ejercicio 4
# Calculo de la longitud y Area del Circulo

import math

import numpy

radio = float(input("Ingrese el numero del radio :"))

area = round((numpy.pi * radio ** 2), 4)
longitud = round((2 * numpy.pi * radio), 4)

var = numpy.pi
var2 = math.pi

print(f"El valor de var1 es {var} y el de var2 es de {var2}")

print(f"Teniendo en cuenta que la circunferencia tiene un radio de {radio}, su area es de {area} y su longitud es"
      f" de {longitud}")

#####################################
# Otra manera de Redondear

print("Second Form")

area = numpy.pi * radio ** 2
longitud = 2 * numpy.pi * radio

print(f"Teniendo en cuenta que la circunferencia tiene un radio de {radio}, su area es de {area:.2f} y su longitud es "
      f"de {longitud:.2f}")
