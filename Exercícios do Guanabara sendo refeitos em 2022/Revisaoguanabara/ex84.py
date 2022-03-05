#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

pessoas = []
quant_pessoas = 0
while True:
    nome = str(input('Nome: '))
    pessoas.append(nome)
    peso = float(input('Insira o seu peso: '))
    pessoas.append(peso)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break
converter = int(len(pessoas))
print(converter // 2)