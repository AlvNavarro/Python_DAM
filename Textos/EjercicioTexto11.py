# Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.
def duplicar_vocales(cadena):
    vocales = "aeiouAEIOU"
    nueva_cadena = ""
    for caracter in cadena:
        if caracter in vocales:
            nueva_cadena += caracter*2
        else:
            nueva_cadena += caracter
    return nueva_cadena
frase = input("Ingrese una cadena de texto: ")
resultado = duplicar_vocales(frase)
print(f"Cadena con vocales duplicadas: {resultado}")