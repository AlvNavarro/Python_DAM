# Calcular el perímetro y área de un rectángulo dada su base y su altura
base = int(input("Dame la base del rectangulo: "))
altura = int(input("Dame la altura del rectangulo: "))
area = base * altura
perimetro = 2*(base + altura)
print(f"Los resultados son: Perimetro = {perimetro} y Area = {area}")