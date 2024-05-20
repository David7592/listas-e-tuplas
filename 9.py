tam = int(input('Tamanho da lista: '))
lista = []
soma = 0

for i in range(tam):
    lista.append(float(input('Valor: ')))
print(lista)

for i in lista:
    soma += i
print(soma)