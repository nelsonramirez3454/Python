"""Leer 10 números enteros, almacenarlos en una lista y determinar a cuántos es 
igual el
cuadrado de cada uno de los números leídos. """
try:
	lista = []
	lista1 = []
	var = 10
	cuadrado = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
	print(lista)
	for j in range(var):
		cuadrado = num ** 2
		lista1.append(cuadrado)
	print(lista1)
except ValueError:
	print("digite un numero entero ")