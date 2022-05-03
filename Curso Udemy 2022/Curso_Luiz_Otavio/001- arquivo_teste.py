

lista1 = [1,2,3,4,5,6]
lista2 = [6,7,8,9,10]


def soma(*args):
    lista_soma = [x + y for x,y in zip(args)]

print(soma(lista1,lista2))