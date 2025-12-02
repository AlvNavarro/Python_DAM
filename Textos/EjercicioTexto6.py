# Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas).

# Definir la cadena de ejemplo
frase = "Programacion_es_divertida"

print(f"Cadena original: {frase}\n")

# Extraer las primeras 6 letras (índices 0 a 5)
sub_1 = frase[:6] 
print(f"1. Las primeras 6 letras: '{sub_1}'") 
# Resultado: 'Progra'

# Extraer la palabra "divertida" (índices 16 hasta el final)
sub_2 = frase[16:]
print(f"2. La palabra 'divertida': '{sub_2}'") 
# Resultado: 'divertida'

# Extraer la palabra "es" (índices 13 y 14)
sub_3 = frase[13:15]
print(f"3. La palabra 'es': '{sub_3}'") 
# Resultado: 'es'

# Extraer la cadena de forma invertida
sub_4 = frase[::-1]
print(f"4. Cadena invertida: '{sub_4}'")
# Resultado: 'aditrevids_se_noicamargorP'