# Ejercicio 13: Escriba un programa que lea dos números y lo visualiza en orden ascendente.
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num1 <= num2:
    print(f"Los números en orden ascendente son: {num1}, {num2}")
else:
    print(f"Los números en orden ascendente son: {num2}, {num1}") 