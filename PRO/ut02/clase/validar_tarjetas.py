cuenta=input("Introduzca su numero de tarjeta con espacios: ")
cuentasinespacios=cuenta.replace(" ", "")
indicepar=14
indiceinpar=15
suma=0

while indicepar>=0:
    n=int(cuentasinespacios[indicepar])*2
    if n//10 >= 1:
        suma=suma+(n//10)+(n%10)
    else:
        suma=suma+n
    indicepar=indicepar-2

while indiceinpar>0:
    m=int(cuentasinespacios[indiceinpar])
    suma=suma+m
    indiceinpar=indiceinpar-2
print(suma)
if suma%10==0:
    print("El numero de tarjeta "+cuenta+" es valido")
else:
    print("El numero de tarjeta "+cuenta+" no es valido")