# La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
# postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
# el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
# control switch)


IGV_TASA = 0.18
nombre_postulante = input("Ingrese el nombre del postulante: ")
facultad_ingresada = input("Ingrese la facultad que va a estudiar: ")
facultad_buscada = facultad_ingresada.strip()
importe_matricula = 0
mensualidad = 0
facultad_encontrada = False

if facultad_buscada == "Ing. de Sistemas":
    importe_matricula = 350
    mensualidad = 650
    facultad_encontrada = True
elif facultad_buscada == "Derecho":
    importe_matricula = 300
    mensualidad = 550
    facultad_encontrada = True
elif facultad_buscada == "Ing. Naviera":
    importe_matricula = 300
    mensualidad = 500
    facultad_encontrada = True
elif facultad_buscada == "Ing. Pesquera":
    importe_matricula = 310
    mensualidad = 460
    facultad_encontrada = True
elif facultad_buscada == "Contabilidad":
    importe_matricula = 280
    mensualidad = 490
    facultad_encontrada = True
elif facultad_buscada == "Administración":
    importe_matricula = 360
    mensualidad = 520
    facultad_encontrada = True

print("\n--- Resultados de Matrícula ---")

if not facultad_encontrada:
    print(f"ERROR: La facultad '{facultad_ingresada}' no se encontró en la lista de costos.")
else:
    subtotal = importe_matricula + mensualidad
    igv_monto = subtotal * IGV_TASA
    monto_final = subtotal + igv_monto

    print(f"Postulante: {nombre_postulante}")
    print(f"Facultad: {facultad_buscada}")
    print(f"Importe de Matrícula: S/. {importe_matricula:.2f}")
    print(f"Mensualidad: S/. {mensualidad:.2f}")

    print("\nDetalle de Pago")
    print(f"IGV 18% (Importe + Mensualidad): S/. {igv_monto:.2f}")
    print(f"Monto Final a Pagar: S/. {monto_final:.2f}")