def listaOrdenada(lista):
    if len(lista) <= 1:
        return True
    return lista[0] <= lista[1] and listaOrdenada(lista[1:])

#principal

lista_random = [2,4,6]

print(listaOrdenada(lista_random))