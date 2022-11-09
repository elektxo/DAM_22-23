menu = '''1. Agendar actividad
2. Borrar actividad
3. Listar actividades
9. Salir
'''

agenda = {}

while True:
    print(menu)
    opc = input('Elije una opcion: ')
    match opc:
        case "1":
            fecha = input('Indica fecha de la actividad: ')
            if fecha not in agenda:
                hora_inicio = input('Hora de inicio de la actividad: ')
                hora_fin = input('Hora de finalizacion de la actividad: ')
                actividad = input('Nombre de la actividad: ')
                agenda[fecha] = (hora_inicio, hora_fin, actividad)
            else:
                print('Ya hay una actividad en esa fecha')
        case "2":
            fecha = input('Indica la fecha de la actividad a borrar: ')
            if fecha in agenda:
                del agenda[fecha]
            else:
                print('No se encontro esa fecha en la agenda')
        case "3":
            for (key, value) in agenda.items():
                print(f'Fecha: {key} -- Descripcion: {value}')
        case "9":
            print('Adios...')
            break
        case _:
            print('Opcion desconocida')