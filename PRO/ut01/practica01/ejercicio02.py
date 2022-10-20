palabra01 = input("Intrododuce una palabra: ")
palabra02 = input("Intrododuce otra palabra: ")
final = ""
comienzo = ""

if len(palabra01) <= len(palabra02):
    bucle = len(palabra01)
else:
    bucle = len(palabra02)

for i in range(bucle):
    if palabra01[i] == palabra02[i]:
        comienzo += palabra01[i]
    else:
        break

for i in range(bucle):
    if palabra01[::-1][i] == palabra02[::-1][i]:
        final += palabra01[::-1][i]
    else:
        break

print(f"El comienzo mas largo es [{comienzo}]")
print(f"El final mas largo es [{final[::-1]}]")