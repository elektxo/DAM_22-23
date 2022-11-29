def suma_numeros(n):
    if n == 1:
        a_devolver = 1
    elif n == 0:
        a_devolver = 0
    else:
        a_devolver = n + suma_numeros(n-1)
    return a_devolver

print(suma_numeros(5))