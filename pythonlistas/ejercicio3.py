"""Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está el
mayor número primo leído."""
try:
	lista = []
	var = 10
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num % 2 != 0:
			mayor = num
			posicion = i + 1
	print(f"la lista de los numeros ingresados es: {lista}")
	print(f"la posicion del numero primo mayor es: {posicion}")

except ValueError:
	print("digite un numero entero")