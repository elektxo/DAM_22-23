#diseña una funcion en python que recibe parametros numericos
# y devuelve una lista con todos los parametros ordenador de manera ceciente

# en el programa principal la funcion recibira tantos parametros como lo indique un numero aleatorio entre 1 y 20

# los numeros a pasar son numeros entre 100 y 200

def ordenar(*args):
    for i in args:
        print(i)

#principal

ordenar(1,2,3,4,5)