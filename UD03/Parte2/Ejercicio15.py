try:
    altura = int(input("Ingrese la altura de la piramide invertida (numero positivo): "))
    
    if altura <= 0:
        print("La altura debe ser un numero positivo.")
    else:
        print(f"\nPiramide invertida de asteriscos de altura {altura}:")
        
        for i in range(altura):
            num_espacios = i
            num_asteriscos = 2 * (altura - i) - 1

            linea = " " * num_espacios + "*" * num_asteriscos
            
            print(linea)

except ValueError:
    print("Error: Ingrese un numero entero valido para la altura.")