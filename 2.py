v = int(input('Comprimento vertical: '))
h = int(input('Comprimento horizontal: '))

for i in range(v):
    if i == 0 or i == v - 1:
        print(' * ' * h)
    else:
        print(' * ' + '   ' * (h - 2) + ' * ')