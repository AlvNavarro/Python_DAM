# Ejercicio 27: Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.
def main():
    nota = 0
    hubo_diez = False
    while nota != -1:
        nota = float(input("Ingrese una nota (0-10) o -1 para terminar: "))
        if nota == 10:
            hubo_diez = True
    if hubo_diez:
        print("Se ingresó al menos una nota con valor 10.")
    else:
        print("No se ingresó ninguna nota con valor 10.")
