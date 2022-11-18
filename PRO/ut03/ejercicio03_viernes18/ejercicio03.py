#funciones

def calculo_probabilidades( ocasiones_por_valor ):
    total_casos=0
    p = {}
    for (key, value) in ocasiones_por_valor.items():
        total_casos+=value

    for (key, value) in ocasiones_por_valor.items():
        pos=str((value/total_casos)*100)
        p[key]=pos[0]+pos[1]+pos[2]+pos[3]+"%"

    return p

def calculo_combinaciones():
    combinaciones = {}
    for i in range(2,13):
        combinaciones[i]=0
        for j in range(1,7):
            for k in range(1,7):
                if (j+k) == i:
                    combinaciones[i]+=1
    return combinaciones

#principal

combos = calculo_combinaciones()
print(combos)

posibilidades = calculo_probabilidades(combos)
print(posibilidades)