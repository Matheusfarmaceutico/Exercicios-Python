from itertools import groupby
def separador():
    return "-="*30



alunos = [
    {"Nome":"Luiz","nota":"A"},
    {"Nome":"Letícia","nota":"B"},
    {"Nome":"Fabrício","nota":"A"},
    {"Nome":"Rosemary","nota":"C"},
    {"Nome":"Joana","nota":"D"},
    {"Nome":"João", "nota":"A"},{"Nome":"Eduardo", "nota":"B"},{"Nome":"André", "nota":"A"},{"Nome":"Anderson", "nota":"C"},
    {"Nome":"José", "nota":"B"},
]
#Utilizando lambda
alunos.sort(key = lambda item: item['nota'])
# Para que sort consiga ordenar o dicionário, ele precisa de uma função (nesse caso uma função lambda) para extrair a nota para aí sim organizar.
print(alunos)
print(separador())
#utilizando funcões

alunos = [
    {"Nome":"Luiz","nota":"A"},
    {"Nome":"Letícia","nota":"B"},
    {"Nome":"Fabrício","nota":"A"},
    {"Nome":"Rosemary","nota":"C"},
    {"Nome":"Joana","nota":"D"},
    {"Nome":"João", "nota":"A"},{"Nome":"Eduardo", "nota":"B"},{"Nome":"André", "nota":"A"},{"Nome":"Anderson", "nota":"C"},
    {"Nome":"José", "nota":"B"},
]
def org(item):
    return item["nota"]

alunos.sort(key = org)

print(separador())
#exibindo com for, para ficar mais claro.
alunos = [
    {"Nome":"Luiz","nota":"A"},
    {"Nome":"Letícia","nota":"B"},
    {"Nome":"Fabrício","nota":"A"},
    {"Nome":"Rosemary","nota":"C"},
    {"Nome":"Joana","nota":"D"},
    {"Nome":"João", "nota":"A"},{"Nome":"Eduardo", "nota":"B"},{"Nome":"André", "nota":"A"},{"Nome":"Anderson", "nota":"C"},
    {"Nome":"José", "nota":"B"},
]
alunos.sort(key= lambda item: item["nota"])
for v in alunos:
    print(v)

print(separador())


#agrupando, de fato, os grupos.
alunos = [
    {"Nome":"Luiz","nota":"A"},
    {"Nome":"Letícia","nota":"B"},
    {"Nome":"Fabrício","nota":"A"},
    {"Nome":"Rosemary","nota":"C"},
    {"Nome":"Joana","nota":"D"},
    {"Nome":"João", "nota":"A"},{"Nome":"Eduardo", "nota":"B"},{"Nome":"André", "nota":"A"},{"Nome":"Anderson", "nota":"C"},
    {"Nome":"José", "nota":"B"},
]

ordena = lambda item: item["nota"]
alunos.sort(key = ordena)
agrupar = groupby(alunos,ordena)

for agrupamento, valores_agrupados in agrupar:
    print(f'Agrupamento: {agrupamento}')
    valores_agrupados = list(valores_agrupados)
    for pessoas in valores_agrupados:
        print(pessoas)
