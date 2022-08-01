"""Cargar una lista de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y
mostrarlo en pantalla."""
try:
	lista = []
	num1 = 0
	num2 = 1
	num3 = 0
	tope = 10

	for i in range(tope):
		
		while num2 < 83:
			num3 = num1 + num2
			num1 = num2
			num2 = num3
			lista.append(num3)
	
	print(lista)

except ValueError:
	print("digite un numero entero")