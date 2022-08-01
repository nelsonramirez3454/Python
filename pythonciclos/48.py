'''Utilizando ciclos anidados generar las siguientes parejas de enteros

0 1
1 1
2 2
3 2
4 3
5 3
6 4
7 4
8 5
9 5'''
try:
	h = 0
	for i in range(1,6):
		for j in range(0,2):
			while h < 10:
				print (h, i)
				h += 1
				break
except ValueError:
	print ("ERROR")