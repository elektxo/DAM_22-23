palabra01 = input('Introduce la primera palabra: ')
palabra02 = input('Introduce la segunda palabra: ')

caracteres = ''

for i in palabra01:
    if caracteres.count(i) == 0:
        caracteres += i
        match palabra02.count(i):
            case 0:
                print(f'{i} no esta en {palabra02}')
            case 1:
                print(f'{i} esta en {palabra02}')
            case _:
                print(f'{i} esta en {palabra02} {palabra02.count(i)} veces')