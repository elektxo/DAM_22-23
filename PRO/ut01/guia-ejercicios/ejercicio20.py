from curses.ascii import isdigit

n = input("Introduce un numero: ")
if n.isdigit():
    n = int(n)
    if n>=1:
        print(n, end=" ")
        while n!=1:
            if n%2 != 0:
                n*=3
                n+=1
            else:
                n//=2
            print(n, end=" ")
    else:
        print("El numeor introducido debe ser mayor a 0...")

else:
    print("Debe introducir un numero no una cadena de caracteres...")
