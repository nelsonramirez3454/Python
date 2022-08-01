"""Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el
promedio entero de los datos de la lista."""
try:
	lista = []
	var = 10
	promedio = 0
	suma = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		suma += num
		promedio = suma / var

	print(f"el promedio de los datos de la lista es de:  {promedio}")
	

except ValueError:
	print("digite un numero entero")