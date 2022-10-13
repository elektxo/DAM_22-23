palabra = input("Introduce una palabra: ")
v_aux = True

for i in range(len(palabra)-1):
    if palabra[i] > palabra[i+1]:
        print("No es una palabra alfebetica")
        v_aux = False
        break

if v_aux:
    print("Es una palabra alfebetica")
