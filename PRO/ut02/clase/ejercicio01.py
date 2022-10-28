lista01 = [1,2,3,4]
lista02 = [2,0,9]
checker = False

if len(lista01)>= len(lista02):
    for i in lista01:
        if lista02.count(i) > 0:
            checker = True
            break
else:
    for i in lista02:
        if lista01.count(i) > 0:
            checker = True
            break

if checker:
    print('Se solapan')
else:
    print('No se solapan')