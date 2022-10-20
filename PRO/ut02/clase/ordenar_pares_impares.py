lista = []
lista_impares = []

while True:
    dato = input("Introduce un numero: ")
    if dato == "*":
        break
    if dato.lstrip('-').isdigit():
        lista += [int(dato)]
    else:
        print("Eso no es un numero")

for i in lista:
    if i%2 != 0:
        lista_impares += [i]

for i in lista_impares:
    lista.remove(i)
    lista += [i]

for i in lista:
    print(i, end=" ")