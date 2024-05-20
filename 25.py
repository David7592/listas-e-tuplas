v = int(input('Comprimento1: '))
h = int(input('Comprimento2: '))
matriz = []
x = int(input('Elemento da lista: '))

for i in range(v):
    matriz.append([x]*h)

for i in range(v):
    print(matriz[i])