"""Leer dos números enteros y almacenar en una lista los 10 primeros números primos
comprendidos entre el menor y el mayor. Luego mostrarlos en pantalla."""
try:
	lista = []
	lista1 = []
	num1 = int(input("digite un numero"))
	num2 = int(input("digite otro numero"))

	if num1 > num2:
		for i in range(num2,num1):
			if (((2**(i-1))% i)== 1 or i == 2):
				lista.append(i)
		print(lista)
	else:
		for j in range(num1,num2):
			if (((2**(j-1))% j)== 1 or j == 2):
				lista1.append(j)
		print(lista1)

	

except ValueError:
	print("digite un numero entero")