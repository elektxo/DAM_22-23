def validarTarjeta(cuenta):
    indicepar=14
    indiceinpar=15
    suma=0
    while indicepar>=0:
        n=int(cuenta[indicepar])*2
        if n//10 >= 1:
            suma=suma+(n//10)+(n%10)
        else:
            suma=suma+n
        indicepar=indicepar-2

    while indiceinpar>0:
        m=int(cuenta[indiceinpar])
        suma=suma+m
        indiceinpar=indiceinpar-2

    if suma%10==0:
        a_devolver = True
    else:
        a_devolver = False

    return a_devolver

# principal

n_cuenta=input("Introduzca su numero de tarjeta sin espacios: ")

if n_cuenta.isdigit() and len(n_cuenta) == 16:
    resultado = validarTarjeta(n_cuenta)
    print(resultado)
else:
    print('No se ha introducido correctamente el numero')