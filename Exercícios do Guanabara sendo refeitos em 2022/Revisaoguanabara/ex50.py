"""Exercício Python 050: Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""

# Solution for Matheus's
number = 0
cont = 1
s = 0
while cont < 7:
    try:
        number = int(input(f'Enter a {cont} valid interger number: '))
        cont += 1
        if number % 2 == 0:
            s += number
        else:
            print('Odd number added, it is not be counted!')
            continue
    except:
        print('Invalid character! Try Again:',end=' ')
        continue

print(f'The sum of all the even numbers entered was: {s}')
