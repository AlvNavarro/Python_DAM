try:
    altura = int(input("Ingrese la altura de la escalera (numero positivo): "))
    
    if altura <= 0:
        print("La altura debe ser un numero positivo.")
    else:
        print(f"\nEscalera de numeros de altura {altura}:")
        
        for i in range(1, altura + 1):
            numero_str = str(i)
            print(numero_str * i)

except ValueError:
    print("Error: Ingrese un numero entero valido para la altura.")