lista1 = [1, 1, 3, 3, 5, 11, 4, 7, 9]
lista2 = [1, 2, 3, 5, 6, 8, 4, 9]
lista3 = []

for i in lista1 + lista2:
    if i not in lista3:
        lista3.append(i)
print(lista3)