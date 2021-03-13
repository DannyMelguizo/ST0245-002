import timeit
def merge_sort(array):
    if len(array) > 1:
        mitad = len(array) // 2
        izquierda = array[:mitad]
        derecha = array[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = 0
        j = 0
        k = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
              array[k] = izquierda[i]
              i += 1
            else:
                array[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            array[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            array[k] = derecha[j]
            j += 1
            k += 1

arreglo = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

inicio = timeit.default_timer()
merge_sort(arreglo)
final = timeit.default_timer()

total = final - inicio

print(f'El tiempo en ejecutar el arreglo {arreglo} es: ',"{:.10f}".format(total),"ms")