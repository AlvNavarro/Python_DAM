hay_negativos = False
positivos = 0
negativos = 0
total_leidos = 0

print("Ingrese una secuencia de numeros. Ingrese 0 para terminar.")

while True:
    try:
        numero = float(input(f"Ingrese numero {total_leidos + 1} (0 para terminar): "))
        
        if numero == 0:
            break
        
        total_leidos += 1
        
        if numero > 0:
            positivos += 1
        else:
            negativos += 1
            hay_negativos = True
            
    except ValueError:
        print("Entrada invalida. Por favor, ingrese un numero valido.")

print("\n--- Resultado del Analisis ---")
print(f"Total de numeros no nulos leidos: {total_leidos}")
print("-" * 30)

if hay_negativos:
    print("Si se leyo al menos un numero negativo.")
else:
    print("No se leyo ningun numero negativo.")

print(f"Total de numeros positivos: {positivos}")
print(f"Total de numeros negativos: {negativos}")

print("Fin del programa.")