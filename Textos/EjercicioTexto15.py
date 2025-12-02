# Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'
def reemplazar_vocales(cadena):
    vocales = "aeiouAEIOU"
    nueva_cadena = ""
    for caracter in cadena:
        if caracter in vocales:
            nueva_cadena += "*"
        else:
            nueva_cadena += caracter
    return nueva_cadena

texto = input("Ingrese una cadena de texto:")
resultado = reemplazar_vocales(texto)
print("Cadena con vocales reemplazadas:", resultado)