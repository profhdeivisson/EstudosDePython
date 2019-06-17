questions = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
respostas = []
contRespostas = 0

for q in questions:
    x = ' '
    while x not in 'sn':
        x = input(q).strip().lower()[0]
    respostas.append(x)
    if x == 's':
        contRespostas += 1
if contRespostas == 2:
    print('Classificado como SUSPEITO!')
elif contRespostas == 3 or contRespostas == 4:
    print('Classificado como CÚMPLICE!')
elif contRespostas == 5:
    print('Classificado como ASSASSINO!')
else:
    print('Classificado como INOCENTE!')