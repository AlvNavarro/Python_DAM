# Leer una cadena y contar cuántos caracteres son letras mayúsculas
def contar_mayusculas(cadena):
    contador = 0
    for caracter in cadena:
        if caracter.isupper():
            contador += 1
    return contador

frase = input("Ingrese una cadena de texto: ")
num_mayusculas = contar_mayusculas(frase)
print(f"Número de letras mayúsculas en la cadena: {num_mayusculas}")