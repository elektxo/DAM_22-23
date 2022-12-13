def tiro(lista, turno):
    jugada = input('Indica tu jugada: ')
    

puntuaciones = [(0,0,0)]

for i in range(1,11):
    puntuaciones = tiro(puntuaciones, i)
    print(puntuaciones)