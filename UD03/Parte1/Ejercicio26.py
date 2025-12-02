"""
En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
    Si los tres dados son seis, mostrar el mensaje “Excelente”
    Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
    Si un dado se obtiene seis, mostrar el mensaje “Regular”
    Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch).
"""

def pedir_valor_dado(pos: int) -> int:
    while True:
        try:
            valor = int(input(f"Ingrese el valor del dado {pos} (1-6): ").strip())
        except ValueError:
            print("ERROR: Debe ingresar un número entero entre 1 y 6.")
            continue

        if 1 <= valor <= 6:
            return valor
        else:
            print("ERROR: El valor del dado debe estar entre 1 y 6. Intente nuevamente.")


def main() -> None:
    dado1 = pedir_valor_dado(1)
    dado2 = pedir_valor_dado(2)
    dado3 = pedir_valor_dado(3)

    cantidad_seises = sum(1 for d in (dado1, dado2, dado3) if d == 6)

    match cantidad_seises:
        case 3:
            mensaje = "Excelente"
        case 2:
            mensaje = "Muy bien"
        case 1:
            mensaje = "Regular"
        case 0:
            mensaje = "Pésimo"
        case _:
            mensaje = "Error: resultado inesperado"

    print("\n--- Resultados ---")
    print(f"Dados: {dado1}, {dado2}, {dado3}")
    print(f"Cantidad de seises: {cantidad_seises}")
    print(f"Mensaje: {mensaje}")


if __name__ == "__main__":
    main()

