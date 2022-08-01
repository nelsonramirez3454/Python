'''realice un programa utilizando ciclos anidados que imprima las siguientes parejas:
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
3 0
3 1
3 2
4 0
4 1
4 2'''
try:

	for i in range(0,5):#empieza en cero termina en 5
		for j in range (0,3):#primero termina este ciclo y despues vuelve al otro
			print (i, j)

except ValueError:
	print ("Digite un valor valido")