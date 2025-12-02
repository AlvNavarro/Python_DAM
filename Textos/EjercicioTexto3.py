"""
EjercicioTexto3 - Contar caracteres en una cadena
Demuestra cómo contar cuántas veces aparece un carácter específico
en una cadena de texto utilizando un bucle for y un contador en Python.
"""
def contador(cadena, caracter):
    contador = 0
    for char in cadena:
        if char == caracter:
            contador += 1
    return contador

texto = input("Introduce una cadena de texto: ")
caracter_contar = input("Introduce el carácter a contar: ")
resultado = contador (texto, caracter_contar)
print(f"El carácter '{caracter_contar}' aparece {resultado} veces en la cadena '{texto}'.")
