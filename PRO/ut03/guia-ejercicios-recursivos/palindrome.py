def invertir(palabra, longuitud=0):
    if longuitud == 0:
        longuitud = len(palabra)
    if palabra == '':
        if palabra == '' and longuitud == 0:
            return True
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