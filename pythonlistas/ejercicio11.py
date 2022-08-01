"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
tienen, de los almacenados allí, menos de 3 dígitos."""
try:
	lista = []
	var = 10
	contador = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num < 100:
			contador += 1
	print(lista)
	print(f"los numeros que tienen menos de 3 digitos son: {contador}")
	

except ValueError:
	print("digite un numero entero")