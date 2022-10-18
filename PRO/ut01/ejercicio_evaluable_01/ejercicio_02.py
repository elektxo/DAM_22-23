frase = input("Indique la frase o palabra: ")
frase_final = ""

for i in range(len(frase)):
    if i % 2 != 0:
        frase_final += frase[i]
        frase_final += frase[i-1]
    else:
        if i == len(frase)-1:
            frase_final += frase[i]

print(frase_final)