sexo=str(input('Qual o seu sexo? [M/F]')).strip().upper()
while sexo not in 'MF':
    sexo=str(input('Dados inválidos! Digite seu sexo: [M/F]:')).strip().upper()
if sexo=='M':
    print('Seu sexo é masculino')
elif sexo=='F':
    print('Seu sexo é feminino')


