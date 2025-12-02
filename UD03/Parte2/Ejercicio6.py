def calcular_factorial(N):
    if N < 0:
        return "Error: El factorial no esta definido para numeros negativos."
    
    if N == 0 or N == 1:
        return 1
    
    resultado = 1
    for i in range(2, N + 1):
        resultado *= i
        
    return resultado

try:
    N = int(input("Ingrese un numero positivo N para calcular su factorial (N!): "))
    
    if N < 0:
        print("El numero debe ser positivo.")
    else:
        factorial = calcular_factorial(N)
        print(f"El factorial de {N} ({N}!) es: {factorial}")

except ValueError:
    print("Error: Ingrese un numero entero valido.")