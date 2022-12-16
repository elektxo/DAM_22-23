# ejercicio 03 del examen
#
# diccionario del personal de una empresa

personal = {
    'dic01':['Pedro', 'Pérez', 36, 'H'],
    'dic02':['María', 'Jiménez', 45, 'M'],
    'dic03':['Jesús', 'González', 22, 'H'],
    'dic04':['Luisa', 'García', 25, 'M'],
    'dic05':['Rosa', 'Suárez', 30, 'M']
}

def mayoresEdad(diccionario, edad):
    a_devolver = []
    for (clave, valor) in diccionario.items():
        if valor[2] > edad:
            a_devolver.append((valor[0],valor[1]))
    return a_devolver

def contarEmpleados(diccionario):
    n_mujeres = 0
    n_hombres = 0
    for (clave, valor) in diccionario.items():
        if valor[3] == 'M':
            n_mujeres += 1
        else:
            n_hombres += 1
    return n_mujeres, n_hombres, len(diccionario)

def  dividirEmpleados(diccionario):
    datos_mujeres = {}
    datos_hombres = {}
    for (clave, valor) in diccionario.items():
        if valor[3] == 'M':
            datos_mujeres[clave] = valor
        else:
            datos_hombres[clave] = valor
    return datos_mujeres, datos_hombres

while True:
    print(""" 
        1.- Ver los mayores
        2.- Contar empleados
        3.- Dividir empleados
        9.- Salir
    """)
    op = input('Elije una opcion: ')
    match op:
        case '1':
            anyos = input('Indica la edad: ')
            if anyos.isdigit():
                anyos = int(anyos)
                print(mayoresEdad(personal, anyos))
        case '2':
            resultado = contarEmpleados(personal)
            print(f'Mujeres: {resultado[0]}, hombres: {resultado[1]}, personas totales: {resultado[2]}')
        case '3':
            resultado = dividirEmpleados(personal)
            print(f'Mujeres: {resultado[0]}')
            print(f'Hombres: {resultado[1]}')
        case '9':
            print('Adios...')
            break