try:
	lista = []
	var = 10

	for i in range(var):
		num = int(input("digite un numero: "))
		lista.append(num)
		for j in range(0,var):
			while num != 0:
				res = num % 10
				for k in range(1,res+1):
					print(k)
				num //= 10

except ValueError:
	print("digite un numero entero ")