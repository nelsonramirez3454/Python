"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está el
menor número primo."""
try:
	lista = []
	var = 10
	listaprimo = []
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if (((2**(num-1))% num)== 1 or num == 2):              
			listaprimo.append(num)
	print("el menor numero primo es: ")
	print(min(listaprimo))

except ValueError:
	print("digite un numero entero")