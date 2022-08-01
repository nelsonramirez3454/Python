"""leer 10 numeros enteros, almacenarlos en una lista y determinar en que posicion se encuentra el mayor"""

try:
	lista = []
	var = 10
	mayor = 0
	posicion = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num > mayor:
			mayor = num
			posicion = i + 1
	print(f"el mayor es: {mayor}")
	print(f"y se encuentra en la posicion es: {posicion}")

	

except ValueError:
	print("digite un numero entero")


