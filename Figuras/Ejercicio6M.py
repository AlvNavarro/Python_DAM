"""
Ejercicio 6: Letra M mayúscula con asteriscos
Enunciado:

Imprime la letra M mayúscula usando asteriscos en una matriz cuadrada de tamaño impar n. Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto.

Figura para n=7:

*     *
**   **
* * * *
*  *  *
*     *
*     *
*     *
columna_actual = j
fila_actual = i
"""

altura = int(input("Dime la altura: "))

def letra_m(altura):
    if altura < 3 or altura % 2 == 0:
        print("La altura debe ser un número impar mayor o igual a 3.")
        return

    for i in range(altura):
        linea = ""
        for j in range(altura):
            if j == 0:
                linea += '*'
            elif j == altura - 1:
                linea += '*'
            elif i <= altura // 2:
                if j == i:
                    linea += '*'
                elif j == altura - 1 - i:
                    linea += '*'
                else:
                    linea += ' '
            else:
                linea += ' '
        print(linea)

letra_m(altura)