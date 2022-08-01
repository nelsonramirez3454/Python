"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentran los números con más de 3 dígitos."""
try:
	lista = []
	var = 10
	listaPosicion = []
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num > 99:
			listaPosicion.append(i)
	print(lista)
	print(f"los numeros con mas de tres digitos se encuentran en las posiciones {listaPosicion}")


	

except ValueError:
	print("digite un numero entero")