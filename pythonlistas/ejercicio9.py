"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántas veces está
repetido el mayor."""
try:
	lista = []
	var = 10
	mayor = 0
	contador = 1
	for i in range(var):
		num = int(input("ingrese un numero: "))
		lista.append(num)
		if num > mayor:
			mayor = num
		elif num == mayor:
			contador += 1
	print(f"el mayor es {mayor} y esta repetido {contador} veces")

	

except ValueError:
	print("digite un numero entero")