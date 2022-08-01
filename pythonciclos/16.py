'''
16. Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número
n leído.
'''
try:
    num=int(input("Digite un numero de múltiplos de 3: "))
    suma = 0
    multiplo = 0
    for i in range(1,num+1):
        multiplo += 3
        suma += multiplo
    promedio = suma / num
    print  (promedio)
except ValueError:
    print ('ERROR')