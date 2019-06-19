questions = {1: 'Telefonou para a vítima?', 2: 'Esteve no local do crime?', 3: 'Mora perto da vítima?', 4: 'Devia para a vítima?', 5: 'Já trabalhou com a vítima?'}
análise = {0: 'Inocente', 1: 'Inocente', 2: 'Suspeito', 3: 'Cúmplice', 4: 'Cúmplice', 5: 'Assassino'}
respostas = []
for q in questions.values():
    x = ' '
    while x not in 'sn':
        x = input(q).strip().lower()[0]
    if x == 's':
        respostas.append(x)
print(f'Você é {análise[len(respostas)]}')