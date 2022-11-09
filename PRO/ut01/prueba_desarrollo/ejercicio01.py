palabra = input('Introduzca una palabra: ')

for i in range(len(palabra)):
    print(palabra[i::], end='')
    for j in range(i):
        print(palabra[j], end='')
    print()