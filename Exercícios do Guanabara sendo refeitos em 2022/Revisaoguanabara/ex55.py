"""Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""
maior = menor = 0
for w in range(1,6):
    weight = float(input(f'{w} person, enter a valid weight, please: '))
    if w == 1:
        maior = weight
        menor = weight
    else:
        if weight > maior:
            maior = weight
        elif weight < menor:
            menor = weight
print(f'O maior peso foi {maior} e o menor {menor}')
