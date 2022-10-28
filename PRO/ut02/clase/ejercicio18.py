from curses.ascii import isdigit
import random

lista = []
lista_coincidencias = []

tamano = input('Indica el tamaño de la lista: ')

if tamano.isdigit() and int(tamano)>0:
    tamano = int(tamano)
    n_terminal = input('Indique el numero es el que termine:')
    if n_terminal.isdigit():
        for i in range(tamano):
            lista.append(random.randint(1, 300))
        print('--- Lista original ---')
        for i in lista:
            print(i, end=' ')
        print()
        print('--- Lista de coincidencias ---')
        print()
        for i in lista:
            checker = True
            if len(str(i)) >= len(n_terminal):
                for j in range(len(n_terminal)):
                    if str(i)[::-1][j] != n_terminal[::-1][j]:
                        checker = False
            if checker:
                lista_coincidencias.append(i)
        for i in lista_coincidencias:
            print(i, end=' ')
    else:
        print('El numero terminal tiene que ser igual o superior a 0')
else:
    print('El tamaño de la lista tiene que se un numero superior a 0')