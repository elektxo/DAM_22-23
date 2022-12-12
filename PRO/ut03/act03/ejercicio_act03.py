def suma(lista):
    if lista == []:
        return 0
    else:
        if type(lista[0]) == list:
            a_devolver = suma(lista[0])
        else:
            a_devolver = lista[0]
        return a_devolver + suma(lista[1:])

datos = [ 2, 3, [ 1, 2 ], 3, 5, [2, 3, 6, 10, 7], 3]

resultado = suma(datos)

print(resultado)