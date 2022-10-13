import random
n_misterioso = random.randint(1, 10)

intentos = 0
for i in range(5):
    intento = input("Intenta adivinarlo: ")
    if str(n_misterioso) != intento:
        print("Vuelve a intentarlo...")
    else:
        print("Haz acertado maquina, el numero era", n_misterioso)
        print("Lo haz acertado en", i+1, "intentos")
        break