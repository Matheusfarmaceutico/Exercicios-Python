"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador
vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
acertar, mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
computador = randint(0,10)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Tente adivinhar um número entre 0 e 10: '))
    palpites += 1
    if jogador < computador:
        print('Mais...')
    elif jogador > computador:
        print('Menos...')
    elif jogador == computador:
        acertou = True
print(f'FIM DE JOGO! VOCÊ ACERTOU APÓS  {palpites} tentativas')