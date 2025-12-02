CANTIDAD_NUMEROS = 100
positivos = 0
negativos = 0

print(f"Ingrese {CANTIDAD_NUMEROS} numeros no nulos (0 no es valido).")

for i in range(1, CANTIDAD_NUMEROS + 1):
    while True:
        try:
            numero = float(input(f"Numero {i} de {CANTIDAD_NUMEROS}: "))
            
            if numero == 0:
                print("El numero no debe ser nulo (0). Intente de nuevo.")
                continue
            
            if numero > 0:
                positivos += 1
            else:
                negativos += 1
            
            break
        
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero valido.")

print("\n--- Resultado del Analisis ---")
print(f"Numeros positivos leidos: {positivos}")
print(f"Numeros negativos leidos: {negativos}")
print("Fin del programa.")