# checar se um objeto, no caso abaixo uma lista, é iteravel ou nao
lista = [1,2,3,4,5]
print(hasattr(lista, '__iter__')) # funcao hasattr: Os argumentos são um objeto e uma string. O resultado é True se a string é o nome de um dos atributos do objeto, e False se ela não for.
print()

'''Nota: Quando iteramos sobre um objeto, como uma lista, estamos o transformando em um ITERADOR.
Podemos verificar se um objeto é um iterador'''

lista = [1,2,3,4,5]
lista = iter(lista)
for c in lista:
    print(c)
print(hasattr(lista, "__next__"))
print()

#
lista2 = ['a',2,3,4,5]
lista2 = iter(lista2)
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(type(lista2)) 

'''Diferenca entre iteráveis e iteradores:
1 - iteráveis - O objeto em si, como uma lista, tupla, etc.
2 - Iteradores - Um objeto iterador  que vai te dar um valor de cada vez'''

