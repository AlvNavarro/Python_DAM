# Ejercicio 16: Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene.
numero = int(input("Introduce un número entre 0 y 99999: "))
if 0 <= numero <= 99999:
    if numero < 10:
        print("El número tiene 1 cifra.")
    elif numero < 100:
        print("El número tiene 2 cifras.")
    elif numero < 1000:
        print("El número tiene 3 cifras.")
    elif numero < 10000:
        print("El número tiene 4 cifras.")
    else:
        print("El número tiene 5 cifras.")