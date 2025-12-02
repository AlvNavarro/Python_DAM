"""
EjercicioTexto2 - Concatenación con el operador +

Demuestra cómo concatenar caracteres y cadenas de texto (strings)
utilizando el operador + en Python.
"""

def examples():
	"""Muestra varios ejemplos de concatenación con +"""
	# Concatenar caracteres individuales
	char_concat = 'a' + 'b'
	print("Concatenar caracteres: 'a' + 'b' ->", char_concat)

	# Concatenar cadenas (strings)
	greeting = 'Hola' + ' ' + 'Mundo'
	print("Concatenar cadenas: 'Hola' + ' ' + 'Mundo' ->", greeting)

	# Concatenar trozos para formar palabras
	word = 'Py' + 'thon'
	print("Formar palabra: 'Py' + 'thon' ->", word)

	# Concatenar números (convertir con str)
	age_concat = 'Edad: ' + str(25)
	print("Concatenar con números: 'Edad: ' + str(25) ->", age_concat)

print("Ejemplos de concatenación con el operador +:")
examples()