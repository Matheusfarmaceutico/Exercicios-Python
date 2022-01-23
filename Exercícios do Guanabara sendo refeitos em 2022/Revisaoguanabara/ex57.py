"""Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido! Tente novamente: ')).strip().upper()[0]
if sexo == 'M':
    print(f'Você registrou o sexo masculino')
else:
    print(f'Você registrou o sexo feminino')
print({sexo})