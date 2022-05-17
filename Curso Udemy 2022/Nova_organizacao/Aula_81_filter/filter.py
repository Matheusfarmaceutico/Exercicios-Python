

from dados import produtos,pessoas,lista
from separador import separador
import sys

print("Utilizando Filter")
nova_lista = filter(lambda x: x > 5, lista)
print(f"Tamanho em bytes {sys.getsizeof(nova_lista)}")

print(list(nova_lista))

print(separador())

print("Utilizando list comprehension")

nova_lista2 = [x for x in lista if x > 5]
print(nova_lista2)
print(f"Tamanho em bytes: {sys.getsizeof(nova_lista2)}")
print(separador())

print("Filtrar produtos maiores do que determinado valor através de filter + lambda: ")

filtrar_produto_lambda = filter(lambda x: x['preco'] > 50,produtos)
for v in filtrar_produto_lambda:
    print(v)

print(separador())
print("Filtrar produtos maiores do que determinado valor através de filter + funcao: ")

def filtra(produto):
    if produto['preco'] > 50:
        return True

filtrar_produto_funcao = filter(filtra, produtos)

for v in filtrar_produto_funcao:
    print(v)

print(separador())

print("Posso mimetizar o map utilizando o Filter")


def filtra2(produto):
    if produto["preco"] > 50:
        produto["Desconto"] = "Ativo"
    return True


mimetizar = filter(filtra2,produtos)


for v in mimetizar:
    print(v)

print(separador())


filtrar_sujeito = filter(lambda pessoa: pessoa['idade'] < 30,pessoas)

for pessoa in filtrar_sujeito:
    print(pessoa)