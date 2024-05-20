lista = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10, 9, 9, 9, 9, 10]
print(lista)
x = int(input('Qual elemento deseja remover: '))
y = '*'

for i in range(len(lista)):
    if lista[i] == x:
        lista[i] = y
print(lista)