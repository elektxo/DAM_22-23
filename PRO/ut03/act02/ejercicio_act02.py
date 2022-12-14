from random import randint, choice

def tiro(lista, turno):
    primer_tiro = [1,2,3,4,5,6,7,8,9,'X','-']
    segundo_tiro = [1,2,3,4,5,6,7,8,9,'/','-']
    jugada_01 = choice(primer_tiro)
    if primer_tiro != 'X':
        jugada_02 = choice(segundo_tiro)
        lista.append((jugada_01, jugada_02))
    else:
        lista.append((jugada_01))
    lista[0] = (0, turno, 0)
    if turno > 1:
        pass
    return lista

puntuaciones = [(0,0,0)]

for i in range(1,11):
    puntuaciones = tiro(puntuaciones, i)
    print(puntuaciones)

print(puntuaciones)