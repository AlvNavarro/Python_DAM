# Ejercicio 26: Escriba un programa que calcula el salario neto semanal de un trabajador en función del número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
# • Las primeras 35 horas se pagan a tarifa normal.
# • Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
# • Las tasas de impuesto son:
#    •   Los primeros 500€ son libres de impuestos.
#    •   Los siguientes 400€ tiene un 25% de impuesto.
#    •   Los restantes un 45% de impuesto.
# Escribe el nombre del trabajador, salario bruto, tasas y salario neto
nombre = input ("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
tarifa_hora = float(input("Ingrese la tarifa por hora: "))
if horas_trabajadas <= 35:
    salario = horas_trabajadas * tarifa_hora
else:
    horas_extra = horas_trabajadas - 35
    salario = (35 * tarifa_hora) + (horas_extra * tarifa_hora * 1.5)
if salario <= 500:
    impuesto = 0
elif salario <= 900:
    impuesto = (salario - 500) * 0.25
else:
    impuesto = (400 * 0.25) + (salario - 900) * 0.45
salario_neto = salario - impuesto
print("Nombre del trabajador:", nombre)
print("Salario bruto:", salario)
print("Impuesto:", impuesto)
print("Salario neto:", salario_neto)