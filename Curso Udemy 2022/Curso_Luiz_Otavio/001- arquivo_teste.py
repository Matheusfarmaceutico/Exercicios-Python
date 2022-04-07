
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