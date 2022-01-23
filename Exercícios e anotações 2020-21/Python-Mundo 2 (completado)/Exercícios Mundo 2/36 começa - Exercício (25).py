from time import sleep
n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
opção=0
while opção!=5:
    print('''Você tem as seguintes opções para esses dois números:
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa''')
    opção=int(input('Digite a opção escolhida:'))
    if opção==1:
        somar=n1+n2
        print('\033[31mA soma de {} e {} é igual a {}\033[m'.format(n1,n2,somar))
    if opção==2:
        multiplicar=n1*n2
        print('\033[31mO produto entre {} e {} é igual a {}\033[m'.format(n1,n2,multiplicar))
    if opção==3 and n1>n2:
        print('\033[31mO maior número é {}\033[m'.format(n1))
    if opção==3 and n2>n1:
        print('\033[31mO maior número é {}\033[m'.format(n2))
    if opção==4:
        n1=int(input('Digite o primeiro valor:'))
        n2=int(input('Digite o segundo valor:'))
    if opção==5:
        print('FINALIZANDO...')
    if opção != 5 and opção != 4 and opção != 3 and opção != 2 and opção != 1:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
    sleep(2)
print('FIM DO PROGRAMA! VOLTE SEMPRE!')