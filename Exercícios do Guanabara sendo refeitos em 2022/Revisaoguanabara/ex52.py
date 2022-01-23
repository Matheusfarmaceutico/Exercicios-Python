"""Exercício Python 052: Faça um programa que leia um número inteiro e
diga se ele é ou não um número primo. Mostre por quantas vezes ele foi ou divisível"""

cont = 0
number = int(input('Enter a valid prime number: '))
for c in range(1, number + 1):
    if number % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print(f'\033[31m',end=' ')
    print(f'{c}',end='')
print('\033[0m')
print(f'{number} has been divisible {cont} times, so',end=' ')
if cont <= 2:
    print(f'it is a prime number!',end='')
else:
    print(f'it is not a prime number!')