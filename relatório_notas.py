notas = []
total = acimaMédia = contMenorSete = 0
while True:
    nota = 0
    nota = int(input('Digite uma nota: '))
    if nota == -1:
        break
    notas.append(nota)
    total += nota
print(f'Há {len(notas)} itens na lista.')
for c in notas:
    print(f'{c}', end=' ')
    if c < 7:
        contMenorSete += 1
    if c > total / len(notas):
        acimaMédia += 1
print('')
for c in reversed(notas):
    print(c)
print('Total = {}'.format(total))
print(f'A média dos valores digitados é: {total / len(notas):.2f}')
print(f'{acimaMédia} números estão acima da média.')
print(f'{contMenorSete} números são menores que 7.')
print('Volte sempre!')
