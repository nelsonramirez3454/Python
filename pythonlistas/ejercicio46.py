'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista son primos y comienzan por 5.'''
try:
	lista=[]
	hasta=10
	cont = 0
	for i in range(0,hasta):
		num = int(input("Digite un numero: "))
		lista.append(num)
		if ((2**(num-1))%num) == 1 or num == 2:
			j = 1
			while j < num:
				if num // j == 5:
					cont += 1
				j *= 10
	print(f"Hay {cont} numeros que empiezan en 5 y son primos")


except ValueError:
	print("ERROR")