"""alamcenar una lista 20 numeros enteros, imprimir cuantos numeros son impares"""
try:
	lista = []
	var = 20
	contador = 0
	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		if num % 2 != 0:
			contador += 1

	print(f"la lista de los numeros ingresados son {lista}")
	print(f"la cantidad de numeros impares que hay en los numeros ingresados es de :{contador}")
except ValueError:
	print("digite un numero entero ")