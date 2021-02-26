def array_generator(len):
    return len

def array_sum(array):
    array_generator(array)
    suma = 0
    for i in array:
        suma = suma + i
    return suma

def array_mult(array, num):
    array_generator(array)
    array_new = []
    for i in array:
        array_new.append(i*num)
    return array_new

def insertion_sort(array):
    array_generator(array)
    longitud_array = range(1, len(array))
    for i in longitud_array:
        menor = array[i]
        while array[i-1] > menor and i > 0:
            temp = array[i]
            array[i] = array[i-1]
            array[i-1] = temp
            i = i - 1
    return array
#print(f"La suma de los elementos en el arreglo es: {array_sum([1,2,3,4,5,6,7,8,9,])}")
#print(f"El producto de los elementos en el arreglo es: {array_mult([1,2,3,4,5,6,7,8,9,], 5)}")
print(f"Al hacer un insertion sort en el arreglo, queda: {insertion_sort([17,8,70,100,1000,40,5,2,1])}")