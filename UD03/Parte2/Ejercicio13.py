try:
    altura = int(input("Ingrese la altura de la escalera (numero positivo): "))
    
    if altura <= 0:
        print("La altura debe ser un numero positivo.")
    else:
        print(f"\nEscalera de secuencia de numeros de altura {altura}:")
        
        for i in range(1, altura + 1):
            linea = ""
            for j in range(1, i + 1):
                linea += str(j)
            
            print(linea)

except ValueError:
    print("Error: Ingrese un numero entero valido para la altura.")