#se quiere leer una frase y saber cuantos caracteres son vocales y cuantos consonantes

frase = input("Introduce una frase: ")
vocales = 0
consonantes = 0

for i in range(len(frase)):
    if frase.lower()[i] == "a" or frase.lower()[i] == "e" or frase.lower()[i] == "i" or frase.lower()[i] == "o" or frase.lower()[i] == "u":
        vocales += 1
    else:
        if frase.lower()[i] != " ":
            consonantes += 1

print("Hay", vocales, "vocales y", consonantes, "consonantes")