"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
n1 = int(input('Enter a single number: '))
n2 = int(input('Enter a second number: '))
option = 0
while option != 5:
    print('''What you want to do with these values?
          [1] SUM
          [2] Multiply
          [3] MAJOR
          [4] New numbers
          [5] End program''')
    option = int(input('Please choose: '))
    if option == 1:
        print(f'The sum of these values is: {n1 + n2} ')
    elif option == 2:
        print(f'The multiplication of these values is: {n1 * n2} ')
    elif option == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        if n1 < n2:
            print(f'O maior valor é {n2}')
        else:
            print('Os valores são iguais!')
    elif option == 4:
        n1 = int(input('Digite um novo primeiro valor: '))
        n2 = int(input('Digite um novo segundo valor: '))
    elif option == 5:
        print('Finalizando...')
    elif option > 5:
        print('Opção inválida, tente novamente!')

