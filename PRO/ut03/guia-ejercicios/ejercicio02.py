menu = """
1. ºC a ºF
2. ºC a ºK
3. ºK a ºC
4. ºK a ºF
5. ºF a ºC
6. ºF a ºK
9. Salir
"""

def deCaF(gradosC):
    final = gradosC * 1.8 + 32
    return final

def deCaK(gradosC):
    final = gradosC + 273.15
    return final

def deKaC(gradosK):
    final = gradosK - 273.15
    return final

def deKaF(gradosK):
    final = (gradosK - 273.15) * 1.8 + 32
    return final

def deFaC(gradosF):
    final = (gradosF - 32) / 1.8
    return final

def deFaK(gradosF):
    final = ((gradosF - 32) / 1.8) + 273.15
    return final

#principal
while True:
    print(menu)
    op = input('Indica una opcion: ')
    match op:
        case '1':
            grados = input('Indica los grados: ')
            print(deCaF(int(grados)))
        case '2':
            grados = input('Indica los grados: ')
            print(deCaK(int(grados)))
        case '3':
            grados = input('Indica los grados: ')
            print(deKaC(int(grados)))
        case '4':
            grados = input('Indica los grados: ')
            print(deKaF(int(grados)))
        case '5':
            grados = input('Indica los grados: ')
            print(deFaC(int(grados)))
        case '6':
            grados = input('Indica los grados: ')
            print(deFaK(int(grados)))
        case '9':
            print('Adios...')
            break