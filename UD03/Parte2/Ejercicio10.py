limite = 10
suma = 0
producto = 1

print(f"Calculando la suma y el producto de los 10 primeros numeros naturales (1 a {limite}).")

for numero in range(1, limite + 1):
    suma += numero
    producto *= numero

print(f"Suma de los primeros {limite} numeros naturales: {suma}")
print(f"Producto de los primeros {limite} numeros naturales: {producto}")

print("Fin del programa.")