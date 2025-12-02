"""
Ejercicio 8: Rombo sólido
Enunciado:

Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.

Figura para n=4:

   *
  ***
 *****
*******
 *****
  ***
   *
"""

try:
    altura = int(input("Introduce la altura del rombo (debe ser impar): "))
    if altura <= 0 or altura % 2 == 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número entero positivo e impar.")
else:
    medio = altura // 2
    
    for i in range(altura):
        if i <= medio:
            x = i
        else:
            x = altura - 1 - i
            
        espacios = " " * (medio - x)
        
        asteriscos = "*" * (2 * x + 1)

        print(espacios + asteriscos)