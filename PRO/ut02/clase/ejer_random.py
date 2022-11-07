dict = {'aa' : 18, 'bb' : 23, 'cc' : 54, 'dd' : 18}
dict_2 = {}

for (value, key) in dict.items():
    if key in dict_2:
        dict_2[key].append(value)
    else:
        dict_2[key] = [value]

for (key, value) in dict_2.items():
    print(f'La clave {key} tiene de valor {value}')