tupla = [1, 2, 3, 4, 5, 11, 15]
invertida = []

for i in range(len(tupla) -1, -1, -1):
    invertida.append(tupla[i])
print(tuple(invertida))