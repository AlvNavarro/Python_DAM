# Ejercicio 30: Dibuja un ordinograma de un programa que dada una cantidad de euros que el usuario 
# introduce por teclado (múltiplo de 5 €) mostrará los billetes de cada tipo que serán necesarios 
# para alcanzar dicha cantidad (utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar 
# el mínimo de billetes posible. Por ejemplo, si el usuario introduce 145 el programa indicará que
# será necesario 1 billete de 100 €, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 
# 29 billetes de 5, que aunque sume 145 € no es el mínimo número de billetes posible).
def main():
    cantidad = int(input("Ingrese una cantidad en euros (múltiplo de 5): "))
    if cantidad % 5 != 0:
        print("La cantidad debe ser un múltiplo de 5.")
        return

    billetes = [500, 200, 100, 50, 20, 10, 5]
    conteo_billetes = {}

    for billete in billetes:
        conteo_billetes[billete] = cantidad // billete
        cantidad %= billete

    print("Desglose de billetes necesarios:")
    for billete, cantidad_billetes in conteo_billetes.items():
        if cantidad_billetes > 0:
            print(f"{cantidad_billetes} billete(s) de {billete} €")

if __name__ == "__main__":
    main()