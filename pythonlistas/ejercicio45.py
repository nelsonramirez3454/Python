'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista comienzan por 34.'''
try:
	lista=[]
	hasta=10
	cont = 0
	for i in range(0,hasta):
		num = int(input("Digite un numero: "))
		lista.append(num)
		j = 1
		while j < num:
			if num // j == 34:
				cont += 1
			j *= 10
	print(f"Hay {cont} numeros que empiezan en 34")


except ValueError:
	print("ERROR")