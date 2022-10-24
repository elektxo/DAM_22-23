n_filas = input("Indica el numero de filas: ")
n_columnas = input("Indica el numero de columnas: ")
matriz = []

if n_columnas.lstrip('-').isdigit() and n_filas.isdigit():
    n_filas = int(n_filas)
    n_columnas = int(n_columnas)
    for i in range(n_filas):
        matriz.append([])

    for i in matriz:
        for j in range(n_columnas):
            while True:
                dato = input("Introduce un numero: ")
                if dato.isdigit():
                    i.append(int(dato))
                    break
                else:
                    print('Introduce un numero <= 0')
for i in matriz:
    print(i)