from random import randint

def generar_carton():
    generado = ''
    for i in range(5):
        generado += str(random.randint(0, 99))
        if i < 4:
            generado += '-'
    return generado

def verificar_numero(numero, lista_string):
    lista = lista_string.split('-')
    for i in lista:
        if i == numero:
            return True
    return False

while True:
    print("""
        1. Generame un carton
        2. Verificar numero
        9. Salir
    """)
    op = input('Elije una opcion: ')
    match op:
        case '1':
            carton = generar_carton()
            print(carton)
        case '2':
            n = input('India el numero a verificar: ')
            if n.isdigit():
                n = int(n)
        case '9':
            print('Adios...')
            break