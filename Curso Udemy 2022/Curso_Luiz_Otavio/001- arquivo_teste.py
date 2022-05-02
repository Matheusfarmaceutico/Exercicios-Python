import sys
lista = list(range(10))
print(lista)
print(sys.getsizeof(lista))

lista2 = [x for x in range(10)]
print(lista2)
print(sys.getsizeof(lista2))