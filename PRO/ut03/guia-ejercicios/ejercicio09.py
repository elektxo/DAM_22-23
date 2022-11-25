def leer_datos():
    datos = []
    while True:
        x = input('Introduce dato o @ para salir: ')
        if x == '@':
            break
        datos.append(x)
    return datos


def superposicion(list1, list2):
    comunes = []
    for i in list1:
        if i in list2:
            comunes.append(i)
    return comunes

#principal
lista1 = leer_datos()
lista2 = leer_datos()

resultado = superposicion(lista1, lista2)

print(f'Los elementos comunes son {resultado}')
