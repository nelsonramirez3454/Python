"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones están
los números positivos."""
try:
	lista = []
	var = 10
	listaposicion = []
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num > 0:
			listaposicion.append(i)
	print(f"los numeros positivos se encuentran en las posiciones {listaposicion}") 

except ValueError:
	print("digite un numero entero")