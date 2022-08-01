"""Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el
mayor número leído."""
try:
	lista = []
	var = 10
	posicion = 0
	mayor = 0
	for i in range(var):
		num = int(input("digite un numero entero: "))
		lista.append(num)
		if num > mayor:
			mayor = num
			posicion = i + 1
	print(f"la lista de los numeros ingresados es: {lista}")
	print(f"el numero mayor se encuentra en la posicion: {posicion}")
except ValueError:
	print("digite un numero entero")