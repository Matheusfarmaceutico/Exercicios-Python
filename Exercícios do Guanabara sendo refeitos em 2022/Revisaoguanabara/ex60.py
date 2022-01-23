"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

# minha solução utilizando for
'''fact = int(input('Enter a valid integer to find its factorial: '))
mult = 1
for c in range(fact,0,-1):
    mult *= c
    print(c,end=' ')
print(end='= ')
print(mult)'''
# soluções do Guanabara:
# 01 - Cálculo de fatorial utilizando math
"""from math import factorial
n = int(input('Enter a valid integer to find its factorial: '))

print(f'{n}! = {factorial(5)}')"""
# 02 utilizando laço while
factorial = int(input('Enter a valid integer to know its factorial: '))
f = 1
cont = factorial
while cont > 0:
    print(cont,end='')
    print(' X ' if cont > 1 else ' = ',end='')
    f *= cont
    cont -= 1
print(f)