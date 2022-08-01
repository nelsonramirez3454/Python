""" Leer 10 números enteros, almacenarlos en una lista y determinar si la semisuma entre el
valor mayor y el valor menor es un número par. """
try:
	lista = []
	var = 10
	suma = 0
	semisuma = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
	suma = min(lista)+max(lista)
	semisuma = suma / 2
	print(f"la semisuma es: {semisuma}")
	if semisuma % 2 == 0:
		print(f"la semisuma es un numero par")
	else:
		print(f"la semisuma NO es un numero par")

except ValueError:
	print("digite un numero entero ")