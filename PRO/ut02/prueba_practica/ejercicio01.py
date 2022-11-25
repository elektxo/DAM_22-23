# Ejercicio 01 de Estructuras de datos

Facturas = { ("cte-01","fra01"):["art-01", 10, 15],
    ("cte-02","fra02"):["art-01", 5, 15],
    ("cte-03","fra03"):["art-01", 7, 15],
    ("cte-04","fra04"):["art-01", 12, 15],
    ("cte-01","fra05"):["art-02", 2, 35],
    ("cte-02","fra06"):["art-02", 12, 35],
    ("cte-03","fra07"):["art-02", 5, 35],
    ("cte-04","fra08"):["art-02", 3, 35],
    ("cte-09","fra13"):["art-06", 250,2 ],
    ("cte-05","fra09"):["art-03", 60, 10],
    ("cte-06","fra10"):["art-04", 1, 600],
    ("cte-07","fra11"):["art-05", 500, 1],
    ("cte-08","fra12"):["art-06", 250,2 ]
    }

menu = """\nMenu para trabajar con las pregunta del examen

1 - Pregunta 01
2 - Pregunta 02
3 - Pregunta 03
4 - Pregunta 04
9 - Terminar"""

while True:
    print(menu)
    opc = input("\nIntroduzca opción:")
    match opc:
        case '1': 
            lista_aux_cod_clientes = []
            for (key, value) in Facturas.items():
                if key[0] not in lista_aux_cod_clientes:
                    lista_aux_cod_clientes.append(key[0])
            cantidad_maxima = 0
            for i in lista_aux_cod_clientes:
                cantidad = 0
                for (key, value) in Facturas.items():                        
                    if i == key[0]:
                        cantidad += value[1]*value[2]
                if cantidad > cantidad_maxima:
                    cantidad_maxima = cantidad
            print('Los clientes que mas han gastado son: ')
            for (key, value) in Facturas.items():
                if cantidad_maxima == value[1]*value[2]:
                    print(key[0])


        case '2':
            lista_aux_cod_articulos = []
            for (key, value) in Facturas.items():
                if value[0] not in lista_aux_cod_articulos:
                    lista_aux_cod_articulos.append(value[0])
            cantidad_maxima = 0
            for i in lista_aux_cod_articulos:
                cantidad = 0
                for (key, value) in Facturas.items():
                    if i == value[0]:
                        cantidad += value[1]
                if cantidad > cantidad_maxima:
                    cantidad_maxima = cantidad
            print('Los articulos mas vendidos fueron: ')
            for i in lista_aux_cod_articulos:
                cantidad = 0
                for (key, value) in Facturas.items():
                    if value[0] == i:
                        cantidad += value[1]
                if cantidad == cantidad_maxima:
                    print(i)
    
        case '3':
            print(f'El numero de facturas de este mes fueron: {len(Facturas)}')
        case '4':
            Clientes = { "cte-01": ("cif-01","cliente01","dir-cte-01"),
                "cte-02": ("cif-02","cliente02","dir-cte-02"),
                "cte-03": ("cif-03","cliente03","dir-cte-03"),
                "cte-04": ("cif-04","cliente04","dir-cte-04"),
                "cte-05": ("cif-05","cliente05","dir-cte-05"),
                "cte-06": ("cif-06","cliente06","dir-cte-06"),
                "cte-07": ("cif-07","cliente07","dir-cte-07"),
                "cte-08": ("cif-08","cliente08","dir-cte-08"),
                "cte-09": ("cif-09","cliente09","dir-cte-09"),
                "cte-10": ("cif-10","cliente11","dir-cte-10"),
                "cte-11": ("cif-11","cliente11","dir-cte-11"),
                "cte-12": ("cif-12","cliente12","dir-cte-12") }

            lista_aux_cod_clientes = []
            for (key, value) in Facturas.items():
                if key[0] not in lista_aux_cod_clientes:
                    lista_aux_cod_clientes.append(key[0])
            for (key, value) in Clientes.items():
                if key not in lista_aux_cod_clientes:
                    for i in value:
                        print(i, end=" ")
                    print()


        case '9':
            print("Finalizando el programa...")
            break
        case _:
            print("Error...opción incorrecta")
