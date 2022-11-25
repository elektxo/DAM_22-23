# Diseñe una función de nombre “la_mas_larga()” que recibe un número indeterminado de parámetros que
# representan palabras para buscar entre ellas la más larga. La función debe retornar dos valores, el primero la
# longitud de la palabra más larga y el segundo una lista donde esta/están la o las palabras más largas de todas las
# recibidas, tenga en cuenta que puede ser más de una. La lista de palabras que se retorna debe estar ordenada
# alfabéticamente.

def la_mas_larga(lista):
    longitud = len(lista[0])
    for i in lista:
        if longitud < len(i):
            longitud = len(i)
    lista_largas = []
    for i in lista:
        if longitud == len(i):
            lista_largas.append(i)
    return longitud, lista_largas

#principal

parametros = []

while True:
    x = input('Introduce una palabra o @ para salir: ')
    if x == '@':
        break
    parametros.append(x)

resultado = la_mas_larga(parametros)

print(resultado)