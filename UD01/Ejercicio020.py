# Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice su factura N! siendo el factorial:
# 0!=1
# 1!=1
# 2!=2*1
# …
# N!= N*(N-1)*(N-2)*…*1
def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)
