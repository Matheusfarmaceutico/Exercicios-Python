from itertools import groupby, tee
from itertools import groupby


def separador():
    return "-="*30


alunos = [
    {"Nome": "Luiz", "nota": "A"},
    {"Nome": "Letícia", "nota": "B"},
    {"Nome": "Fabrício", "nota": "A"},
    {"Nome": "Rosemary", "nota": "C"},
    {"Nome": "Joana", "nota": "D"},
    {"Nome": "João", "nota": "A"}, {"Nome": "Eduardo", "nota": "B"}, {
        "Nome": "André", "nota": "A"}, {"Nome": "Anderson", "nota": "C"},
    {"Nome": "José", "nota": "B"},
]
# Utilizando lambda
alunos.sort(key=lambda item: item['nota'])
# Para que sort consiga ordenar o dicionário, ele precisa de uma função (nesse caso uma função lambda) para extrair a nota para aí sim organizar.
print(alunos)
print(separador())
# utilizando funcões

alunos = [
    {"Nome": "Luiz", "nota": "A"},
    {"Nome": "Letícia", "nota": "B"},
    {"Nome": "Fabrício", "nota": "A"},
    {"Nome": "Rosemary", "nota": "C"},
    {"Nome": "Joana", "nota": "D"},
    {"Nome": "João", "nota": "A"}, {"Nome": "Eduardo", "nota": "B"}, {
        "Nome": "André", "nota": "A"}, {"Nome": "Anderson", "nota": "C"},
    {"Nome": "José", "nota": "B"},
]


def org(item):
    return item["nota"]


alunos.sort(key=org)

print(separador())
# exibindo com for, para ficar mais claro.
alunos = [
    {"Nome": "Luiz", "nota": "A"},
    {"Nome": "Letícia", "nota": "B"},
    {"Nome": "Fabrício", "nota": "A"},
    {"Nome": "Rosemary", "nota": "C"},
    {"Nome": "Joana", "nota": "D"},
    {"Nome": "João", "nota": "A"}, {"Nome": "Eduardo", "nota": "B"}, {
        "Nome": "André", "nota": "A"}, {"Nome": "Anderson", "nota": "C"},
    {"Nome": "José", "nota": "B"},
]
alunos.sort(key=lambda item: item["nota"])
for v in alunos:
    print(v)

print(separador())


# agrupando, de fato, os grupos.

# 1.0 - Verificando quantas pessoas tiram determinada Nota.
alunos = [
    {"Nome": "Luiz", "nota": "A"},
    {"Nome": "Letícia", "nota": "B"},
    {"Nome": "Fabrício", "nota": "A"},
    {"Nome": "Rosemary", "nota": "C"},
    {"Nome": "Joana", "nota": "D"},
    {"Nome": "João", "nota": "A"}, {"Nome": "Eduardo", "nota": "B"}, {
        "Nome": "André", "nota": "A"}, {"Nome": "Anderson", "nota": "C"},
    {"Nome": "José", "nota": "B"},
]


def organizar(item): return item['nota']


alunos.sort(key=organizar)
agrupamento = groupby(alunos, organizar)
for agrupamento, dados_person in agrupamento:
    print(f'Agrupamento: {agrupamento}')
    quantidade = len(list(dados_person))
    print(quantidade)
print(separador())
# 2.0 - Verificando quais pessoas tiraram determinada nota.
alunos = [
    {"Nome": "Luiz", "nota": "A"},
    {"Nome": "Letícia", "nota": "B"},
    {"Nome": "Fabrício", "nota": "A"},
    {"Nome": "Rosemary", "nota": "C"},
    {"Nome": "Joana", "nota": "D"},
    {"Nome": "João", "nota": "A"}, {"Nome": "Eduardo", "nota": "B"}, {
        "Nome": "André", "nota": "A"}, {"Nome": "Anderson", "nota": "C"},
    {"Nome": "José", "nota": "B"},
]


def organizar(item): return item['nota']


alunos.sort(key=organizar)
agrupamento = groupby(alunos, organizar)
for agrupamento, dados_person in agrupamento:
    print()
    print(f'Agrupamento: {agrupamento}')
    print()
    for agrupamento in dados_person:
        print(agrupamento["Nome"])

print(separador())

# 3.0 - Mostrando quantidade pessoas que estao no meu grupo e o nome dessas pessoas.
""" Note que esse vai ser um caso mais complexo, pois uma vez que eu esgoto meu interado..."""
alunos = [
    {"Nome": "Luiz", "nota": "A"},
    {"Nome": "Letícia", "nota": "B"},
    {"Nome": "Fabrício", "nota": "A"},
    {"Nome": "Rosemary", "nota": "C"},
    {"Nome": "Joana", "nota": "D"},
    {"Nome": "João", "nota": "A"}, {"Nome": "Eduardo", "nota": "B"}, {
        "Nome": "André", "nota": "A"}, {"Nome": "Anderson", "nota": "C"},
    {"Nome": "José", "nota": "B"},
]


def organizar(item): return item['nota']


alunos.sort(key=organizar)
agrupamento = groupby(alunos, organizar)
for agrupamento, dados_person in agrupamento:
    print()
    print(f'Agrupamento: {agrupamento}')
    print()
    quantidade = len(list(dados_person))
    print(quantidade)
    for agrupamento in dados_person:
        print(agrupamento["Nome"])
    # Note que eu fizer dessa forma, nao consigo mostrar o nome dos alunos, pois os dados de iteradores já foram consumidos, havendo a necessidade de criar uma cópia de dados_person, através do módulo tee.
print(separador())
alunos = [
    {"Nome": "Luiz", "nota": "A"},
    {"Nome": "Letícia", "nota": "B"},
    {"Nome": "Fabrício", "nota": "A"},
    {"Nome": "Rosemary", "nota": "C"},
    {"Nome": "Joana", "nota": "D"},
    {"Nome": "João", "nota": "A"}, {"Nome": "Eduardo", "nota": "B"}, {
        "Nome": "André", "nota": "A"}, {"Nome": "Anderson", "nota": "C"},
    {"Nome": "José", "nota": "B"},
]


def organizar(iter): return iter["nota"]


alunos_ordenados = sorted(alunos, key=organizar)
grupos_separados = groupby(alunos_ordenados, organizar)

for agrupamentos, full_dados in grupos_separados:
    print()
    print(f"Agrupamentos {agrupamentos}")
    # trata-se de um iterador que se esgota, por isso tee faz duas cópias de "full dados", para que eu consiga exibir os nomes dos alunos e a quantidade deles que tiraram uma determinada nota"
    v1, v2 = tee(full_dados)

    for aluno in v1:
        # V1 é uma cópia de full_dados, e a utilizo aqui para que eu possa exibir o nome do aluno daquele grupamento em específico.
        print(aluno["Nome"])
    # V2 é uma cópia de full_dados, e a utilizo aqui para quantificar quantos alunos estão em um determinado grupamento de notas. Note que preciso v2 (que é um objeto) para uma lista, para que eu quantificar antes de exibir o len, de fato.
    quantidade = len(list(v2))
    print(f"Quantidade de alunos do agrupamento {agrupamentos}:  {quantidade}")
