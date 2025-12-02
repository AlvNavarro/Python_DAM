# Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo)
def concatenar_cadenas(cadena1, cadena2):
    cadena_concatenada = ""
    for caracter in cadena1:
        cadena_concatenada += caracter
    for caracter in cadena2:
        cadena_concatenada += caracter
    return cadena_concatenada
cadena_1 = input("Ingrese la primera cadena de texto: ")
cadena_2 = input("Ingrese la segunda cadena de texto: ")
resultado = concatenar_cadenas(cadena_1, cadena_2)
print("Cadena concatenada:", resultado)