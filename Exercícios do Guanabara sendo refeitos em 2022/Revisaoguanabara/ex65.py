"""Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

option = 'S'
cont = soma = maior = menor = 0
while option in 'Ss':
    n = int(input('Digite um número:'))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    option = str(input('Quer continuar? [S/N]: ')).strip()
media = soma/cont
print(f'A média dos {cont} valores digitados foi {media} ')
print(f'O maior valor digitado foi {maior} e o menor {menor}')
# resolução mais sofisticada, usando exceções, break, continue, etc:
"""option = ' '
s = maior = menor = c = 0
while True:
    try:
        n = int(input(f'Digite o {c + 1} número: '))
        c += 1
        s += n
    except:
        print('Caractere inválido! Apenas números, por favor.')
        continue
    while option not in 'SsNn':
        option = str(input('Quer continuar? [S/N]: '))
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if option in 'Nn':
        break
media = s/c
print(f'A média dos {c} valores inseridos foi {media}')
print(f'Maior número inserido foi {maior}; Menor número inserido {menor}')
"""