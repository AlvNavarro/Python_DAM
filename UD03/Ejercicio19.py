# Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares, con el siguiente menú de opciones:
# Bienvenido a su Cajero Virtual
# 1. Ingresar dinero en cuenta
# 2. Retirar dinero de la cuenta
# 3. Salir
saldo = 1000
while True:
    print("Bienvenido a su Cajero Virtual")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        saldo += cantidad
        print("Depósito exitoso. Su nuevo saldo es:", saldo)
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= cantidad
            print("Retiro exitoso. Su nuevo saldo es:", saldo)
    elif opcion == "3":
        print("Gracias por usar el cajero. Hasta luego.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")