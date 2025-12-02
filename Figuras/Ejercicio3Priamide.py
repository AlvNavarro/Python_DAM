"""
Ejercicio 3: Pirámide con huecos internos (estructura tipo "reja")
Enunciado:

Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.

Figura para n=6:

     *
    * *
   *   *
  * * * *
 *       *
***********
"""
altura = int(input("Ingrese la altura de la pirámide: "))
medio=altura//2

def piramide(altura):
    for i in range(altura):
        print(" " * (altura - i - 1), end="")

        if i == medio:
            print("* " * (medio + 1 ), end="")
            
        elif i == 0:
            print("*", end="")

        elif i == altura - 1:
            print("*" * (2 * i + 1), end="")

        else:
            print("*", end="")
            hueco = 2 * i - 1
            print(" " * hueco, end="")
            
            print("*", end="")
                
        print()
        
piramide(altura)