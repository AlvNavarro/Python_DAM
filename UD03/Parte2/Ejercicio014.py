"""
Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado.
Ejemplo: Si introducimos un 5, deberá dibujar lo siguiente:
    *
   ***
  *****
 *******
"""

try:
    altura=int(input("Introduce la altura de la escalera: "))
    if altura <=0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número entero.")
else:
    for i in range(altura):
        print(" " * (altura - i - 1) + "*" * (2 * i + 1))