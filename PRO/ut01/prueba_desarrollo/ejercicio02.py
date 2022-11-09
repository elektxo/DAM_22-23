import random

bucle = True

while bucle:
    n_aleatorio = str(random.randint(1,20))
    for i in range(5):
        n_usuario = input(f'Introduzca número del intento {i+1}: ')
        if n_aleatorio == n_usuario:
            print(f'Enhorabuena…has adivinado el número en {i+1} intentos')
            break
        else:
            if i == 4:
                print(f'Ohhhh… no has adivinado el número. Este era el {n_aleatorio}')
    while bucle:
        op = input('Desea jugar de nuevo (s/n): ')
        match op:
            case 's':
                print('Vamos a jugar')
                break
            case 'n':
                bucle = False
                print('Adios...')
            case _:
                print('Opcion no encontrada, vuelva a intentarlo')