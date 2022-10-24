j = 0

n = input("Introduce un numero: ")
if n.isdigit and int(n) > 0:
    n = int(n)

    for i in range(1, n+1):
        j += i
        print(f'{i} - {j}')