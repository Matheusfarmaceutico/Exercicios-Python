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

"""Um laço for utiliza o método __next__ para transformar um objeto iterável em um iterador. Manualmente podemos utilizar a funcao iter(objeto) para fazer a mesma ."""

#travadores e gerenciamento de memória

import sys
import time

lista = list(range(10))
print(sys.getsizeof(lista)) #modulos sys e getsizeof para ver quanto de memoria um objeto ocupa. No caso atual, consumiu 136 bytes. (Python 3.9.9)

print()
# A funcao a seguir e sua execucao tenta simular como um programa pesado funciona. Note que ele tenta carregar todos os 100 valores e nao os exibe na tela até que estes sejam integralmente processados.
"""def pesadao():
    r = []
    for c in range(100):
        r.append(c)
        time.sleep(0.1)
    return r
r = pesadao()


for v in r:
    print(v) 
print()"""

#Já neste caso, quando utilizamos o yield, os valores sao liberados conforme sao processados.

"""def leve():
    for c in range(100):
        yield c

        
g = leve()


for v in g:
    print(v)
    time.sleep(0.1)"""


#código travador, nao executar fora de ambiente de controle
#ESSE CODIGO ENXERÁ A MEMÓRIA AOS POUCOS COM UMA LISTA DE NÚMEROS ABSURDA, ATÉ QUE O PC TRAVE.
"""def travador(max_number):
    r = []
    for c in range(max_number + 1):
        r.append(c)


g = travador(623*10**21)
for v in g:
    print(v)"""
#ABAIXO VOCÊ VERÁ UMA FORMA DE REPRESENTAR O MESMO NUMERO GIGANTE AOS POUCOS, SEM QUE O COMPUTADOR TRAVE NECESSARIAMENTE.

"""def gerador(max_number):
    for c in range(max_number + 1):
        yield c

g = gerador(623*10**21)
for v in g:
    print(v)"""
#Observe que list comprehensions sao um pouco mais otimizadas do que o for tradicional. 
"""lista = [x for x in range(1000)]
print(sys.getsizeof(lista))
lista2 = list(range(1000))
print(sys.getsizeof(lista2))"""

#Observe que é possível criar um gerador com parênteses

"""lista = (x for x in range(1000))
print(type(lista))
print(next(lista))
print(next(lista))
print(next(lista))"""

#Mais uma vez podemos comparar o quanto geradores economizam mais memória do que listas

lista = [x for x in range(1000)]
lista_gerador = (x for x in range(1000)) #parênteses criam geradores
print(sys.getsizeof(lista)) #Python 3.9.9 = 8856 bytes
print(sys.getsizeof(lista_gerador)) #Python 3.9.9 = 112 bytes
