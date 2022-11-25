L = [ [1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9] ]

cantidad_maxima = sum(L[0])

for i in L:
    if sum(i) > cantidad_maxima:
        cantidad_maxima = sum(i)

print(f'La lista suma mayor es {cantidad_maxima} y las lista que lo cumlen son: ')

for i in L:
    if sum(i) == cantidad_maxima:
        print(i)
