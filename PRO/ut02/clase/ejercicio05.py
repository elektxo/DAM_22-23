alumnos = [('pepe', 18), ('pedro', 13), ('juan', 21), ('reinaldo', 40), ('antonio', 55)]

while True:
    nombre = input('Introduce un nombre: ')

    if nombre == '*':
        break

    edad = input('Indica la edad: ')

    if edad.isdigit():
        edad = int(edad)
        alumnos.append((nombre, edad))
    else:
        print('Se ha introducido una edad erronea')

for i in alumnos:
    if i[1] >= 18:
        print(i[0], 'es mayor de edad')

print('🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸🇪🇸')

if len(alumnos) > 3:
    ordenados = sorted(alumnos, key=lambda mayores : mayores [1])
    for i in range(3):
        print(ordenados[::-1][i])