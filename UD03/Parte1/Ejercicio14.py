# Ejercicio 14 : Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales.
num1 = float(input("Introduce el primer número:"))
num2 = float(input("Introduce el segundo número:"))
if num1 > num2:
    print(f"El numero mayor es : {num1}")
elif num2 > num1:
    print(f"El numero mayor es : {num2}")
else:
    print("Los números son iguales.")