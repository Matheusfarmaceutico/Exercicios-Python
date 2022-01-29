"""Fizbuzz - Se o parâmetro da função for divisivel por 3, retorne fizz, se o parâmetro da função for divisivel
por 5, retorne buzz, se o parâmetro da função for divisível por 5 e 3, retorne Fizzbuzz, caso contrário, retor
ne o número enviado."""
from random import randint


def efeverscente(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return f'{numero} foi divisivel por 3 e 5: fizzbuzz'
    if numero % 3 == 0:
        return f"{numero} foi divisível por 3: fizz"
    if numero % 5 == 0:
        return f"{numero} foi divisível por 5: buzz"

    return numero


for c in range(1, 100):
    print(efeverscente(randint(0, 100)))
