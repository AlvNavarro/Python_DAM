"""
          *
        * *
      *   *
    *     *
  *       *
*         *
  *       *
    *     *
      *   *
        * *
          *
"""

try:
    altura = int(input("Introduce la altura: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Debes introducir un número entero positivo.")
else:
    filas_totales = (altura * 2) + 1 

    mitad = altura 

    for i in range(filas_totales):
        if i <= mitad:
            x = i
        else:
            x = filas_totales - 1 - i
        print(" " * 2 * (mitad - x), end="")
        print("*", end="")
        
        if x > 0:
            print(" " * (2 * x - 1) + "*")
        else:
            print()