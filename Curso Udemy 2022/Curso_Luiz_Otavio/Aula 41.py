# uso do split e count
'''string = 'O Brasil Brasil I I I I'
lista_1 = string.split(' ')
palavra = ''
cont = 0
for valor in lista_1:
    quantvezes = lista_1.count(valor)
    if quantvezes > cont:
        cont = quantvezes
        palavra = valor
print(f'A palavra que mais apareceu nessa frase foi {palavra} ')'''
# uso do Join
'''lista = ['Ana','Vitória']
juntar = '***'.join(lista)
print(juntar)'''
# uso do enumerate: retorna tuplas
'''lista = ['Jogador','Numero']
for indice, valor in enumerate(lista):
    print(indice,valor)'''
