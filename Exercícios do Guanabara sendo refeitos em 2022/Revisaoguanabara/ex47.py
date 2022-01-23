"""Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão 
no intervalo entre 1 e 50.

for c in range(0, 51, 2):
    if c == 0:
        continue
    else:
        print(c, end=' ') MINHA SOLUÇÃO: UM POUCO MENOS OTIMIZADA"""
"""SOLUÇÃO DO GUANABARA: """

for c in range(2,51,2):
    print(c,end=' ')