"""Leer 10 números enteros, almacenarlos en una lista y determinar cuál es el número
menor."""
try:
	lista = []
	var = 10
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
	print("el numero menor es:")
	print(min(lista))

except ValueError:
	print("digite un numero entero")