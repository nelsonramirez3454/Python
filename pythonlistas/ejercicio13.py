"""Leer 10 números enteros, almacenarlos en una lista y determinar si el promedio entero
de estos datos está almacenado en la lista."""
try:
	lista = []
	var = 10
	promedio = 0
	suma = 0
	contador = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		suma += num
		promedio = suma / var
	print(f"el promedio de los datos de la lista es de:  {promedio}")
	for j in range(var):
		if lista[j] == promedio:
			contador += 1
	if contador > 0:
		print("el promedio esta dentro de la lista")
	else:
		print("el promedio NO se encuentra dentro de la lista")

except ValueError:
	print("digite un numero entero")