'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista comienzan en dígito primo.'''
try:
	lista=[]
	hasta=10
	cont = 0
	for i in range(0,hasta):
		num = int(input("Digite un numero: "))
		lista.append(num)
		j = 1
		while j < num:
			if (num // j == 2) or (num // j == 3) or (num // j == 5) or (num // j == 7):
				cont += 1
			j *= 10
	print(f"Hay {cont} numeros que empiezan en digito primo")


except ValueError:
	print("ERROR")