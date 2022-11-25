def multiplicacion_rusa(multiplicador, multiplicando):
    suma = 0
    if multiplicador%2==1:
        suma += multiplicando
    while multiplicador != 1:
        multiplicador = multiplicador//2
        multiplicando = multiplicando*2
        if multiplicador%2 == 1:
            suma += multiplicando
    return suma



x = int(input('Indica el multiplicador: '))
y = int(input('Indica el multiplicando: '))

resultado = multiplicacion_rusa(x, y)
print(resultado)
