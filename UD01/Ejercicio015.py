# Ejercicio 15: Dibuja un ordinograma de un programa que lee dos números y muestra el mayor.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num1 > num2:
    print(f"El número mayor es: {num1}")
else:
    print(f"El número mayor es: {num2}")