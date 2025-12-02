"""
    4 
    4 4
    4   4
    4     4
    4 4 4 4 4
"""

try:
    altura = int(input("Introduce la altura del triángulo: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número entero positivo.")
else:
    for i in range(altura):
        for j in range(i + 1):
            if j == 0 or j == i or i == altura - 1:
                print("4", end=" ")
            else:
                print(" ", end=" ")
        print()