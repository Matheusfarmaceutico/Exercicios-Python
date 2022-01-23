from random import randint
computador=randint(0,10)
palpite=0
print('Sou o seu computador. Pensei num número de 0 a 10.')
print('Gostaria de adivinhar qual foi?')
acertou=False
while not acertou:
    jogada=int(input('Digite o seu palpite:'))
    palpite=palpite+1
    if computador==jogada:
        acertou=True
    else:
        if jogada<computador:
            print('Mais...!')
        elif jogada>computador:
            print('Menos...!')
print('Você acertou após {} tentativas'.format(palpite))