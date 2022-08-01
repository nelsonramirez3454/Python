"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el
número con más dígitos."""
try:
	lista = []
	var = 10
	mayor = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		contador = 0
		while num != 0:
			respuesta = num % 10
			contador += 1
			num //= 10
		if contador >= mayor:
			mayor = contador
			posicion = i
	print(f"la posicion del numero con mas digitos es: {posicion} ")
	

except ValueError:
	print("digite un numero entero")