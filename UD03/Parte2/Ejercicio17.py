inicio = 100
fin = 200
suma_pares = 0
suma_impares = 0

print(f"Sumando pares e impares entre {inicio} y {fin}...")

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("\n--- Resultados de Sumas ---")
print(f"Suma de los numeros pares entre {inicio} y {fin}: {suma_pares}")
print(f"Suma de los numeros impares entre {inicio} y {fin}: {suma_impares}")

print("Fin del programa.")