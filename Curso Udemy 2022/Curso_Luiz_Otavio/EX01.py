""" Faça um programa em que o usuário possa digitar um número inteiro, informando em seguida se o mesmo
é par ou ímpar. Caso o usuário não digite um número inteiro, informe-0 sobre o problema."""

while True:
    try:
        num = int(input('Digite um número inteiro: '))
        if num % 2 == 0:
            print(f'{num} é um número par!')
        else:
            print(f'{num} é um número ímpar!')
        break
    except:
        print('Error!')
