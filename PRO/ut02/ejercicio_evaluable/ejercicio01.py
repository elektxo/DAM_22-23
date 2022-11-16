clientes = []
ventas = []

while True:
    print("""
    (1) Añadir cliente
    (2) Eliminar cliente
    (3) Añadir factura
    (4) Procesar facturacion del mes
    (5) Lista clientes
    (6) Terminar
          """)
    op = input('Elije una opcion: ')
    print()
    match op:
        case '1':
            nombre = input('Indica el nombre del cliente: ')
            validador = True
            for i in clientes:
                if i[0] == nombre:
                    print('El clientes ya existe')
                    validador = False
            if validador:
                cif = input('Indica el cif: ')
                direccion = input('Indica la direccion: ')
                clientes.append((nombre, cif, direccion))
        case '2':
            nombre = input('Indica el nombre del cliente a eliminar: ')
            cliente_factura = False
            for i in clientes:
                if i[0] == nombre:
                    for j in ventas:
                        if nombre == j[0]:
                            cliente_factura = True
                    if cliente_factura:
                        print('No se puede eliminar, este cliente esta en una factura')
                    else:
                        clientes.remove(i)
        case '3':
            nombre = input('Indica el nombre del cliente para la factura: ')
            for i in clientes:
                if i[0] == nombre:
                    dia = input('Indica el dia de la factura: ')
                    if dia.isdigit():
                        dia = int(dia)
                        if dia < 31 == dia > 0:
                            importe = input('Indica el importe de la factura, con punto: ')
                            if importe.isdigit() or '.' in importe:
                                if importe.isdigit():
                                    importe = int(importe)
                                    ventas.append((nombre, dia, importe))
                                else:
                                    if len(importe.split('.')) == 2:
                                        if importe.split('.')[0].isdigit() and importe.split('.')[1].isdigit():
                                            importe = float(importe)
                                            ventas.append((nombre, dia, importe))
                            else:
                                print('Importe mal introducido, operacion abortada')
                        else:
                            print('El dia tiene que estar comprendido entre 1 y 30')
        case '4':
            for i in clientes:
                facturacion_del_mes = 0.0
                for j in ventas:
                    if i[0] == j[0]:
                        facturacion_del_mes += j[2]
                print(f'{i[0]} a facturado {facturacion_del_mes}')
        case '5':
            for i in clientes:
                for j in i:
                    print(j, end=' ')
                print()
        case '6':
            print("Adios...")
            break
