"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces se repite
el promedio entero de los datos dentro de la lista."""
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
	print(f"el promedio se encuentra en la lista {contador} veces")
	

except ValueError:
	print("digite un numero entero")