# Mi diccionario sera con las claves de todos los diccionarios 
# y si las que se repitan pues juntan sus valores en un lista y se queda solo una

def uneDiccionarios(*lista):
    dicionario_grande = {}
    for i in lista:
        for (key, value) in i.items():
            if key not in dicionario_grande:
                dicionario_grande[key] = [value]
            else:
                dicionario_grande[key].append(value)
    return dicionario_grande

def escribirDiccionarios(diccionario):
    for (key, value) in diccionario.items():
        print(key)
        print('        ', end='')
        for i in range(len(value)):
            if i == len(value)-1:
                print(value[i], end='')
            else:
                print(value[i], end=',')
        print()

dic = {"V":"S001"}
dic2 = {"V": "S002"}
dic3 = {"VI": "S001"}
dic4 = {"VI": "S005"}
dic5 = {"VII":"S005"}
dic6 = {"V":"S009"}
dic7 = {"VIII":"S007"}

diccionario_hijo = uneDiccionarios(dic, dic2, dic3, dic4, dic5, dic6, dic7)

escribirDiccionarios(diccionario_hijo)