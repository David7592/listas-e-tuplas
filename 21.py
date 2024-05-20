tupla = (1, 33, 6, 14, 10, 22, 2)
tuplapar = []
tuplaimpar = []
contpar = 0
contimpar = 0

for i in tupla:
    if i % 2 == 0:
        tuplapar.append(i)
        contpar += 1
    else:
        tuplaimpar.append(i)
        contimpar += 1

print(f'Par: {tuple(tuplapar)}\nÍmpar: {tuple(tuplaimpar)}')
print(contpar)
print(contimpar)