"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el
número cuya suma de dígitos sea la mayor."""
try:
	lista = []
	var = 10
	mayor = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		suma = 0
		while num != 0:
			respuesta = num % 10
			suma += respuesta
			num //= 10
		if suma > mayor:
			mayor = suma
			posicion = i
	print(f"la posicion del numero cuya suma de digitos es mayor: {posicion} y la suma es {mayor}")
	

except ValueError:
	print("digite un numero entero")