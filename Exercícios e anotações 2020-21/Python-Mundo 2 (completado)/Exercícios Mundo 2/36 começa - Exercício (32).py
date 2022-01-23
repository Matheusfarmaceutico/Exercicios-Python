c=0
from random import randint

while True:
    jogador=int(input('Digite um valor:'))
    computador=randint(0,10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('Par ou Ímpar? [P/I]:')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {total}')
    if tipo=='P':
        if total%2==0:
            print('VOCÊ VENCEU!')
            c=c+1
        else:
            print('VOCÊ PERDEU!')
            break
    if tipo=='I':
        if total%2!=0:
            print('VOCÊ VENCEU!')
            c=c+1
        else:
            print('VOCÊ PERDEU!')
            break
        print('VAMOS JOGAR NOVAMENTE!')
print(f'GAME OVER! VOCÊ VENCEU {c} VEZES!')
