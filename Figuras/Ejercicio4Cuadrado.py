"""
Ejercicio 4: Cuadrado con diagonales y borde relleno
Enunciado:

Imprime un cuadrado de lado n con bordes de asteriscos y las dos diagonales marcadas, dejando espacios en el resto.

Figura para n=7:

*******
* *   *
*  *  *
*   * *
*  *  *
* *   *
*******
"""
altura = int(input("Ingrese la altura del cuadrado:"))
anchointerior = altura - 2
medio = altura // 2
for i in range(1, altura + 1):
    if i == 1:
        print("*" * altura)
    for j in range(1, altura+1):
        if j != altura and j <= medio:
            print("*" + " "*(j) + "*" + " " * (anchointerior - (j+1)) + "*")
        elif j > medio:
            print("*" +  " "*(anchointerior-(j-1)) + "*" + " " * (anchointerior - (j)) + "*")
    if i == altura:
        print("*" * altura)