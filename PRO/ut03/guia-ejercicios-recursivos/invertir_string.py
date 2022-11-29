def invertir(palabra):
    if palabra == '':
        return ''
    return invertir(palabra[1:]) + palabra[0]

# principal

print(invertir('libra'))

'''
invertir('ibra') + l
invertir('bra') + i
invertir('ra') + b
invertir('a') + r
invertir('') + a

return a + r
return ar + b
return arb + i
return arbi + l
return arbil
'''