"""2 - Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles""" #desafiomelhorado
numeros = []


def soma(*valores):
    s = 0
    for v in numeros:
        s += v
    print(s)


while True:
    numeros.append(int(input(f'Digite um número:  ')))
    option = ' '
    while option not in 'SsNn':

        option = str(input('Quer contInuar? '))
    if option in 'Nn':
        break

soma(numeros)
