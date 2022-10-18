cuenta=input("Introduzca su numero de tarjeta sin espacios: ")
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
print(suma)
if suma%10==0:
    print(f"El numero de tarjeta {cuenta} es valido")
else:
    print(f"El numero de tarjeta {cuenta} no es valido")