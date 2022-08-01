"""Leer 10 números enteros, almacenarlos en una lista y determinar cuáles son los números
múltiplos de 5 y en qué posiciones están."""
try:
	lista = []
	var = 10
	listamultiplosde5 = []
	listaposicion = []
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num % 5 == 0:
			listamultiplosde5.append(num)
			listaposicion.append(i)
	print(f"estos son los multiplos de 5 almacenados en la lista {listamultiplosde5}")
	print(f"Se encuentran ubicados en las posiciones  {listaposicion}")


except ValueError:
	print("digite un numero entero")