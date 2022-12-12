# Escribir un programa en python que defina la funcion matchDict(dic1, dic2)
# que encuentre los valores de clave repetidos en dos diccionarios que se 
# pasan como parametros

def matchDict(dic1, dic2):
    for clave, value in dic1.items():
        if clave in dic2:
            print(f'{clave} en dic1 = {value} en dic2 = {dic2[clave]}')

dict1 = {1:'uno', 2:'dos', 4:'cuatro'}
dict2 = {1:'a', 3:'c', 5:'e', 2:'b'}

matchDict(dict1, dict2)