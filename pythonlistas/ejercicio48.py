'''Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se
encuentra el número primo con mayor cantidad de dígitos pares.'''
try:
	lista=[]
	hasta=10
	mayor = 0
	p = 0
	for i in range(0,hasta):
		num = int(input("Digite un numero: "))
		lista.append(num)
		if ((2**(num-1))%num) == 1 or num == 2:
			cont = 0
			while num != 0:
				res = num // 10
				if res % 2 == 0:
					cont += 1
				num //= 10
			if cont > mayor:
				mayor = cont
				p = i
	if mayor != 0:
		print(f"El numero con la mayor cantidad de dígitos primos esta en la posicion {p}")
	else:
		print("No hay numeros primos")

except ValueError:
	print("ERROR")