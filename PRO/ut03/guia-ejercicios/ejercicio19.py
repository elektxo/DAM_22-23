def ganador(c1, c2, c3, meta):
    a_ganar = 0

    if int(c1) == int(meta):
        a_ganar = 1
    elif int(c2) == int(meta):
        a_ganar = 2
    elif int(c3) == int(meta):
        a_ganar = 3
    else:
        return 0

def contar(parametro):
    n_vocales = 0
    vocales = 'aeiouáéíóú'
    for i in parametro.lower():
        if i in vocales:
            n_vocales += 1
    return n_vocales

#principal

alianza1 = 3 #input('Indica numero de victorias de la alianza 1: ')
alianza2 = 4 #input('Indica numero de victorias de la alianza 2: ')
alianza3 = 2  #input('Indica numero de victorias de la alianza 3: ')

objetivo = 5 #input('Indica el valor de la meta: ')

resultado = ganador(alianza1, alianza2, alianza3, objetivo)

print(f'La alianza ganadora es la {resultado}')

palabra = 'esto_es_una_palabra'
print(f'El numero de vocales de la palabra es {contar(palabra)}')