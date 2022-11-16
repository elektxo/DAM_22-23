viajeros = {'43843223W':['Adrian',['madrid', 'barcelona']], '12345678A':['Araceli', ['barcelona', 'caceres']], '87654321B':['Payo',['caceres', 'madrid']]}
paises = {'españa':['barcelona', 'madrid', 'caceres'], 'francia':['paris']}

while True:
    print("""
          (1) Agregar pasajeros a la lista de viajeros
          (2) Agregar ciudades la lista de ciudades
          (3) Dado el dni de un pasajero, ver a que ciudad a viajado
          (4) Dada una ciudad mostrar la cantidad de pasajeros (número) que van a esa ciudad
          (5) Dado el dni de una persona, ver a que países viaja
          (6) Dado un país decir cuantos pasajeros viajan a el y mostrar el nombre todos ellos
          (7) Salir del programa
          """)
    op = input('Indica que quieres hacer: ')
    match op:
        case "1":
            while True:
                dni = input('Indica el dni del pasajero a introducir: ')
                if dni not in viajeros:
                    nombre = input('Indica el nombre del pasajero a introducir: ')
                    lista_ciudades = []
                    while True:
                        esta = False
                        ciudad = input('Indica a que ciudad viaja')
                        for (pais, ciudades) in paises.items():
                            if ciudad in ciudades:
                                lista_ciudades.append(ciudad)
                                esta = True
                        if not esta:
                            print('No se pudo encontrar la ciudad indicada')
                        continuar = input('Desea seguir metiendo ciudades? (s/n, por omicion sera no) ')
                        if continuar != 's':
                            break
                else:
                    print('Ese dni ya esta en la lista')
                continuar = input('Desea introducir otro viajero? (s/n, por omicion sera no) ')
                if continuar != 's':
                    break
        case "2":
            pais = input('Indica el pais: ')
            if pais not in paises:
                paises[pais]=[]
            while True:
                ciudad = input('Indica que ciudad quiere agregar: ')
                if ciudad in paises[pais]:
                    print('Ya esta esa ciudad')
                else:
                    paises[pais].append(ciudad)
                continuar = input('Desea añadir mas ciudades? (s/n, por omicion sera no)')
                if continuar != 's':
                    break
        case "3":
            dni = input('Indica el dni del viajero a consultar: ')
            if dni in viajeros:
                for i in viajeros[dni][1]:
                    print(i)
            else:
                print('No se encontro el dni en la lista de viajeros')
        case "4":
            ciudad = input('Indica el nombre de la ciudad: ')
            n = 0
            for (key, value) in viajeros.items():
                for i in value[1]:
                    if i == ciudad:
                        n += 1
            print(f'A {ciudad} viajan {n} personas')
        case "5":
            dni = input('Indica el dni: ')
            listado = []
            if dni in viajeros:
                for i in viajeros[dni][1]:
                    for (key, value) in paises.items():
                        if i in value:
                            if not key in listado:
                                listado.append(key)
                print(f'A viajado a {listado}')
        case "6":
            n = 0
            pais = input('Indica el pais: ')
            if pais in paises:
                for (key, value) in viajeros.items():
                    for j in value[1]:
                        if j in paises[pais]:
                            n += 1
                            break
                print(f'A {pais} viajan {n} personas')
            else:
                print('No esta registrado ese pais')
        case "7":
            print('Adios...')
            break