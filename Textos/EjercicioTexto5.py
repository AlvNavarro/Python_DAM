# Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.
def verificar_caracter(cadena, caracter):
    for char in cadena:
        if char == caracter:
            return True
    return False

texto = input ("Introduce una cadena de texto:")
caracter_verificar = input ("Introduce el carácter a verificar:")
if verificar_caracter (texto, caracter_verificar):
    print (f"El carácter '{caracter_verificar}' SÍ está en la cadena '{texto}'.")
else:
    print (f"El carácter '{caracter_verificar}' NO está en la cadena '{texto}'.")
    