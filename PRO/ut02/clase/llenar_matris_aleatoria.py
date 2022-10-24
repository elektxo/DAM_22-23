import random

n_filas = input("Indica el numero de filas: ")
n_columnas = input("Indica el numero de columnas: ")
matriz = []
n_usados = []

if n_columnas.isdigit() and n_filas.isdigit():
    n_filas = int(n_filas)
    n_columnas = int(n_columnas)
    for i in range(n_filas):
        matriz.append([])

    for i in matriz:
        for j in range(n_columnas):
            dato = random.randint(0, n_columnas * n_filas)
            if dato in n_usados:
                while dato in n_usados:
                    dato = random.randint(0, n_columnas * n_filas)
            n_usados.append(dato)
            i.append(dato)

    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()
else:
    print("Las columnas y filas tiene que ser un entero superior a 0")