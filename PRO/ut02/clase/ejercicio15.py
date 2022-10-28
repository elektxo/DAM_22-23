matris = [[1,4,5],[4,2,6],[5,6,3]]
matris_traspuesta = [[],[],[]]

print('---Matris original---')
for i in matris:
    for j in i:
        print(j, end=" ")
    print()

print('---Matris traspuesta---')
for i in range(3):
    for j in range(3):
        matris_traspuesta[i].append(matris[j][i])
        print(matris[j][i], end=" ")
    print()