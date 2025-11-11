# Ejercicio 23: Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
# el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
# se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
# según sea el caso y el total a pagar de la compra.

valor_compra = float(input("Ingrese el valor de compra: "))
tipo_pago = input("Ingrese el tipo de pago (contado/tarjeta): ")

if tipo_pago == "contado":
    descuento = valor_compra * 0.05
    total = valor_compra - descuento
    print("Descuento aplicado: ${:.2f}".format(descuento))
else:
    recargo = valor_compra * 0.03
    total = valor_compra + recargo
    print("Recargo aplicado: ${:.2f}".format(recargo))

print("Total a pagar: ${:.2f}".format(total))