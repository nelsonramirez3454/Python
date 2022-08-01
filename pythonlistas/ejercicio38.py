""" Leer 10 números enteros, almacenarlos en una lista y determinar si la semisuma
entre el
valor mayor y el valor menor es un número primo. """
try:
	lista = []
	lista2 = []
	listaSuma = []
	var= 30
	for i in range(var):
		num1 = int(input("digite un numero: "))
		lista.append(num1)
	for g in range(var):
		num2 = int(input("digite un numero: "))
		lista2.append(num2)
	for h in range(var):
		suma= 0
		suma=lista[h] + lista2[h]
		listaSuma.append(suma)
	print(listaSuma)
except ValueError:
	print("digite un numero entero ")