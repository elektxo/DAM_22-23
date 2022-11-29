def fibo(n):
    if n == 0:
        a_devolver = 0
    elif n == 1:
        a_devolver = 1
    else:
        a_devolver = fibo(n-1) + fibo(n-2)
    return a_devolver

# principal

print(fibo(3))

'''
fibo(1) + fibo(2) -> 1 + (fibo(0) + fibo(1)) -> 1 + (0 + 1)
'''