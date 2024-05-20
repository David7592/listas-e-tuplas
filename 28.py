lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista_intercalada = []

for i in range(len(lista) // 2):
    lista_intercalada.append(lista[i])
    lista_intercalada.append(lista[-(i + 1)])
if len(lista) % 2 != 0:
    lista_intercalada.append(lista[len(lista) // 2])

print(lista_intercalada)