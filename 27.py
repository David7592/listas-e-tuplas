matriz = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1]]
soma1 = 0
soma2 = 0

for i in range(len(matriz)):
    print(matriz[i])

for i in range(len(matriz)):
    soma1 += matriz[i][i]
    soma2 += matriz[i][5 - i - 1]

print(f'Diagonal principal: {soma1}')
print(f'Diagonal secundária: {soma2}')