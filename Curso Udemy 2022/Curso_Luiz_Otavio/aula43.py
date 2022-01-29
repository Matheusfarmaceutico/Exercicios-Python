# desempacotamento de lista:
"""lista = ['Joao', 'Maria', 'Renata']
n1, n2, n3 = lista
print(n2)"""

lista = ['João','Maria','Rafael','Sempre','Amado']
n1, n2, *novalista, ultimodalista = lista
print(novalista)  # desempacotamento de lista criando outra lista
print(ultimodalista)