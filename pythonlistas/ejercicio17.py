"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
negativos hay."""
try:
	lista = []
	var = 10
	contador = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num < 0:
			contador += 1
	print(f"hay {contador} numeros negativos") 

except ValueError:
	print("digite un numero entero")