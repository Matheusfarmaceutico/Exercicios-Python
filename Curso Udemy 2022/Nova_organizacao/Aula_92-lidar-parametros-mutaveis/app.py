def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista

gabigol = []
clientes1 = lista_de_clientes(["Joao","Maria","Rodrigo"])
# Perceba que quando eu seto um valor para o segundo argumento, o valor padrao da lista é mudado, fazendo com que seja resetado e n haja repeticao de valores.
clientes2 = lista_de_clientes(["Marcos","Henrique","Antonio"],gabigol)
clientes3 = lista_de_clientes(["Matheus","Ribamar","Kauan"])
print(f'{" Primeiro exemplo ":=^40}')
print(clientes1)
print(clientes2)

print("-="*30)
# A questao é que n seria interessante eu obrigar a utilizacao de um 2 parametro, entao posso resolver isso da seguinte forma.
def lista_de_clientes2(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista
# Observe que acima eu setei lista=None (None é um valor imutavel em python). Entao se lista is None, quer dizer que nao foi enviado uma lista como 2 argumento, sendo seu conteudo alterado para uma lista vazia.
print(f'{" Segundo exemplo ":=^40}')
clientes1 = lista_de_clientes2(["Joao","Maria","Rodrigo"])
clientes2 = lista_de_clientes2(["Marcos","Henrique","Antonio"])
clientes3 = lista_de_clientes2(["Matheus","Ribamar","Kauan"])
print(clientes1)
print(clientes2)
print(clientes3)
#note que os prints sao os ultimos a serem executados no debug, isso mostra o motivo de variaveis modificarem quando n estamos utilizando um segundo arg setado com None, tuple, strings, False ou True (valores imutáveis)