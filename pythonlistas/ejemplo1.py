""""""
try:
	lista = []
	var = 10

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
	print(f"la lista de los numeros ingresados son {lista}")
except ValueError:
	print("digite un numero entero ")