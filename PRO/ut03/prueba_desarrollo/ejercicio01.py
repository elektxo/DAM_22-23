n = 1234321

def calcularCapicua(numero):
    primer_n = 0
    ultimo_n = 0
    nuevo_n = 0
    divisor = 10
    if numero > 9:
        ultimo_n = numero % 10
        numero = numero // 10
        while True:
            if numero//divisor > 0:
                divisor = divisor * 10
            else:
                nuevo_n = numero % (divisor/10)
                primer_n = numero // (divisor/10)
                break
        a_devolver = primer_n == ultimo_n
    else:
        return True
    return a_devolver == calcularCapicua(nuevo_n)

resultados = calcularCapicua(n)

print(resultados)