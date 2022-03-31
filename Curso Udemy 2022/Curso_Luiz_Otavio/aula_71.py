


'''lista = "Matheus"
lista = iter(lista)
print(hasattr(lista,"__next__"))
lista3 = [1,2,3]
print(hasattr(lista3, "__next__"))
print(hasattr(lista3, "__iter__")) # uma lista normal é iteravel (__iter__) mas nao é iteradora (__next__)'''


lista = "Matheus"
lista = iter(lista)
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
for v in lista:
    print(v) # note que o for tem meio que uma exceção embutida. Ele n deixa aparecer a msg de erro.

