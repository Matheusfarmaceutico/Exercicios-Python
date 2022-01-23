""""Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
 N primeiros elementos de uma Sequência de Fibonacci. """



elementos = int(input('Quantos elementos você quer ver?'))
t1 = 0
t2 = 1
cont = 3 # começa em 3 porque se nao o laço ia se repetir mais 3 vezes, que é a quant já exposta no print de t1 e t2 e t3
print(f'{t1} -> {t2}',end='')
while cont <= elementos:
    t3 = t1 + t2
    print(f' - > {t3}',end= '')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')