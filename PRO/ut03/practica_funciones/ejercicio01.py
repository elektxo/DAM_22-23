import random

def generarClave(valores, tamañoclave):
    clave = []
    for i in range(tamañoclave):
        clave.append(random.choice(valores))
    return clave

def compruebaIntento(clave, intento):
    pistas = []
    copia_clave = clave[::-1]
    for i in range(5):
        if clave[i] == intento[i]:
            pistas.append('*')
            copia_clave.pop()
        else:
            if copia_clave.count(intento[i]) > 0:
                pistas.append('+')
                copia_clave.pop(copia_clave.index(intento[i]))
            else:
                pistas.append('?')

    return pistas

tupla = ('a', 'b', 'c', 'd', '1', '2', '3', '4')

intentos = 0

clave = generarClave(tupla, 5)

while intentos < 10:
    prueba = input('Indica tu intento (Ejemplo: 1,2,3,4,a): ')
    if len(prueba.split(',')) == 5:
        intentos += 1
        resultado = compruebaIntento(clave, prueba.split(','))
        print(resultado)
        if resultado.count('*') == 5:
            print('Has acertado')
            intentos = 10
        else:
            print('Pruebe otra vez')
    else:
        print('El intento tiene que tener 5 elementos.')