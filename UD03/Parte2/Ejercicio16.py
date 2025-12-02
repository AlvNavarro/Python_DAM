nota_diez_encontrada = False

print("Ingrese una secuencia de notas (0 a 10). Ingrese -1 para terminar.")

while True:
    try:
        nota = float(input("Ingrese una nota: "))
        
        if nota == -1:
            break
        
        if 0 <= nota <= 10:
            if nota == 10:
                nota_diez_encontrada = True
        else:
            print("Nota fuera de rango (0 a 10). Por favor, ingrese una nota valida.")
            
    except ValueError:
        print("Entrada invalida. Por favor, ingrese un numero valido.")

print("\n--- Resultado del Analisis ---")
if nota_diez_encontrada:
    print("Si. Hubo al menos una nota con valor 10.")
else:
    print("No. No hubo notas con valor 10.")

print("Fin del programa.")