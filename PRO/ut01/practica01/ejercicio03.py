frase = input("Escribe una frase: ")
frase_final = ""
palabra = ""

for i in frase[::-1]:
    if i == " ":
        frase_final += palabra[::-1]
        palabra = ""
        frase_final += " "
    else:
        palabra += i
frase_final += palabra[::-1]

print(frase_final)