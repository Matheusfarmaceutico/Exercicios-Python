#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*50)
print('{:^30}'.format('SEJA BEM VINDO AO NOSSO CAIXA ELETRÔNICO!'))
print('='*50)
valor=int(input('Digite o quanto que você quer sacar R$'))
ced=50
total=valor
quantced=0
while True:
    if total>=ced:
        total=total-ced
        quantced+=1
    else:
        if quantced>0:
            print(f'o total de {quantced} cédulas de R${ced} ')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        quantced=0
        if total==0:
            break
print('VOLTE SEMPRE!')
