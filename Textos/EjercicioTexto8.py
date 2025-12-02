# Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower()).
frase = "Programacion_es_divertida"
print(f"Cadena original: {frase}\n")
opcion = input("Escribe 'M' para convertir a mayúsculas o 'm' para minúsculas: ")
nueva_frase = ""
diferencia = ord('a') - ord('A')
for caracter in frase:
    if opcion == 'M':
        if 'a' <= caracter <= 'z':
            nueva_frase += chr(ord(caracter) - diferencia)
        else:ord('a') - ord('A')
        nueva_frase += caracter
    elif opcion == 'm':
        if 'A' <= caracter <= 'Z':
            nueva_frase += chr(ord(caracter) + diferencia)
        else:
            nueva_frase += caracter
    else:
        nueva_frase = frase
        break
print(f"Cadena después de la conversión: '{nueva_frase}'")