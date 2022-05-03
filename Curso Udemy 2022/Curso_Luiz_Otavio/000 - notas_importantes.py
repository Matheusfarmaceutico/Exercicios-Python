#Geradores e sua importância:

#código travador, nao executar fora de ambiente de controle
#ESSE CODIGO ENCHERÁ A MEMÓRIA AOS POUCOS COM UMA LISTA DE NÚMEROS ABSURDA, ATÉ QUE O PC TRAVE.
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

lista1 = [1,2,3,4,5,6]
lista2 = [6,7,8,9,10]


def soma(*args):
    lista_soma = [x + y for x,y in zip(args)]

print(soma(lista1,lista2))


