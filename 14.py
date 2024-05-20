lista1 = [1, 1, 2, 3, 4, 4, 5]
lista2 = [6, 7, 7, 1, 2, 2, 5, 9]
lista3 = []

for i in lista1 + lista2:
    if i not in lista3:
        lista3.append(i)
print(lista3)