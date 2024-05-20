import random
v = int(input('Comprimento1: '))
h = int(input('Comprimento2: '))
matriz = []
contador = 0

for i in range(v):
    lista = []
    for j in range(h):
        lista.append(random.randint(0, 1))
    matriz.append(lista)

for i in range(v):
    print(matriz[i])

for linha in matriz:
    for elemento in linha:
        if elemento == 0:
            contador += 1

x = (contador * 100)/(v * h)

print(f'O número 0 apareceu {contador} e constitui {x}% da matriz ')