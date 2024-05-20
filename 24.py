matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

somalinha = []
somacoluna = [0] * len(matriz[0])

for linha in matriz:
    somalinha.append(sum(linha))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        somacoluna[j] += matriz[i][j]

print("Somas das linhas:", somalinha)
print("Somas das colunas:", somacoluna)