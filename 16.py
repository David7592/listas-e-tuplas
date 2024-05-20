nota = [7.0, 7.5, 9.0, 6.0]
peso = [2, 2, 3, 3]
somapeso = 0
print(f'Notas: {nota}')
print(f'Respectivos pesos: {peso}')

a = nota[0] * peso[0]
b = nota[1] * peso[1]
c = nota[2] * peso[2]
d = nota[3] * peso[3]
soma = a + b + c + d

for i in peso:
    somapeso += i

print(f'Média poderada do aluno: {soma/somapeso}')