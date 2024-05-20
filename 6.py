import random

lan = int(input('Lançamentos: '))
lista = []
quan1 = 0
quan2 = 0
quan3 = 0
quan4 = 0
quan5 = 0
quan6 = 0

for i in range(lan):
    lista.append(random.randint(1, 6))
print(lista)
for i in lista:
    if i == 1:
        quan1 += 1
    if i == 2:
        quan2 += 1
    if i == 3:
        quan3 += 1
    if i == 4:
        quan4 += 1
    if i == 5:
        quan5 += 1
    if i == 6:
        quan6 += 1

print(f'1 apareceu {quan1}X\n2 apareceu {quan2}X\n3 apareceu {quan3}X\n4 apareceu {quan4}X\n5 apareceu {quan5}X\n6 apareceu {quan6}X')