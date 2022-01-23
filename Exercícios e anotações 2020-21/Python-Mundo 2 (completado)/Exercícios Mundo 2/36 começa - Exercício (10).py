import random
from time import sleep
itens=('pedra','papel','tesoura')
computador=random.randint(0,2)
print('''BEM VINDO AO NOSSO JOKENPÔ
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador=int(input('Escolha uma opção válida para jogar:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if jogador!=0 and jogador!=1 and jogador!=2:
    print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')
else:
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
if computador==0:#computador joga pedra
    if jogador==0:#jogador joga pedra
        print('EMPATE!')
    elif jogador==1:#jogador joga papel
        print('JOGADOR VENCEU!')
    elif jogador==2:#jogador joga tesoura
        print('COMPUTADOR VENCEU!')
    #else:
        #print('JOGADA INVÁLIDA!')
if computador==1: #computador joga papel
    if jogador==0:#jogador joga pedra
        print('COMPUTADOR VENCEU!')
    elif jogador==1:#jogador joga papel
        print('EMPATE!')
    elif jogador==2: #jogador lança tesoura
        print('JOGADOR VENCEU!')
    #else:
        #print('JOGADA INVÁLIDA!')
if computador==2: #computador joga tesoura
    if jogador==0: #jogador joga pedra
        print('JOGADOR VENCEU!')
    if jogador==1: #jogador joga papel
        print('COMPUTADOR VENCEU!')
    if jogador==2: #jogador joga tesoura
        print('EMPATE!')
    #else:
        #print('JOGADA INVÁLIDA!')
