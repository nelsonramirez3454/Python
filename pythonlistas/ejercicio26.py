"""Leer 10 números enteros, almacenarlos en una lista y calcularle el factorial a cada uno de
los números leídos almacenándolos en otra lista."""
try:
	lista = []
	lista2 = []
	var = 10
	


	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		fac = 1
		for j in range(1,num+1):
			fac *= j
		lista2.append(fac)
	print(f"la lista de los numeros enteros es:{lista}")
	print(f"el factorial de los numeros es:{lista2} ")
except ValueError:
	print("digite un numero entero ")