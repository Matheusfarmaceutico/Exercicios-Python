"""Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for."""
tab = int(input('Digite um número para ver sua tabuada: '))
for c in range(0,10):
    print(f'{tab} X {c} = {tab * c}')