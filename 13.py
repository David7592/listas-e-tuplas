lista = [1, 3, 5, 2, 10, 4, 6]
print(lista)
x = input('Crescente ou decrescente(c/d): ')
if x == 'c':
    lista.sort(reverse=False)
    print(lista)
if x == 'd':
    lista.sort(reverse=True)
    print(lista)