tupla1 = [1, 2, 3, 4, 4, 4, 1, 1, 5]
tupla2 = []
soma = 0

for i in tupla1:
    if i not in tupla2:
        tupla2.append(i)

print(f'Elementos da tupla: {tuple(tupla2)}')
print(f'Essa tupla possui {len(tupla2)} elementos')