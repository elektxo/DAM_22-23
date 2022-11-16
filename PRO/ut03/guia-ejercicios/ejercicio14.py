lista = ['hola', 'mundo', 'de', 'las', 'cositas']

#funciones

def longuitud_pila(pila):
    return len(pila)

def estaVacia(pila):
    if len(pila) == 0:
        return True
    return False

def estaLlena(pila):
    if longuitud_pila(pila) < 10:
        return False
    return True

def añadirElementoPila(pila, elemento):
    if not estaLlena(pila):
        pila.append(elemento)
    else:
        return

def sacarElementoPila(pila, elemento):
    pass

def verContenido(pila):
    return pila


#principal

menu = """
1 - Ver longuitud de la pila
2 - Ver si la pila esta vacie
3 - Ver si la pila esta llena
4 - Añadir elemento a la pila
5 - Sacar elemento de la pila
6 - Ver contenido de la pila
9 - Salir
"""

while True:
    print(menu)
    op = input('Elije una opcion: ')
    match op:
        case '1':
            print(longuitud_pila(lista))
        case '2':
            if estaVacia(lista):
                print('La pila esta vacia')
            else:
                print('La pila no esta vacia')
        case '3':
            if estaLlena(lista):
                print('La pila esta llena')
            else:
                print('La pila no esta llena')
        case '4':
            valor = input('Que quieres añadir? ')
            añadirElementoPila(lista, valor)
        case '5':
            sacarElementoPila(lista)
        case '6':
            print(verContenido(lista))
        case '9':
            print('Adios...')
            break
        case _:
            print('Opcion no encontrada')