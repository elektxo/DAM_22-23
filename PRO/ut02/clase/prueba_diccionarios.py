personas = {}

while True:
    op = input('Indica el nombre de la persona o @ para salir: ')
    if op == '@':
        print('Adios...')
        break
    edad = input('Indica la edad de la persona: ')
    personas[op] = edad

print(personas)