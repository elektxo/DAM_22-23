abc = {}
abcedario = 'abcefghijklmnñopqrstuvwxyz'
frase = input('Escribe una frase: ').lower().replace(' ', '')

for i in frase:
    valor_dvto = abc.setdefault(i, 0)
    abc[i] += 1

