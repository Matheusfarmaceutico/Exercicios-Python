
# O objetivo do exercício é somar os valores dos produtos com list comprehensions



"""carrinho = []

carrinho.append(('Macarrão',30))
carrinho.append(('Feijão',20))

total = [y for x,y in carrinho]
print(sum(total))"""



#sem utilizar list comprehension


carrinho = []
while True:
    produto = input("Digite o nome e o valor de um produto: ")
    valor = float(input("Digite o valor de tal produto: "))
    carrinho.append((produto,valor))
    option = str(input("Quer continuar?"))
    if option in "Nn":
        break


def outro(lista):
    s = 0
    for v in lista:
        s += v[1]
    return s
print(outro(carrinho))