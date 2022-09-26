n = int(input("Introduce un numero: "))
aux_n = n
espacio = " "
asterisco = "*"
n_ast = 1

while aux_n>0:
    print(espacio * (aux_n - 1) + asterisco * n_ast)
    aux_n -= 1
    n_ast += 2

while aux_n < n:
    print(espacio * (n-2) + asterisco * 3)
    aux_n += 1