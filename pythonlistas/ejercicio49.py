'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
terminan en dígito primo.'''
try:
	lista=[]
	hasta=10
	cont = 0
	for i in range(0,hasta):
		num = int(input("Digite un numero: "))
		lista.append(num)
		res = num % 10
		if (res == 2) or (res == 3) or (res == 5) or (res == 7):
			cont += 1

	print(f"hay {cont} numeros que terminan en dígito primo")

except ValueError:
	print("ERROR")