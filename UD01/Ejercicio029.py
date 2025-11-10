# Ejercicio 29: Dibuja un ordinograma de un programa donde el usuario “piensa” un número del 1 al 100 
# y el ordenador intenta adivinarlo. Es decir, el ordenador irá proponiendo números una y otra 
# vez hasta adivinarlo (El usuario deberá indicarlo al ordenador si es mayor o menor o igual al número pensado)
def main():
    print("Piensa en un número del 1 al 100.")
    input("Presiona Enter cuando estés listo.")
    bajo = 1
    alto = 100
    while True:
        intento = (bajo + alto) // 2
        respuesta = input(f"¿Es {intento} tu número? (mayor/menor/igual): ")
        if respuesta == "igual":
            print("¡He adivinado tu número!")
            break
        elif respuesta == "mayor":
            bajo = intento + 1
        elif respuesta == "menor":
            alto = intento - 1
        else:
            print("Respuesta no válida. Por favor, responde con 'mayor', 'menor' o 'igual'.")
