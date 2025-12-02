def calcular_billetes(cantidad):
    if not isinstance(cantidad, int) or cantidad <= 0:
        return "Error: La cantidad debe ser un numero entero positivo."
    
    if cantidad % 5 != 0:
        return "Error: La cantidad debe ser un multiplo de 5 euros."

    denominaciones = [500, 200, 100, 50, 20, 10, 5]
    resultado = {}
    cantidad_restante = cantidad

    print(f"\nDesglose de {cantidad} euros (billetes minimos):")

    for billete in denominaciones:
        conteo = cantidad_restante // billete
        
        if conteo > 0:
            resultado[billete] = conteo
            cantidad_restante %= billete
    
    total_billetes = 0
    for billete, cantidad in resultado.items():
        print(f"{cantidad} billete(s) de {billete} €")
        total_billetes += cantidad

    print(f"\nTotal de billetes utilizados: {total_billetes}")
    return "Calculo completado."

try:
    cantidad_euros = int(input("Ingrese la cantidad de euros (multiplo de 5 €): "))
    print(calcular_billetes(cantidad_euros))

except ValueError:
    print("Error: Ingrese un numero entero valido.")