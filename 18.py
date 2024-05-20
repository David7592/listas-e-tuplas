lista = ['casa', 'academia', 'faculdade', 'autoescola', 'estudar']
somaa = 0
somae = 0
somai = 0
somao = 0
somau = 0

for palavra in lista:
    for letra in palavra:
        if letra == 'a':
            somaa += 1
        if letra == 'e':
            somae += 1
        if letra == 'i':
            somai += 1
        if letra == 'o':
            somao += 1
        if letra == 'u':
            somau += 1

print(lista)
print(f'a = {somaa}\ne = {somae}\ni = {somai}\no = {somao}\nu = {somau}')