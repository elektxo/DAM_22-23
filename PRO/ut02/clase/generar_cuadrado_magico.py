import random

n_columnas_filas = input("Indica el numero de columnas: ")
n_usados = []

if n_columnas_filas.isdigit():
    n_columnas_filas = int(n_columnas_filas)
    if n_columnas_filas > 0:

        while True:
            matriz = []
            checker = True
            for i in range(n_columnas_filas):
                matriz.append([])
            for i in matriz:
                for j in range(n_columnas_filas):
                    dato = random.randint(1, n_columnas_filas * n_columnas_filas)
                    if dato in n_usados:
                        while dato in n_usados:
                            dato = random.randint(1, n_columnas_filas * n_columnas_filas)
                    n_usados.append(dato)
                    i.append(dato)
            sumatotal = sum(matriz[0])
            for i in range(n_columnas_filas):
                suma = 0
                for j in range(n_columnas_filas):
                    suma += matriz[i][j]
                if suma == sumatotal:
                    for i in range(n_columnas_filas):
                        suma = 0
                        for j in range(n_columnas_filas):
                            suma += matriz[j][i]
                    if suma == sumatotal:
                        suma = 0
                        for i in range(n_columnas_filas):
                            suma += matriz[i][i]
                        if sumatotal == suma:
                            suma = 0
                            for i in range(n_columnas_filas):
                                suma += matriz[(n_columnas_filas-1)-i][i]
                        else:
                            checker = False
                    else:
                        checker = False
                else:
                    checker = False
            if checker:
                for i in matriz:
                    print(i)
                break