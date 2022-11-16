menu = """
1. Cantidad en segundo a horas, minutos y segundo
2. Cantidad en horas, minutos y segundo a segundo
3. Salir
"""
def segundo(tiempo):
    horas = 0
    minutos = 0
    segundos = 0
    if tiempo >= 3600:
        horas = tiempo // 3600
        tiempo = tiempo % 3600
    if tiempo >= 60:
        minutos = tiempo // 60
        tiempo = tiempo % 60
    segundos += tiempo
    return f'{horas}:{minutos}:{segundos}'

def horas(tiempo):
    segundos = 0
    if int(tiempo[0]) != 0:
        segundos += int(tiempo[0])*3600
    if int(tiempo[1]) != 0:
        segundos += int(tiempo[1])*60
    if int(tiempo[2]) != 0:
        segundos += int(tiempo[2])
    return segundos

#principal

while True:
    print(menu)
    op = input('Elije una opcion:')
    match op:
        case '1':
            segundos = input('Indica las segundo: ')
            print(segundo(int(segundos)))
        case '2':
            hora = input('Indica el tiempo: (hh,mm,ss)')
            print(horas(hora.split(',')))
        case '3':
            print('Adios...')
            break
        case _:
            pass