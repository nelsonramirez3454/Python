"""Leer 10 números enteros, almacenarlos en una lista y mostrar en pantalla todos los
enteros comprendidos entre 1 y cada uno de los números almacenados en la lista."""
try:
	lista = []
	lista2 = []
	var = 10

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)

		for j in range(len(lista,list)):
			lista2.append(j)
	print(lista)
		print(lista2)
except ValueError:
	print("digite un numero entero ")