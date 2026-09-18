# Funcion para hacer la paritcion del arreglo
def partition(a, l, h):
    # Selecciona el elemento pivote
    pvt = a[h]
    # j es el índice de los elementos que son menores que
    # pivot y también índica la posición correcta del pivot encontrado hasta este momento
    j = l - 1
    # Recorre a[l..h-1] y mueve todos los elementos menores
    # al lado izquierdo del pivote
    # Los elementos de l a j son más pequeños despúes de cada iteración
    for k in range(l, h): # Recorre el arreglo
        # Si el elemento actual es menor que el pivote
        if a[k] < pvt: # Compara el elemento actual con el pivote
            j += 1 # Incrementa el indice del elemento pas pequeño
            swap(a, j, k) # Intercambia los elementos
    # Mover el pivote despues de elementos mas pequeños y
    # devolverlo a su posición
    swap(a, j + 1, h) # Intercambia el pivote con el elemento siguiente al ultimo elemento más pequeño
    return j + 1 # Devuelve el índice del pivote

# Funcion para intercambiar los elementos en el arreglo
def swap(a, j ,k): # intercambia los elementos
    a[j], a[k], = a[k], a[j] # intercambia los elementos
# Implementación de la funcion QuickSort
def qckSort(a, l, h): # Función principal de QuickSort
    if l < h: # Si el índice izquierdo es menor que el derecho
        # Pi es el indice de partición, regresa el indice del pivote
        pi = partition(a, l, h)
        # Llamadas recursivas para los elementos menores
        # Y mayores a iguales a los elementos
        qckSort(a, l, pi - 1) # Llamada recursiva para los elemntos menores que el pivote
        qckSort(a, pi + 1, h) # Llamada recursiva para los elementos mayores o iguales que el pivote

#Codigo para probar la implementacion de QuickSort
if __name__ == "__main__": # Punto de entrada del programa
    a = [10, 7, 8, 9, 1, 5]
    size = len(a)
    print("El arreglo antes de ordenarlo: ")
    for v in a: # Imprime el arreglo
        print(v, end=" ")
    print() # Salto de linea
    qckSort(a, 0, size - 1)
    print(" El arreglo después de ordenarlo: ")
    for v in a: # Imprime el arreglo ordenado
        print(v, end=" ")
