# Ejercicio 23: Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta 
# que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.
def main():
    contador_positivos = 0
    contador_negativos = 0
    ha_leido_negativo = False

    while True:
        numero = int(input("Introduce un número no nulo (0 para terminar): "))
        if numero == 0:
            break
        if numero > 0:
            contador_positivos += 1
        else:
            contador_negativos += 1
            ha_leido_negativo = True

    if ha_leido_negativo:
        print("Se ha leído al menos un número negativo.")
    else:
        print("No se ha leído ningún número negativo.")

    print(f"Números positivos: {contador_positivos}")
    print(f"Números negativos: {contador_negativos}")