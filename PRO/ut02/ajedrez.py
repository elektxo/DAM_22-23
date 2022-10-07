tablero=[["⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜"], ["⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛"], ["⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜"], ["⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛"], ["⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜"], ["⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛"], ["⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜"], ["⬜", "⬛", "⬜", "⬛", "⬜", "⬛", "⬜", "⬛"]]
for i in range(0,8):
    for j in range(0,8):
        print(str(tablero[i][j]), end="")
    print()
ficha=input("Indique la ficha para colocar(T torre C caballo P peon # reyna R rey A alfil): ")
posicion=input("Posicion de la ficha que quiere colocar: ")
pos_fila = int(posicion.split(",")[0])
pos_columna=int(posicion.split(",")[1])
copia_pos_fila=pos_fila
copia_pos_columna=pos_columna
if pos_columna<=7 and pos_columna>=0 and pos_fila<=7 and pos_fila>=0:
    match ficha:
        case "T":
            for i in range(0,8):
                tablero[i][copia_pos_columna]="✅"
            for i in range(0,8):
                tablero[copia_pos_fila][i]="✅"
            tablero[copia_pos_fila][copia_pos_columna]="🏰"
        case "A":
            while copia_pos_fila<8 and copia_pos_columna<8:
                tablero[copia_pos_fila][copia_pos_columna]="✅"
                copia_pos_fila=copia_pos_fila+1
                copia_pos_columna=copia_pos_columna+1
            copia_pos_fila=pos_fila
            copia_pos_columna=pos_columna
            while copia_pos_fila<8 and copia_pos_columna>-1:
                tablero[copia_pos_fila][copia_pos_columna]="✅"
                copia_pos_fila=copia_pos_fila+1
                copia_pos_columna=copia_pos_columna-1
            copia_pos_fila=pos_fila
            copia_pos_columna=pos_columna
            while copia_pos_fila>-1 and copia_pos_columna<8:
                tablero[copia_pos_fila][copia_pos_columna]="✅"
                copia_pos_fila=copia_pos_fila-1
                copia_pos_columna=copia_pos_columna+1
            copia_pos_fila=pos_fila
            copia_pos_columna=pos_columna
            while copia_pos_fila>-1 and copia_pos_columna>-1:
                tablero[copia_pos_fila][copia_pos_columna]="✅"
                copia_pos_fila=copia_pos_fila-1
                copia_pos_columna=copia_pos_columna-1
            tablero[pos_fila][pos_columna]="♗ "
        case "#":
            for i in range(0,8):
                tablero[i][copia_pos_columna]="✅"
            for i in range(0,8):
                tablero[copia_pos_fila][i]="✅"
            copia_pos_fila=pos_fila
            copia_pos_columna=pos_columna
            while copia_pos_fila<8 and copia_pos_columna<8:
                tablero[copia_pos_fila][copia_pos_columna]="✅"
                copia_pos_fila=copia_pos_fila+1
                copia_pos_columna=copia_pos_columna+1               
            copia_pos_fila=pos_fila
            copia_pos_columna=pos_columna
            while copia_pos_fila<8 and copia_pos_columna>-1:
                tablero[copia_pos_fila][copia_pos_columna]="✅"
                copia_pos_fila=copia_pos_fila+1
                copia_pos_columna=copia_pos_columna-1
            copia_pos_fila=pos_fila
            copia_pos_columna=pos_columna
            while copia_pos_fila>-1 and copia_pos_columna<8:
                tablero[copia_pos_fila][copia_pos_columna]="✅"
                copia_pos_fila=copia_pos_fila-1
                copia_pos_columna=copia_pos_columna+1
            copia_pos_fila=pos_fila
            copia_pos_columna=pos_columna
            while copia_pos_fila>-1 and copia_pos_columna>-1:
                tablero[copia_pos_fila][copia_pos_columna]="✅"
                copia_pos_fila=copia_pos_fila-1
                copia_pos_columna=copia_pos_columna-1  
            tablero[pos_fila][pos_columna]="👸"
        case "P":
            tablero[pos_fila][pos_columna]="♟️ "
            if copia_pos_fila<7:
                if pos_fila==1:
                    tablero[copia_pos_fila+2][copia_pos_columna]="✅"
                tablero[copia_pos_fila+1][copia_pos_columna]="✅"
                if copia_pos_columna>0:
                    tablero[copia_pos_fila+1][copia_pos_columna-1]="✅"
                if copia_pos_columna<7:
                    tablero[copia_pos_fila+1][copia_pos_columna+1]="✅"
        case "R":
            tablero[pos_fila][pos_columna]="👑"
            if pos_fila<7:
                tablero[pos_fila+1][pos_columna]="✅"
                if pos_columna<7:
                    tablero[pos_fila+1][pos_columna+1]="✅"
            if copia_pos_columna<7:
                tablero[pos_fila][pos_columna+1]="✅"
                if pos_fila>0:
                    tablero[pos_fila-1][pos_columna+1]="✅"
            if pos_fila>0:
                tablero[pos_fila-1][pos_columna]="✅"
                if pos_columna>0:
                    tablero[pos_fila-1][pos_columna-1]="✅"
            if pos_columna>0:
                tablero[pos_fila][pos_columna-1]="✅"
                if pos_fila<7:
                    tablero[pos_fila+1][pos_columna-1]="✅"
        case "C":
            tablero[pos_fila][pos_columna]="🐴"
            if pos_fila<6:
                if pos_columna<7:
                    tablero[pos_fila+2][pos_columna+1]="✅"
                if pos_columna>0:
                    tablero[pos_fila+2][pos_columna-1]="✅"
            if pos_fila>1:
                if pos_columna<7:
                    tablero[pos_fila-2][pos_columna+1]="✅"
                if pos_columna>0:
                    tablero[pos_fila-2][pos_columna-1]="✅"
            if pos_columna<6:
                if pos_fila<7:
                    tablero[pos_fila+1][pos_columna+2]="✅"
                if pos_fila>0:
                    tablero[pos_fila-1][pos_columna+2]="✅"
            if pos_columna>1:
                if pos_fila<7:
                    tablero[pos_fila+1][pos_columna-2]="✅"
                if pos_fila>0:
                    tablero[pos_fila-1][pos_columna-2]="✅"
        case _:
            print("No se encontro la ficha")
else:
    print("La coordenada está fuera del tablero")
for i in range(0,8):
    for j in range(0,8):
        print(str(tablero[i][j]), end="")
    print()