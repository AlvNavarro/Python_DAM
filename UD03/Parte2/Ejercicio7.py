CANTIDAD_NUMEROS = 100
hay_negativos = False

print(f"Ingrese {CANTIDAD_NUMEROS} numeros no nulos (0 no es valido).")

for i in range(1, CANTIDAD_NUMEROS + 1):
    while True:
        try:
            numero = float(input(f"Numero {i} de {CANTIDAD_NUMEROS}: "))
            
            if numero == 0:
                print("El numero no debe ser nulo (0). Intente de nuevo.")
                continue
            
            if numero < 0:
                hay_negativos = True
            
            break
        
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero valido.")

print("\n--- Resultado del Analisis ---")
if hay_negativos:
    print("Si. Se leyo al menos un numero negativo.")
else:
    print("No. No se leyo ningun numero negativo.")

print("Fin del programa.")