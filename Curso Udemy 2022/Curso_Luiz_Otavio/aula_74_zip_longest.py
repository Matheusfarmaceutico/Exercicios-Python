
cidades = ["São Paulo","Goiânia","Petrópolis","Belém"]
estados = ["SP","GO","RJ","PA"]
cidades_estados = zip(estados,cidades)
print(id(cidades_estados))


"""for v in cidades_estados:
    print(v[0], v[1])"""

for v in cidades_estados:
    print(v[0], v[1])

    #ou se eu quiser ver o que o resultado originalmente é transformado em tuplas... Lembre-se de excluir o laço for anterior, porque ele foi consumido pelo iterador.
"""for v in cidades_estados:
    print(v[0], v[1])"""

"""Transformando em um dicionário (chave-valor)"""
cidades_estados = zip(estados,cidades)
print(dict(cidades_estados))

""" O melhor nesse caso é deixar como dicionário, pois se houver valores incosistentes em um das duas listas ex: GO, Goiânia, GO (que seria uma trinca nao do tipo chave-valor)  poderia haver algum problema se estivéssemos utilizando dicionários."""

cidades_estados = zip(estados,cidades)
print(list(cidades_estados))


""" Note que o zip une duas listas até o número da menor lista.
Por exemplo, se eliminássemos o estado do PA, ele só reproduziria até RJ: Petrópolis """
cidades = ["São Paulo","Goiânia","Petrópolis","Belém"]
estados = ["SP","GO","RJ"]
cidades_estados = zip(estados,cidades)
print(list(cidades_estados))

"""Contudo,  se eu utilizar o módulo zip_longest da biblioteca itertools o valor faltante será substituido por None. """
from itertools import zip_longest
cidades = ["São Paulo","Goiânia","Petrópolis","Belém"]
estados = ["SP","GO","RJ"]
cidades_estados = zip_longest(estados,cidades)
print(list(cidades_estados))

"""É ainda possível passar um atributo para que o None seja subtituído por qualquer outro valor, como por exemplo: (Estado_nao_inserido, Belém)"""

from itertools import zip_longest
cidades = ["São Paulo","Goiânia","Petrópolis","Belém"]
estados = ["SP","GO","RJ"]
cidades_estados = zip_longest(estados,cidades,fillvalue = 'UF_Nao_Inserida')
print(list(cidades_estados))
print()
"""Criando indices a partir de count. Note que n é possível usar o zip_longest infinito (sem passar os parametros de limite de contagem) pois assim seria gerado um loop infinito."""

from itertools import count
indice = count()
cidades = ["São Paulo","Goiânia","Petrópolis","Belém"]
estados = ["SP","GO","RJ"]
cidades_estados = zip(indice,estados,cidades)
for v in cidades_estados:
    print(v)

""" Se eu quisesse desempacotar as variáveis (as tuplas)"""

from itertools import count
indice = count()
cidades = ["São Paulo","Goiânia","Petrópolis","Belém"]
estados = ["SP","GO","RJ"]
cidades_estados = zip(indice,estados,cidades)
for indice, estados, cidades in cidades_estados:
    print(indice,estados,cidades)
