lista = [1, 1, 1, 3, 5, 1, 1, 3, 3, 8, 8, 8, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1,1] 

lista_empaquetada = []
aux = [0,0]
contador = 0

for i in lista:
    if i != aux[0] and aux[1] != 0:
        lista_empaquetada.append((aux[0], aux[1]))
    if i != aux[0]:
        aux[0] = i
        aux[1] = 0
    aux[1] += 1
    contador += 1
lista_empaquetada.append((aux[0], aux[1]))




for i in range(len(lista_empaquetada)):
    print(lista_empaquetada[i], end=" ")
    if (i+1)%5 == 0:
        print()
    else: 
        if i != len(lista_empaquetada)-1:
            print('-', end=" ")
