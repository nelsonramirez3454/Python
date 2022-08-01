"""Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el
promedio entero de los factoriales de cada uno de los números leídos."""
try:
	lista = []
	lista2 = []
	var = 10
	suma = 0

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		fac = 1
		for j in range(1,num+1):
			fac *= j
		lista2.append(fac)
		suma += fac
	promedio = suma // 10
	print(f"la lista de los numeros enteros es:{lista}")
	print(f"el factorial de los numeros es:{lista2} ")
	print(f"el promedio factorial de los numeros es:{promedio} ")

except ValueError:
	print("digite un numero entero ")