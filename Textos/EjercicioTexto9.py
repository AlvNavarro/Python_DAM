# Leer una cadena y contar cuántas vocales contiene.
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for char in cadena:
        if char in vocales:
            contador += 1
    return contador

frase = input("Ingrese una cadena de texto: ")
num_vocales = contar_vocales(frase)
print(f"La cadena contiene {num_vocales} vocales.")