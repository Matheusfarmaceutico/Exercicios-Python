""" Crie uma função que exiba uma saudação com os parâmetros 'saudacao' e 'nome'
"""


def welcome(nome):
    print('Bem vindo' + ',', nome)


name = str(input('Digite seu nome: '))
welcome(name)
