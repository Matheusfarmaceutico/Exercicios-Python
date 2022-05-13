

from dados import dados,pessoas,lista
from separador import separador
import sys

# 1 - Utilizando map
print("Utilizando map")
print()
print(lista)
nova_lista = map(lambda x: x * 2, lista)
print(list(nova_lista))
print(f"Tamanho em bytes que map utiliza: {sys.getsizeof(nova_lista)}")


# 2 - Utilizando list comprehension
print("Utilizando listas comprehensions")
print()
utilizando_list_comp = [x * 2 for  x in lista]
print(utilizando_list_comp)
print(f"Tamanho em bytes utilizando list comprehension: {sys.getsizeof(utilizando_list_comp)}")


# 3 = Atualizando valores em tabelas com map
## 3.1 - Atualizando preços
def att_precos(p):
    p["preco"] = round(p["preco"] * 1.50,2)
    return p


novos_produtos = map(att_precos,dados)

for v in novos_produtos:
    print(v)
print(separador())
## 3.2 - Deixando apenas nomes de pessoas numa lista com outras informações, como idade, etc.

# Demostrando o db com todos os valores

for dados_totais in pessoas:
    print(dados_totais)
print(separador())

# Criando uma lista apenas com os nomes

def sep_nome(nome):
    return nome["nome"]

only = map(sep_nome,pessoas)
for v in only:
    print(v)
print(separador())
# obs: nesse caso, eu poderia ter feito com func lambdas, já que n precisei atualizar a lista, e sim retornar os nomes apenas.

only2 = map(lambda nome: nome["nome"],pessoas)

for v in only2:
    print(v)


