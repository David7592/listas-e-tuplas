tupla1 = [1, 2, 2, 2, 5, 5, 1, 3]
tupla2 = [7, 8, 8, 5, 9, 1, 2, 3]
tupla3 = []

for i in tupla1 + tupla2:
    if i not in tupla3:
        tupla3.append(i)

print(tuple(tupla3))
