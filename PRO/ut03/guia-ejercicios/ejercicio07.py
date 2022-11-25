def convertirEspaciador(string):
    espaciada = ''
    for i in string:
        if i == ' ':
            pass
        else:
            espaciada += i+' '
    return espaciada


frase = input('Escribe una frase: ')

resultado = convertirEspaciador(frase)
print(resultado)
