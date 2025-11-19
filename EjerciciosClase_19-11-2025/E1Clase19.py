"""
Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.

Figura para n=5
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""
try:
    altura = 5
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número entero positivo.")
else:
    filastotales = (altura * 2) - 1
    mitad = altura - 1
    for i in range(filastotales):
        if i <= mitad:
            x = i
        else:
            x = filastotales - 1 - i
            
        print(" " * (mitad - x), end="")
        print("*", end="")
        
        if x > 0:
            print(" " * (2 * x - 1) + "*")
        else:
            print()