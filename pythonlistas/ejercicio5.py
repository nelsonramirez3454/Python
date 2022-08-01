"""Almacenar en una lista de 10 posiciones los 10 primeros números primos comprendidos
entre 100 y 300. Luego mostrarlos en pantalla."""
try:
	lista = []
	for i in range(100,150):
		if (((2**(i-1))% i)== 1 or i == 2):
			lista.append(i)
	print(lista)
	
except ValueError:
	print("digite un numero entero")