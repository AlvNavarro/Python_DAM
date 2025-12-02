# Leer una cadena y construir una nueva cadena con los caracteres en orden inverso.
def invertir_cadena(cadena):
    nueva_cadena = ""
    for caracter in cadena:
        nueva_cadena = caracter + nueva_cadena
    return nueva_cadena
frase = input("Ingrese una cadena de texto: ")
resultado = invertir_cadena(frase)
print(f"Cadena invertida: {resultado}")
