# Ejercicio 5
# Calculadora


print("|-----------------------------------|\n"
      "| Calculadora                       |\n"
      "| Comandos Disponibles              |\n"
      "| S, s - Suma                       |\n"
      "| R, r - Resta                      |\n"
      "| P, p, M, m - Multiplicacion       |\n"
      "| D, d - Division                   |\n"
      "|-----------------------------------|")

num1Command = int(input("Ingrese primer Numero: "))
command = str(input("Ingrese la Operacion que desea Realizar: ")).lower()
num2Command = int(input("Ingrese Segundo Numero: "))

if command == "s":
    resultado = num1Command + num2Command
    print(f"El resultado es {num1Command} + {num2Command} = {resultado}")
elif command == "r":
    resultado = num1Command - num2Command
    print(f"el resultado es {num1Command} - {num2Command} = {resultado}")
elif command == "p" or command == "m":
    resultado = num1Command * num2Command
    print(f"el resultado es {num1Command} x {num2Command} = {resultado:.2f}")
elif command == "d":
    resultado = num1Command / num2Command
    print(f"el resultado es {num1Command} / {num2Command} = {resultado:.2f}")
else:
    print(f"El comando Utilizado no es valido: <<{command.upper()}>>")