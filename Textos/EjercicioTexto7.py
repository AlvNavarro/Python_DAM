# Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.
frase = "Programacion_es_divertida"
print(f"Cadena original: {frase}\n")

caracter_remplazar = input("Pon el caracter que quieres remplazar: ")
caracter_nuevo = input("Pon el nuevo caracter para remplazarlo: ")

nueva_frase = ""
for caracter in frase:
    if caracter == caracter_remplazar:
        nueva_frase += caracter_nuevo
    else:
        nueva_frase += caracter
print(f"Cadena después de reemplazar '{caracter_remplazar}' por '{caracter_nuevo}': '{nueva_frase}'") 