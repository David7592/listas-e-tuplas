matriz1 = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]]
matriz2 = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]]
soma1 = 0
soma2 = 0

for i in range(3):
    print(matriz1[i])
print()
for i in range(3):
    print(matriz1[i])

for linha in matriz1:
    for elemento in linha:
        soma1 += elemento
print('soma da matriz 1:', soma1)

for linha in matriz2:
    for elemento in linha:
        soma2 += elemento
print('soma da matriz 2:', soma2)

print('soma das duas matrizes:', soma1 + soma2)