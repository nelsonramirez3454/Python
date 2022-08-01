'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos de los números
almacenados en dicha lista pertenecen a los 100 primeros elementos de la serie de Fibonacci.'''
try:
	lista=[]
	fibonacci=[]
	hasta=10
	cont = 0

	a = 0
	b = 1
	c = 0
	fibonacci.append(a)
	for h in range(0,100):
		c = b+c
		b = a
		a = c
		fibonacci.append(a)
	for i in range(0,hasta):
		num = int(input("Digite un numero: "))
		lista.append(num)
		if num == 1: #lo puse por que el uno esta dos veces el la serie
		  num = 2
		for j in range(len(fibonacci)):
			if fibonacci[j] == num:
				cont += 1
	if cont > 0:
		print(f"Hay {cont} numeros en la lista que pertenecen a la serie de fibonacci")
	else:
		print("No hay numeros en la lista que pertenescan a la serie de fibonacci")

except ValueError:
	print("ERROR")