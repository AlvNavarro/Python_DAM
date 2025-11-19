"""
Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n (ej. 9x9).

Figura para n=9:

*   *   *
 *  *  *
  * * *
*********
  * * *
 *  *  *
*   *   *

NO VA BIEN TODAVÍA
"""
try:
    altura = int(input("Introduce la altura del triángulo: "))
    if altura <= 0:
        raise ValueError
    if altura % 2 == 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número entero positivo e impar.")
else:
    mitad = altura // 2
    for i in range(altura):
        for j in range(altura):
            if i == mitad or j == mitad or i == j or j == altura - 1 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print()