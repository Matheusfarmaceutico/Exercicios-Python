#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 


#utilizando Max e Min
valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {c}')))
maior = (max(valores))
menor = (min(valores))
print(f'Você digitou {valores}')
print(f'O maior valor foi {maior} nas posições: ',end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor foi {menor} nas posições: ',end= '')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end= '')

print(f'O maior valor foi {maior} na(s) posição(ões): ',end= '')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor foi {menor} na(s) posição(ões): ',end= '')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end= '')

print()