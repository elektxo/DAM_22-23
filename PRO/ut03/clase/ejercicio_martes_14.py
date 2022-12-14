# Escribe una funcion valoresIguales(dicc) que retorn True
# si todos los valores del diccionario son iguales

# Retorna False en case contrario

def valoresIguales(dicc):
    iguales = True
    dato = list(dicc.values())[0]
    for (clave, valor) in dicc.items():
        if valor != dato:
            iguales = False
    return iguales

diccionario01 = {1:'*', 2:'*', 3:'*'}
diccionario02 = {1:'+', 2:'*', 3:'+', 4:'@', 5:'@'}

print(valoresIguales(diccionario01))