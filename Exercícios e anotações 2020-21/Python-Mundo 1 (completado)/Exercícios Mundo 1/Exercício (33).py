import random
from time import sleep
r=random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um número de 0 até 5. Tente adivinhá-lo!')
print('-=-'*20)
ad=int(input('Adivinhe o número que o computador pensou de 0 até 5: '))
print('CARREGANDO...')
sleep(2)
if ad==r:
    print('VOCÊ ACERTOU! O COMPUTADOR PENSOU NO NÚMERO {}'.format(r))
else:
    print('VOCÊ ERROU! Digitou o número {}... O COMPUTADOR PENSOU NO NÚMERO {}'.format(ad,r))
