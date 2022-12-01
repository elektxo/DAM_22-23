def contarVocales(palabra):
    if palabra == '':
        a_devolver = 0
    else:
        match palabra[0]:
            case 'a'|'e'|'i'|'o'|'u'|'á'|'é'|'í'|'ó'|'ú':
                es_vocal = 1
            case _:
                es_vocal = 0
        a_devolver = es_vocal+contarVocales(palabra[1:])
    return a_devolver

#principal

string = 'manuela'

print(f'La palabra {string} tiene {contarVocales(string.lower())} vocales')