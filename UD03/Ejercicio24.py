# Ejercicio 24: Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
# de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
# Visualizar el descuento y el total a pagar por la compra.
monto_compra = float(input("Ingrese el monto de compra: "))
dia_semana = input("Ingrese el día de la semana: ").strip().lower()

if dia_semana == "martes" or dia_semana == "jueves":
    descuento = monto_compra * 0.15
    total = monto_compra - descuento
    print("Descuento aplicado: ${:.2f}".format(descuento))
else:
    total = monto_compra

print("Total a pagar: ${:.2f}".format(total))