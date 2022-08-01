"""Leer 10 números enteros, almacenarlos en una lista y determinar cuáles son los datos
almacenados múltiplos de 3."""
try:
	lista = []
	var = 10
	listamultiplosde3 = []
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num % 3 == 0:
			listamultiplosde3.append(num)
	print(f"estos son los multiplos de 3 almacenados en la lista {listamultiplosde3}")


except ValueError:
	print("digite un numero entero")