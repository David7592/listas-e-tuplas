matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(0)
    matriz.append(linha)

'''for i in range(5):
    for j in range(5):
        if i == j:
            matriz[i][j] = 1
        if i + j == 5 - 1:
            matriz[i][j] = 1
            matriz[2][2] = 3
    print(matriz[i])'''

for i in range(5):
    for j in range(5):
        if i == j:
            matriz[i][j] = 1
        if i + j == 5 - 1:
            matriz[i][j] = 1
            matriz[2][2] = 3
    print(matriz[i])