try:
    A = float(input("Ingrese la base (A): "))
    B = int(input("Ingrese el exponente (B, debe ser entero no negativo): "))
    
    if B < 0:
        print("El exponente (B) debe ser un numero entero no negativo para este calculo.")
    elif B == 0:
        resultado = 1
        print(f"\nEl resultado de {A} elevado a {B} es: {resultado}")
    else:
        resultado = 1.0 
        
        for _ in range(B):
            resultado *= A
            
        print(f"\nEl resultado de {A} elevado a {B} es: {resultado}")

except ValueError:
    print("Error: Ingrese valores numericos validos.")