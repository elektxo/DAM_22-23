#invertir diccionario
diccionario_ejemplo ={'key1':'value1', 'key2':'value2', 'key3':'value1'}

def invertir(dato):
    new_dic ={}
    for (key, value) in dato.items():
        if value not in new_dic:
            new_dic[value] = [key]
        else:
            new_dic[value].append(key)
    return new_dic


#principal

resultado = invertir(diccionario_ejemplo)

print(f'Diccionario original: {diccionario_ejemplo}')
print(f'Diccionario invertido: {resultado}')
