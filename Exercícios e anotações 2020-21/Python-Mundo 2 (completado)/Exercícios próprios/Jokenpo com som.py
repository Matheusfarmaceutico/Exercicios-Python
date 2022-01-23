from random import randint
import playsound
from time import sleep
lista=('pedra','papel','tesoura')
computador=randint(0,2)
print('''BEM VINDO AO NOSSO JOKENPÔ
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador=int(input('Escolha uma opção válida:'))
print('JO')
playsound.playsound('JO.mp3')
sleep(1)
print('KEN')
playsound.playsound('ken.mp3')
print('PO!!!')
playsound.playsound('PO.mp3')
if jogador!=0 and jogador!=1 and jogador!=2:
        print('JOGADA INVÁLIDA')
        sleep(0.2)
        playsound.playsound('INVALIDO.mp3')
else:
    print('-=' * 11)
    print('COMPUTADOR JOGOU {}'.format(lista[computador]))
    print('JOGADOR JOGOU {}'.format(lista[jogador]))
    print('-='*11)
if computador==0: #computador joga pedra
    if jogador==0:
        print('EMPATE!')
        playsound.playsound('INVALIDO.mp3')
    elif jogador==1:
        print('JOGADOR VENCEU!')
        playsound.playsound('usuario.mp3')
    elif jogador==2:
        print('COMPUTADOR VENCEU!')
        playsound.playsound('computador.mp3')
if computador==1: #computador joga papel
    if jogador==0:
        print('COMPUTADOR VENCEU!')
        playsound.playsound('computador.mp3')
    elif jogador==1:
        print('EMPATE!')
        playsound.playsound('INVÁLIDO.mp3')
    elif jogador==2:
        print('JOGADOR VENCEU!')
        playsound.playsound('usuario.mp3')
if computador==2: #computador joga tesoura
    if jogador==0:
        print('JOGADOR VENCEU!')
        playsound.playsound('usuario.mp3')
    elif jogador==1:
        print('COMPUTADOR VENCEU!')
        playsound.playsound('computador.mp3')
    elif jogador==2:
        print('EMPATE!')
        playsound.playsound('invalido.mp3')
