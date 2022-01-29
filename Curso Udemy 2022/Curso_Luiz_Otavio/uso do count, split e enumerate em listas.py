"""string = 'O Brasil é o país do futebol, o Brasil pentacampeão.'
lista_1 = string.split(' ')
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)} x na frase')"""

'''string = 'O Brasil Brasil I I I I'
lista_1 = string.split(' ')
palavra = ''
cont = 0
for valor in lista_1:
    quantvezes = lista_1.count(valor)
    if quantvezes > cont:
        cont = quantvezes
        palavra = valor
print(f'A palavra que mais apareceu nessa frase foi {palavra} ')'''  # exemplos de split
# uso do join abaixo:

'''lista = ['Ana', 'Coreta']
juntar = '-'.join(lista)
print(juntar)'''
# uso do enumerate: Retorna tuplas
'''lista = ['Jogador','Numero']
for indice, valor in enumerate(lista):
    print(indice,valor)'''
# é possível mudar a key (índice) do enumerate, iniciando por exemplo com 50
lista = ['Matheus','Ana','Júlia']
for i, v in enumerate(lista,50):
    print(i,v)
