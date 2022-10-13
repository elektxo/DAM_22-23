from curses.ascii import isdigit
acumulado = 0
n = input("Introduce un numero: ")
if n.isdigit():
    n = int(n)
    if n>0:
        for i in range(1, n):
            if n%i == 0:
                acumulado += i

if n == acumulado:
    print("Es magico el numero", n)
else:
    print("No es magico")