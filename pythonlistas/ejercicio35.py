"""Leer 10 números enteros, almacenarlos en una lista y determinar si el 
promedio entero
de dichos números es un número primo. """
try:
	lista = []
	var = 10
	promedio = 0
	suma = 0
	for i in range(var):
		num = int(input("digite un numero entero"))
		lista.append(num)
		suma += num
		promedio = suma // var
	if (((2**(promedio-1))% promedio)== 1 or promedio == 2):
		print(f"el promedio es {promedio} y es un numero primo")
	else:
		print(f"el promedio es {promedio} y NO es un numero primo")
except ValueError:
	print("digite un numero entero")
	