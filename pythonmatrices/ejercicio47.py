'''Leer dos matrices 5x5 enteras y determinar si el promedio de los mayores números
primos por cada fila de una matriz es igual al promedio de los mayores números primos por
cada columna de la otra matriz.''' 
try:
	matrizUno = []
	matrizDos = []

	suma = 0
	print("Ingrese los datos de la matriz #1")
	for i in range(5):
		mayor = 0
		fila = []
		for j in range(5):
			contadorPrimo = 0
			numero = int(input("Ingrese un número entero: "))
			for x in range(2, numero):
				if (numero % x) == 0:
					contadorPrimo += 1
					break
			if (contadorPrimo == 0) and (numero != 0) and (numero != 1) and (numero > mayor):
				mayor = numero
			fila.append(numero)
		suma += mayor
		matrizUno.append(fila)
	promedioFilas = suma // 5

	print("Ingrese los datos de la matriz #2")
	for i in range(5):
		fila = []
		for j in range(5):
			numero = int(input("Ingrese un número entero: "))
			fila.append(numero)
		matrizDos.append(fila)

	suma = 0
	b = 0
	while (b <= 4):
		a = 0
		mayor = 0
		while (a <= 4):
			contadorPrimo = 0
			for x in range(2, matrizDos[a][b]):
				'''print(matrizDos[a][b])'''
				if (matrizDos[a][b] % x) == 0:
					contadorPrimo += 1
					break
			if (contadorPrimo == 0) and (matrizDos[a][b] != 0) and (matrizDos[a][b] != 1) and (matrizDos[a][b] > mayor):
				mayor = matrizDos[a][b]
			a += 1
		suma += mayor
		b += 1

	promedioColumnas = suma // 5

	print("La matriz #1 es:")
	for fila in matrizUno:
		print(fila)

	print("La matriz #2 es:")
	for fila in matrizDos:
		print(fila)

	print("Promedio de las filas de la matriz #1:",promedioFilas)
	print("Promedio de las columnas de la matriz #2:",promedioColumnas)

	if (promedioFilas == promedioColumnas):
		print("Por lo tanto, el promedio de la matriz #1 es igual al promedio de la matriz #2")
	else:
		print(" lo tanto, los promedios de las matrices son totalmente diferentes")

except ValueError:
	print("ERROR")