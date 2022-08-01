"""elabore un algoritmo que almacene 10 numeros enteros en una lista, 
y en otra lista almacene el cubo de los numeros de la primera lista"""
try:
	lista = []
	lista2 = []
	var = 10

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)

	for j in range(len(lista)):
		cubo = lista[j] ** 3
		lista2.append(cubo)
	print(f"la lista de los numeros enteros es:{lista}")
	print(f"la lista al cubo de los numeros ingresados es:{lista2} ")
except ValueError:
	print("digite un numero entero ")