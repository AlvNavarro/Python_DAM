def jugar_adivinanza():
    limite_inferior = 1
    limite_superior = 100
    intentos = 0
    
    print("--- Juego Adivina el Numero ---")
    print("Piensa en un numero entero entre 1 y 100.")
    input("Presiona ENTER cuando estes listo...")
    
    while True:
        if limite_inferior > limite_superior:
            print("\n¡Parece que hubo un error o la respuesta no fue consistente! Reiniciando.")
            limite_inferior = 1
            limite_superior = 100
            intentos = 0
            continue

        propuesta = (limite_inferior + limite_superior) // 2
        intentos += 1
        
        print("-" * 30)
        print(f"Intento #{intentos}: ¿Es tu numero el {propuesta}?")
        
        respuesta = input("Introduce 'm' (menor), 'M' (mayor) o 'i' (igual): ").lower().strip()
        
        if respuesta == 'i':
            print(f"\n¡Lo adivine! Tu numero es el {propuesta}. Me tomo {intentos} intentos.")
            break
        
        elif respuesta == 'm':
            limite_superior = propuesta - 1
            print(f"Ajustando rango: {limite_inferior} a {limite_superior}")
            
        elif respuesta == 'M':
            limite_inferior = propuesta + 1
            print(f"Ajustando rango: {limite_inferior} a {limite_superior}")
            
        else:
            print("Respuesta invalida. Por favor, introduce 'm', 'M' o 'i'.")

jugar_adivinanza()