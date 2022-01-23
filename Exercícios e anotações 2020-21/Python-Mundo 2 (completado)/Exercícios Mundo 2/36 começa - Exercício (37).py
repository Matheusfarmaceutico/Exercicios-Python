# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = mil = menor = cont = 0
nomeproduto = ''
while True:
    nome = str(input('Digite o nome do produto: ')).upper().strip()
    valorp = float(input('Digite o valor do produto:'))
    cont += 1
    if valorp > 1000:
        mil += 1
    if cont == 1: # existe uma forma de simplificar isso, já que os dois blocos if e else são iguais. Ver ex original
        menor = valorp
        nomeproduto = nome
    else:
        if valorp < menor:
            menor = valorp
            nomeproduto = nome

    total += valorp
    option = ' '
    while option not in 'SN':
        option = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if option == 'N':
        break
print(f'O total gasto em produtos foi de R$ {total:.2f}')
print(f'A quantidade produtos que custam mais de R$ 1000: {mil}')
print(f'O produto mais barato é {nomeproduto}')