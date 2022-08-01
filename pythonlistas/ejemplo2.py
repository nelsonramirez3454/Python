"""elabore un algosirtmo que almacene 15 numeros en un lista,
 imprimir el numero mayor y la posiciion donde se encuentra"""
try:
	lista = []
	var = 15
	mayor = 0
	posicion = 0
	for i in range(var):
		num = int(input("digite un numero"))
		lista.append(num)
		if num > mayor:
			mayor = num
			posicion = i + 1
	print(f"el numero mayor es: {mayor}")
	print(f"la posicion es: {posicion}")


	
except ValueError:
	print("digite un numero entero ")