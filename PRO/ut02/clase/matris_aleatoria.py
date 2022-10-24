import random

n_filas = input("Indica el numero de filas: ")
n_columnas = input("Indica el numero de columnas: ")
matriz = []

if n_columnas.isdigit() and n_filas.isdigit():
    n_filas = int(n_filas)
    n_columnas = int(n_columnas)
    for i in range(n_filas):
        matriz.append([])

    for i in matriz:
        for j in range(n_columnas):
            i.append(random.randint(0, n_columnas * n_filas))

    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()
else:
    print("Las columnas y filas tiene que ser un entero superior a 0")