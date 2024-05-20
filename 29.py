matriz = [[1, 2, 0, 4, 5], [6, 7, 8, 4, 10], [5, 4, 3, 2, 1], [10, 9, 12, 7, 6]]
soma0 = 0
soma1 = 0
soma2 = 0
soma3 = 0

for i in range(4):
    print(matriz[i])

for i in matriz[0]:
    soma0 += i
print(soma0)
for i in matriz[1]:
    soma1 += i
print(soma1)
for i in matriz[2]:
    soma2 += i
print(soma2)
for i in matriz[3]:
    soma3 += i
print(soma3)