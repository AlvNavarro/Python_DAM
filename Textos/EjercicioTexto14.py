# Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.
def contar_numero(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isdigit():
            contador += 1
    return contador

cadena_entrada = input("Ingrese una cadena de texto: ")
cantidad_numeros = contar_numero(cadena_entrada)
print("Cantidad de caracteres numéricos en la cadena:", cantidad_numeros)