n=int(input("Introduce un numero: "))
aux_n = n
suma=0

while n!=0:
    suma=n%10+suma
    n=n//10
    if n==0 and suma//10!=0:
        n=suma+n
        suma=0
print("El numero magico de ", aux_n, " es ", suma)