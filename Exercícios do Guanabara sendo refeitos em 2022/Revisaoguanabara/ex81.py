"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""




numeros = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    option = ' '
    while option not in 'SsNn':
        option = str(input('Quer continuar? [S/N]: '))
    if option in 'Nn':
        break
# sort ao invés de sort, muda a lista para sempre, é aplicada como se fosse um comando do jupyter notebook
print(f"""Os {len(numeros)} digitados na lista organizados de modo decrescente:
{sorted(numeros,reverse= True)} """)
for chave, valor in enumerate(numeros):
    if valor == 5:
        print(f'O valor 5 consta na posição {chave}')
valores = numeros.sort()