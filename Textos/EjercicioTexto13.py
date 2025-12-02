# Leer una cadena y eliminar todos los espacios, construyendo una cadena continua.
def eliminar_espacios(cadena):
    cadena_sin_espacios = ""
    for caracter in cadena:
        if caracter != " ":
            cadena_sin_espacios += caracter
    return cadena_sin_espacios

cadena_entrada = input("Ingrese una cadena de texto: ")
cadena_salida = eliminar_espacios(cadena_entrada)
print("Cadena sin espacios:", cadena_salida)