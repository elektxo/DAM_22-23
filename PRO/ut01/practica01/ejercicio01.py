n1 = input("Introduce un numero: ")
n2 = input("Introduce otro numero: ")

if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    if n1 < n2:
        if n1 > 0:
            for i in range(n1, n2+1):
                validador = True
                for j in range(len(str(i))):
                    for h in range(len(str(i))):
                        if j != h:
                            if str(i)[j] == str(i)[h]:
                                validador = False

                if validador:
                    print(i)

        else:
            print("Introduce un numero mayor de 0")
    else:
        print("El primer numero tiene que ser menor que el segundo")
else:
    print("No se introdujeron numeros")