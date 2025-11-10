# Ejercicio 28: Dibuja un ordinograma de un programa que suma independientemente los pares y los 
# impares de los números comprendidos entre 100 y 200, y luego muestre por pantalla ambas sumas.
def main():
    suma_pares = 0
    suma_impares = 0
    for numero in range(100, 201):
        if numero % 2 == 0:
            suma_pares += numero
        else:
            suma_impares += numero
    print("Suma de los números pares entre 100 y 200:", suma_pares)
    print("Suma de los números impares entre 100 y 200:", suma_impares)