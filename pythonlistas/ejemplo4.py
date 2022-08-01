"""elabore un algoritmo que almacene 20 numeros en una lista, imprima la sumatoria de los numeros de la lista"""
try:
	lista = []
	var = 20
	suma = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)

	for j in range(len(lista)):
		suma += lista[j]
	print(f"la lista de los numeros ingresados es: {lista}")
	print(f"la sumatoria de los numeros ingresados es: {suma}")
except ValueError:
	print("digite un numero entero ")