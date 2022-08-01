"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántos datos
almacenados son múltiplos de 3."""
try:
	lista = []
	var = 10
	promedio = 0
	suma = 0
	contador = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
	for j in range(var):
		if lista[j] % 3 == 0:
			contador += 1
	print(f"hay {contador} multiplos de 3 almacenados en la lista")
	

except ValueError:
	print("digite un numero entero")