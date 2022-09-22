n_original = input("Introduce un numero: ")
n_aux= n_original
n_invertido = 0

#Invertir numero 
multiplicador = 1
for i in range(len(n_aux)):
    n_invertido = n_invertido + (int(n_aux[i])*multiplicador)
    multiplicador = multiplicador*10

print(n_invertido, n_original)

if int(n_original) == n_invertido:
    print("Es capicua")
else:
    print("No es capicua")