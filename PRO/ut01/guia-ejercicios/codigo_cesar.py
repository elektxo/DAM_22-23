abcedario = "abcdefghijklmnopqrstuvwxyz"

mensaje = input("Introduce el mensaje para encriptar: ")
clave = int(input("Cual es la clave: "))
if clave >= 26:
    clave = clave//26

mensaje_aux = mensaje.lower()

abcedario_aux = ""

for i in range(clave-1, len(abcedario)):
    abcedario_aux += abcedario[i]
for i in range(0, clave):
    abcedario_aux += abcedario[i]
    
print(abcedario_aux)