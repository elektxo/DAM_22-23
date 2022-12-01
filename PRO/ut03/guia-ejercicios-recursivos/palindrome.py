def invertir(palabra, longuitud):
    if palabra == '':
        return ''
    a_devolver = invertir(palabra[1:], longuitud) + palabra[0]
    if len(a_devolver) == longuitud:
        if a_devolver == palabra:
            return True
        else:
            return False
    else:
        return a_devolver

# principal
string = 'libra'
print(invertir(string, len(string)))

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