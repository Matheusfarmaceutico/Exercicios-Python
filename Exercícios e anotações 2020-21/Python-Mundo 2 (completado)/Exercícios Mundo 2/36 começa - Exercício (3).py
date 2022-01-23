n1=int(input('Digite o PRIMEIRO número:'))
n2=int(input('Digite o SEGUNDO número:'))
if n2>n1:
    print('{} é o valor maior'.format(n2))
if n1>n2:
    print('{} é o valor maior'.format(n1))
elif n1==n2:
    print('Não existe valor maior, os dois são iguais!')

