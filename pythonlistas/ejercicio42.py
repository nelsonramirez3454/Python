"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números con
cantidad par de dígitos pares hay almacenados en dicha lista. """
try:
	lista = []
	var = 10
	contador = 0

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)

	for j in range(len(lista)):
		contador_par = 0
		if lista[j] % 2 == 0:
			contador += 1
			while lista[j] != 0:
				residuo = lista[j] % 10
				if residuo % 2 == 0:
					contador_par += 1
				lista[j] //= 10
		print(f"el {contador} par, tiene {contador_par} digitos")
except ValueError:
	print("digite un numero entero ")
