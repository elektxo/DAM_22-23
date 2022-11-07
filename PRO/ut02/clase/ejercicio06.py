dict = {}

while True:
    palabra = input('Escribe una palabra: ')
    if palabra != '@' and palabra != '':
        valor_dvto = dict.setdefault(len(palabra), [])
        dict[len(palabra)].append(palabra)
    else:
        break
maximo = 0
for (key, value) in dict.items():
    if key > maximo:
        maximo = key

for i in range(maximo+1):
    j = maximo-i
    if j in dict:
        print(f'La clave {j} tiene de valor {dict[j]}')