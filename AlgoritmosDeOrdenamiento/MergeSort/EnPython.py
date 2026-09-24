def merge(a, l, m, r): # Merge dos subarrays de a[]
    a1 = m - l + 1 # Tamaño del primer subarray
    a2 = r - m # Tamaño del segundo subarray
    # Crear subarrays temporales
    L = [0] * (a1) # Crear subarray temporal
    R = [0] * (a2) # Crear subarray temporal
    # Copiar datos a los subarrays temporales L[] y R[]
    for j in range(0, a1): # Copiar datos al array temporal
        L[j] = a[l + j]
    for k in range(0, a2): # Copiar datos al array temporal
        R[k] = a[m + 1 + k]
    i = 0 # Indice inicial del primer subarray
    j = 0 # Indice inicial del segundo subarray
    k - l # Indice inicial del subarray mezclado
    # Mezclar los arrays temporales de nuevo en a[l..r]
    while i < a1 and j < a2: # Recorrer ambos arrays
        if L[i] <= R[j]: # Compara los elementos de ambos arrays
            a[k] = L[i] # Copiar el elemento más pequeño al array original
            i += 1 # Incrementar el índice del primer array
        else: # Si el elemento del segundo array es más pequeño
            a[k] = R[j] # Copiar el elemento más pequeño al array original
            j += 1 # Incrementar el índice del segundo array
        k += 1 # Incrementar el índice del array original
    # Copiar los elementos restantes de L[], si hay alguno
    while i < a1: # Recorrer el primer array
        a[k] = L[i] # Copiar el elemento al array original
        i += 1 # Incrementar el índice del primer array
        k += 1 # Incrementar el índice del array original
    # Copiar los elementos restantes de R[], si hay alguno
    while j < a2: # Recorrer el segundo array
        a[k] = R[j] # Copiar el elemento al array original
        j += 1 # Incrementar el índice del segundo array
        k += 1 # Incrementar el índice del array original
    # l es para el indice izquierdo, y r es para el indice derecho del subarray de 'a' a ser ordenado

    def mergeSort(a, l, r): # Función principal que implementa MergeSort
        if l < r:
            # Igual que (l+r)//2, pero evita el desbordamiento para grandes valores de l y h
            m = (l + (r - 1))//2
            # Ordenar la primera y segunda mitad
            mergeSort(a, l, m) # Ordenar la primera mitad
            mergeSort(a, m + 1, r) # Ordenar la segunda mitad
            merge(a, l, m, r) # Mezclar las dos mitades
    # Divide el array en dos mitades, las ordena y luego las mezcla
    
    # Código para probar la implementación de MergeSort
    a = [39, 28, 44, 11] # Arreglo desordenado
    s = len(a) # Tamaño del arreglo
    print("Antes de ordenar el arreglo: ") # Imprime el arreglo
    for j in range(s):
        print("%d" % a[j], end=" ")
    mergeSort(a, 0, s - 1) # Llama la funcion mergeSort
    print("\nDespués de ordenar el arreglo: ")
    for j in range(s):
        print("%d" % a[j], end=" ")