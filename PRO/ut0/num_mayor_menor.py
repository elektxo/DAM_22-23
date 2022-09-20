num = int(input("Introduxca un numero: "))
num_mayor = num
num_menor = num
seguir = "Y"

while seguir == "Y":
    if num > num_mayor:
        num_mayor = num
    if num < num_menor:
        num_menor = num
    seguir = input("Desea continuar?[Y/N] ")
    while seguir != "Y" and seguir != "N":
        seguir = input("Vuelva a intentarlo [Y/N]")
    if seguir == "Y":
        num = int(input("Introduce un numero: "))

print("El numero mayor es ", num_mayor)
print("El numero menor es ", num_menor)