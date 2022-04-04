
# O objetivo do exercício é somar os valores dos produtos com list comprehensions



carrinho = []
carrinho.append(("melancia",1.89))
carrinho.append(("isopor",2))
total = sum([float(y) for x,y in carrinho])
print(f'{total:.2f}')

"""Desafio para amanha é transformar esse esquema de list  comp"""

#sem utilizar list comprehension


carrinho = []
while True:
    produto = input("Digite o nome de um produto: ")
    valor = float(input("Digite o valor de tal produto: "))
    carrinho.append((produto,valor))
    option = str(input("Quer continuar?"))
    if option in "Nn":
        break


def outro(lista):
    s = 0
    for v in lista:
        s += v[1]
    return f'{s:.2f}'
print(outro(carrinho))


