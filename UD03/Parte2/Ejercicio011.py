try:
    altura=int(input("Introduce la altura de la escalera: "))
    if altura <=0:
        raise ValueError
except ValueError:
    print("Error: Debes introducir un número entero.")
else:
    asterisco = "*"
    for i in range (1,altura+1):
        print("*" * i)