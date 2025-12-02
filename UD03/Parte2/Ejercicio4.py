try:
    N = int(input("Ingrese el numero N (limite superior): "))
    
    if N < 1:
        print("El numero N debe ser positivo (mayor o igual a 1).")
    else:
        print(f"Numeros desde 1 hasta {N}:")
        
        for i in range(1, N + 1):
            print(i)

except ValueError:
    print("Error: Ingrese un numero entero valido.")