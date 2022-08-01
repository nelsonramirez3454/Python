"""leer 10 numeros enteros, almacenarlos en una lista y determinar en que posicion se encuentran los
numeros terminados en 4"""

try:
	lista = []
	var = 10
	posicion = 0
	contador = 0
	posicion1 = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num % 10 == 4:
			contador += 1
			posicion = i + 1 
			
	print(f"los numero terminados en 4 son: {contador}")
	print(f"y se encuentra en la posicion es: {posicion}")

	

except ValueError:
	print("digite un numero entero")


