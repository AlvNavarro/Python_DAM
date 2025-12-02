# Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación)
def es_consonante(caracter):
    vocales = "aeiouAEIOU"
    if caracter not in vocales:
        return True
    return False
def filtrar_consonantes(cadena):
    cadena_consonantes = ""
    for caracter in cadena:
        if es_consonante(caracter):
            cadena_consonantes += caracter
    return cadena_consonantes
cadena_entrada = input("Ingrese una cadena de texto: ")
cadena_salida = filtrar_consonantes(cadena_entrada)
print("Cadena con sólo consonantes:", cadena_salida)
