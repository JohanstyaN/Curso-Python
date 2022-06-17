# Ejercicio 5 Cajero Automatico

print("|-----------------------------------|\n"
      "| Bienvenido al Cajero Automatico   |\n"
      "| Escoja su Operacion:              |\n"
      "| 1 - Ingresar Pago                 |\n"
      "| 2 - Retirar dinero                |\n"
      "| 3 - Mostrar Salido                |\n"
      "| 4 - Salir                         |\n"
      "|-----------------------------------|")

account = 1000

operation = int(input("Ingrese la operacion a realizar (Ingrese el Numero Correspondiente): \n"))

while operation != 4:
    if operation == 1:
        income = float(input("Ingrese el valor de la consignacion: "))
        account += income
        operation = int(input("Realizado.\n"
                              "Ingrese la operacion a realizar: \n"))
    elif operation == 2:
        withdrawal = float(input("Ingrese el valor a retirar: "))
        if account < withdrawal:
            print(f"No tiene suficiente saldo en la cuenta: --{account}--")
            operation = int(input("Ingrese la operacion a realizar: \n"))
        else:
            account -= withdrawal
            operation = int(input("Realizado.\n"
                                  "Ingrese la operacion a realizar: \n"))
    elif operation == 3:
        print(f"El saldo de la cuenta es: {account}")
        operation = int(input("Realizado.\n"
                              "Ingrese la operacion a realizar: \n"))
    else:
        print(f"Se ha equivocado de Operacion: <<{operation}>> No existe")
        operation = int(input("Ingrese la operacion a realizar: \n"))
    print("Ha salido del sistema con exito")

# ----------------------------------------------------------------------------------------------------------------------
# Otra Manera

print("Segunda Forma \n")

operation = int(input("Ingrese la operacion a realizar (Ingrese el Numero Correspondiente): \n"))

if operation == 1:
    income = int(input("Ingrese el valor de la consignacion: "))
    account += income
    print(f"El saldo de la cuenta es: {account}")
elif operation == 2:
    withdrawal = int(input("Ingrese el valor a retirar: "))
    if account < withdrawal:
        print(f"No tiene suficiente saldo en la cuenta: --{account}--")
    else:
        account -= withdrawal
        print(f"El saldo de la cuenta es: {account}")

elif operation == 3:
    print(f"El saldo de la cuenta es: {account}")

elif operation == 4:
    print("Ha salido del sistema con exito")
else:
    print("La operacion Solicitada No existe")
