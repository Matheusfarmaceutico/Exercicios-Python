"""Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""
sum = 0
term = int(input('Enter a valid first term of arithmetic progression: '))
ration = int(input('Enter a valid ration of arithmetic progression:'))
pa = term + (10 - 1) * ration
for c in range(term, pa + 1, ration):
    print(c,end=' -> ')
    sum += c
print('FIM',end='')
print()
print(f'PA SUM: {sum} ')