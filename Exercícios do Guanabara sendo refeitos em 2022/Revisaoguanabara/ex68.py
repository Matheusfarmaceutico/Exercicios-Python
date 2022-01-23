"""Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
 quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

from random import randint

vit = 0
while True:
    computador = randint(0, 10)
    try:
        jogador_number = int(input('Número a ser jogado: '))
    except:
        print('Número inválido!')
        continue
    soma_jogadas = (computador + jogador_number) % 2
    jogador_option = ' '
    while jogador_option not in 'PpIi':
        jogador_option = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    if jogador_option == 'P':
        if soma_jogadas == 0:
            print(f'Jogador venceu, pois jogou par e a soma das jogados foi par:  {computador + jogador_number}')
            vit += 1
        else:
            print(f'Jogador perdeu, pois jogou par e a soma das jogadas foi ímpar:  {computador + jogador_number}')
            break
    if jogador_option == 'I':
        if soma_jogadas != 0:
            print(f'Jogador venceu, pois jogou ímpar e a soma das jogadas foi ímpar:  {computador + jogador_number}')
            vit += 1
        else:
            print(f'Jogador perdeu, pois jogou ímpar e a soma das jogadas foi par:  {computador + jogador_number}')
            break
print(f'Número de vitórias: {vit}')