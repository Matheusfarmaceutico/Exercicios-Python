"""Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""


"""print(f'A soma dos {cont} valores digitados é {soma}')
soma = cont = 0
user = int(input('Digite um valor: '))
while user != 999:
    soma += user
    cont += 1
    user = int(input('Digite: '))

print(f'A soma dos {cont} valores digitados é {soma}')""" # solução guanabara PRIMEIRA


'''user = soma = cont = 0
while user != 999:
    user = int(input('Digite um valor: '))
    if user != 999:
        soma += user
        cont += 1
print(f'SOMA: {soma} NÚMEROS {cont}')''' # minha solução
s = c = 0
while True:
    user = int(input('Digite um valor'))
    if user == 999:
        break
    else:
        s += user
        c += 1
print(f'Você somou {c} números e a soma deles foi {s}') #solução usando break
