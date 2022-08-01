'''Utilizando ciclos anidados generar las siguientes parejas de números

0 1
1 1
2 1
3 1
4 2
5 2
6 2
7 2'''
try:
	h = 0
	for i in range(1,3):
		for j in range(0,4):
			while h < 8:
				print (h, i)
				h += 1
				break
except ValueError:
	print ("ERROR")