"""Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el
mayor número par leído."""
try:
	lista = []
	var = 10
	mayor = 0
	posicion = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num > mayor:
			mayor = num
			posicion = i + 1
	print(f"la lista es: {lista}")
	print(f"el numero mayor se encuentra en la posicio: {posicion}")


except ValueError:
	print("digite un numero entero")