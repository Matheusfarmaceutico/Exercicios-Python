"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
media = 0
velho = 0
homem_velho = ' '
mulher_jovem = 0
for d in range(1, 5):
    print(f'{d} pessoa:')
    nome = str(input('Digite seu nome:')).strip().capitalize()
    idade = int(input('Idade: '))
    media += idade
    sexo = str(input('[M/F]: ')).strip().upper()
    if d == 1 and sexo in 'M':
        velho = idade
        homem_velho = nome
    if sexo in 'M':
        if idade > velho:
            velho = idade
            homem_velho = nome
    if sexo in 'F' and idade < 20:
        mulher_jovem += 1


print(f'A média de idade desse grupo é de {media / 5} anos ')
print(f'O homem mais velho se chama {homem_velho}')
print(f'A quantidade de mulheres com menos de vinte anos é {mulher_jovem}')