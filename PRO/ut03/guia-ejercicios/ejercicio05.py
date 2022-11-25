#funciones 

def lectura_cotizaion(dias):
    lista = []
    for i in range(dias):
        cuota = input(f'Cuotizacion del dia {i+1}: ')
        lista.append(int(cuota))
    return lista

def mayor_alza(cotizaciones):
    mayor=cotizaciones[0]
    for i in cotizaciones:
        if i >= mayor:
            mayor=i
    if cotizaciones.count(mayor) > 1:
        resultado='No hay un alza'
    else:
        for i in range(len(cotizaciones)):
            if mayor == cotizaciones[i]:
                resultado=f'El dia de mayor alza fue {i+1} con un alza de {cotizaciones[i]}'
    return resultado


#principal

n = input("Introduce el numero de dias: ")

cotizacion = lectura_cotizaion(int(n))
print(cotizacion)

alza = mayor_alza(cotizacion)
print(alza)
