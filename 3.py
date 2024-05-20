import random
v = int(input('Comprimento1: '))
h = int(input('Comprimento2: '))
matriz = []
soma = 0

for i in range(v):
    linha = []
    for j in range(h):
        linha.append(random.randint(1, 9))
    matriz.append(linha)

for linha in matriz:
    for i in linha:
        soma = soma + i
        media = soma/(v*h)

for i in range(v):
    print(matriz[i])
print(f'A soma dos elementos é {soma}')
print(f'A média da matriz é {media}')