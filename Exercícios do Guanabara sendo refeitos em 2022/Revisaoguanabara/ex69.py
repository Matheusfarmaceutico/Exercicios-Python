"""Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """
maiores = homens = mulheres = 0
cont = 1
while True:
    try:
        print(f'{cont} pessoa: ')
        print(f'-='*10)
        idade = int(input('Idade: '))
        cont += 1
        if idade >= 18:
            maiores += 1
        sexo = ' '
    except:
        print('Caracter inválido! Insira uma idade válida')
        continue
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: '))
        if sexo in 'Mm':
            homens += 1
        if sexo in 'Ff' and idade < 20:
            mulheres += 1
    option = ' '
    while option not in 'SsNn':
        option = str(input('Quer continuar? '))
    if option in 'Nn':
        break
print(f'Quantas pessoas com 18 anos ou mais: {maiores}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres jovens cadastradas: {mulheres}')
