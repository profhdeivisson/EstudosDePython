from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
alternativa = 0
while alternativa != 5:
    print('=-=' * 10)
    alternativa = int(input('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    >>>>> Qual é a sua opção? 
    '''))
    if alternativa == 1:
        print('O resultado da soma entre {} e {} = {}'.format(n1, n2, n1 + n2))
    elif alternativa == 2:
        print('O resultado da multiplicação entre {} e {} = {}'.format(n1, n2, n1 * n2))
    elif alternativa == 3:
        lista = [n1, n2]
        print('Entre {} e {} o maior número é {}'.format(n1, n2, max(lista)))
    elif alternativa == 4:
        n1 = int(input('Primeiro novo valor: '))
        n2 = int(input('Segundo novo valor: '))
    elif alternativa > 5:
        print('alternativa inválida! Tente novamente.')
    else:
        print('Finalizando...')
    sleep(2)
print('FIM DO PROGRAMA. VOLTE SEMPRE!')
