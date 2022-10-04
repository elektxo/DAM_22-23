n = input("Introduce la cantidad de veces: ")
resultado = 2

if n.isdigit():
    if int(n)>0:
        for i in range(int(n)):
            resultado *= 2
        print("El resultado de 2 elevado a", n, "es", resultado)
else:
    print("Introcduce un digito y que sea positivo")