contador_primos = 0
contador = 1

while contador_primos < 100:
    acumulado = 0
    for i in range(1, contador):
        if contador%i == 0:
            acumulado += i
    if acumulado == 1:
        contador_primos += 1
        #print(f"Primo numero {contador_primos} es {contador}")
        print(f"{contador:5}", end=" ")
        if contador_primos%10 == 0:
            print()
    contador += 1