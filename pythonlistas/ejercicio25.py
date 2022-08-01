"""Leer 10 números enteros, almacenarlos en una lista y determinar cuántos de los números
leídos son números primos terminados en 3."""
try:
	lista = []
	var = 10
	listaprimo = []
	contador = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if (((2**(num-1))% num)== 1 or num == 2):
			if num % 10 == 3:
				contador += 1	
	print(f"los numeros primos terminados en 3 son:{contador} ")

	

except ValueError:
	print("digite un numero entero")