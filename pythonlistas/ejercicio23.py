"""Leer 10 números enteros, almacenarlos en una lista y determinar si existe al menos un
número repetido."""
try:
	lista = []
	var = 10
	contador = 0
	numero = int(input("ingrese un numero: "))
	lista.append(numero)
	for i in range(var):
		num = int(input("ingrese un numero: "))
		lista.append(num)
		for j in range(0,i+1):
			if num == lista[j]:
				contador += 1
	if contador != 0:
		print("hay numeros repetidos")
	else:
		print("no hay numeros repetidos")
	

except ValueError:
	print("digite un numero entero")