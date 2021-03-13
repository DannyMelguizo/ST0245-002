import timeit
import random
from time import time

def insertion_sort(array):
    nuevo_array = []
    longitud_array = range(1, len(array))
    for i in longitud_array:
        menor = array[i]
        while array[i-1] > menor and i > 0:
            temp = array[i]
            array[i] = array[i-1]
            array[i-1] = temp
            i = i - 1
    nuevo_array = array
    return nuevo_array

arreglo = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

inicio = timeit.default_timer()
insertion_sort(arreglo)
final = timeit.default_timer()

total = final - inicio

print(f'El tiempo en ejecutar el arreglo {arreglo} es: ',"{:.10f}".format(total),"ms")