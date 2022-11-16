import random
#jugador 2 🔴
#jugador 1 🟡
tablero = []
jugador = True

seguir_juego = True

for i in range(6):
    tablero.append([])
    for j in range(7):
        tablero[i].append('🔳')
print('Tus fichas son las amarillas')

while seguir_juego:
    for i in tablero:
        for j in i:
            print(j, end=' ')
        print()
    print('Tablero actual')

    turno = True
    while turno:
        if jugador:
            jugada = input('Jugador 1 indique de 1 a 7 su jugada: ')
            if jugada.isdigit():
                jugada = int(jugada)
                if jugada < 8 and jugada > 0:
                    if tablero[0][jugada-1] == '🔳':
                        jugador = False
                        turno = False
                        jugada -= 1
                        break
                    else:
                        print('La columana esta completa')
                else:
                    print('La jugada tiene que estar comprendida entre 1 y 7')
            else:
                print('Tiene que ser un numero la jugada')
        else:
            jugada = random.randint(0,6)
            if tablero[0][jugada] == '🔳':
                jugador = True
                turno = False
                break
            else:
                print('La columana esta completa')

    for i in range(6):
        if tablero[i][jugada] != '🔳':
            if jugador:
                tablero[i-1][jugada] = '🔴'
                break
            else:
                tablero[i-1][jugada] = '🟡'
                break
        else:
            if i == 5:
                if jugador:
                    tablero[i][jugada] = '🔴'
                    break
                else:
                    tablero[i][jugada] = '🟡'
                    break

    for i in range(6):
        for j in range(4):
            if tablero[i][j] == tablero[i][j+1] and tablero[i][j+1] == tablero[i][j+2] and tablero[i][j+2] == tablero[i][j+3] and tablero[i][j+3] != '🔳':
                if tablero[i][j] == '🔴':
                    print('Ha ganada el jugador 2')
                    seguir_juego = False
                else:
                    print('Ha ganada el jugador 1')
                    seguir_juego = False
    for i in range(3):
        for j in range(7):
            if tablero[i][j] == tablero[i+1][j] and tablero[i+1][j] == tablero[i+2][j] and tablero[i+2][j] == tablero[i+3][j] and tablero[i+3][j] != '🔳':
                if tablero[i][j] == '🔴':
                    print('Ha ganada el jugador 2')
                    seguir_juego = False
                else:
                    print('Ha ganada el jugador 1')
                    seguir_juego = False
    for i in range(3):
        for j in range(4):
            if tablero[i][j] == tablero[i+1][j+1] and tablero[i+1][j+1] == tablero[i+2][j+2] and tablero[i+2][j+2] == tablero[i+3][j+3] and tablero[i+3][j+3] != '🔳':
                if tablero[i][j] == '🔴':
                    print('Ha ganada el jugador 2')
                    seguir_juego = False
                else:
                    print('Ha ganada el jugador 1')
                    seguir_juego = False
    contador = 5
    for i in range(3):
        for j in range(4):
            if tablero[contador - i][j] == tablero[contador - i - 1][j+1] and tablero[contador - i - 1][j+1] == tablero[contador - i-2][j+2] and tablero[contador - i-2][j+2] == tablero[contador - i-3][j+3] and tablero[contador - i-3][j+3] != '🔳':
                if tablero[i][j] == '🔴':
                    print('Ha ganada el jugador 2')
                    seguir_juego = False
                else:
                    print('Ha ganada el jugador 1')
                    seguir_juego = False

    tablero_lleno = True
    for i in tablero:
        for j in i:
            if j == '🔳':
                tablero_lleno = False
    if tablero_lleno:
        print('El tablero esta lleno la partida acaba en empate')
        break