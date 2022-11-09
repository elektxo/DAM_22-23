tablero = []

for i in range(7):
    tablero.append([])
    for j in range(6):
        tablero[i].append('*')
for i in tablero:
    print(i)

while True:
    jugada = input('Indica la columna de 0 a 5: ')
    if jugada.isdigit():
        jugada = int(jugada)
        if jugada >= 0 and jugada <= 5:
            pass
        else:
            print('La columna tiene que estar comprendida entre 0 y 5')
    else:
        print('La columna tiene que se un numero comprendido entre 0 y 5')