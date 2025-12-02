# Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez
def caracteres_repetidos(cadena):
    caracteres_repetidos = ""
    for caracter in cadena:
        if cadena.count(caracter) > 1 and caracter not in caracteres_repetidos:
            caracteres_repetidos += caracter
    return caracteres_repetidos
cadena_entrada = input("Ingrese una cadena de texto: ")
resultado = caracteres_repetidos(cadena_entrada)
print("Caracteres que se repiten más de una vez:", resultado)