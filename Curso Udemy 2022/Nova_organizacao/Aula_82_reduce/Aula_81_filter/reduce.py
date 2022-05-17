
from separador import separador
from dados import pessoas, produtos, lista
from functools import reduce
from sys import getsizeof

print("Acumulando (somando) valores de uma lista utilizando reduce")
somar_lista = reduce(lambda ac,i: i + ac,lista,0)

#ac: acumulador
#i: item
print(somar_lista)
print (f"Tamanho em bytes: {getsizeof(somar_lista)}")

print(separador())

print("Acumulando (somando) valores de precos armezenados em dicionários com reduce")

somar_produto = reduce(lambda ac,i: ac + i["preco"],produtos,0)
print(round(somar_produto,2))

print(separador())

print("Tirando médias de idades com reduce")

media_idades = reduce(lambda ac,i: ac + i["idade"], pessoas,0)
print(media_idades/len(pessoas))