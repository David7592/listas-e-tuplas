lista = [1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 9, 9, 9]
lista1 = []

for elemento in lista:
    if elemento not in lista1:
        lista1.append(elemento)
print(lista1)