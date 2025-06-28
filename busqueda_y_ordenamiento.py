import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = clave
    return arr

def busqueda_binaria(arr, x):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == x:
            return medio
        elif arr[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def medir_tiempo(func, lista, *args):
    inicio = time.time()
    resultado = func(lista, *args) if args else func(lista)
    fin = time.time()
    return resultado, fin - inicio

# =======================
# Pruebas del código
# =======================

print("\n*** Pruebas con listas pequeñas ***\n")

lista_pequeña = [random.randint(1, 100) for _ in range(10)]
print("Lista original:", lista_pequeña)

ordenada_bubble, tiempo_bubble = medir_tiempo(bubble_sort, lista_pequeña.copy())
print("Ordenada con Bubble:", ordenada_bubble)
print(f"Tiempo Bubble Sort: {tiempo_bubble:.6f} segundos\n")

ordenada_insertion, tiempo_insertion = medir_tiempo(insertion_sort, lista_pequeña.copy())
print("Ordenada con Insertion:", ordenada_insertion)
print(f"Tiempo Insertion Sort: {tiempo_insertion:.6f} segundos\n")

pos, tiempo_busqueda = medir_tiempo(busqueda_binaria, ordenada_insertion, lista_pequeña[3])
print(f"Buscando {lista_pequeña[3]} en la lista ordenada -> posición {pos}")
print(f"Tiempo Búsqueda Binaria: {tiempo_busqueda:.6f} segundos\n")

print("\n*** Pruebas con listas grandes ***\n")

lista_grande = [random.randint(1, 10000) for _ in range(5000)]

_, tiempo_bubble_grande = medir_tiempo(bubble_sort, lista_grande.copy())
print(f"Tiempo Bubble Sort con lista grande: {tiempo_bubble_grande:.6f} segundos")

_, tiempo_insertion_grande = medir_tiempo(insertion_sort, lista_grande.copy())
print(f"Tiempo Insertion Sort con lista grande: {tiempo_insertion_grande:.6f} segundos")
