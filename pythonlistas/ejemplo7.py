"""elabore un programa que almacene 15 elementos en una lista, en una lista almacene los numeros pares
de la lista original, y en una lista b almacene los numeros impares de la lista original, imprima las tres listas"""
try:
	lista = []
	lista2 = []
	lista3 = []
	var = 15

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num % 2 == 0:
			lista2.append(num)
		else:
			lista3.append(num)
	print(f"la lista original es: {lista}")
	print(f"la lista de los numeros pares es: {lista2}")
	print(f"la lista de los numeros impares es: {lista3}")



except ValueError:
	print("digite un numero entero ")