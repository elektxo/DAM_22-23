def revuelcaString(frase):
    frase_final = ""

    for i in range(len(frase)):
        if i % 2 != 0:
            frase_final += frase[i]
            frase_final += frase[i-1]
        else:
            if i == len(frase)-1:
                frase_final += frase[i]

    return frase_final

# principal

cadena = input("Indique la frase o palabra: ")

resultado = revuelcaString(cadena)

print(resultado)