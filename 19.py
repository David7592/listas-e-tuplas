lista = [1, 33, 20, 25, 27, 100, 55, 72, 82, 4, 4, 5]

listapar = [i for i in lista if i %2 == 0]
listaimpar = [i for i in lista if i %2 != 0]

x = listapar + listaimpar
print(x)
