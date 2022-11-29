def invertir(palabra, aux_palabra = ''):
    if palabra == '':
        a_devolver = ''
    else:
        a_devolver = invertir(palabra[1:]) + palabra[0]
    return a_devolver

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