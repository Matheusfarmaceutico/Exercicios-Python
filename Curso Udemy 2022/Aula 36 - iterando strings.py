# Desafio Iterar frase
"""frase = 'O rato roeu a roupa do rei de roma'
cont = 0
nova = ''
option = input('LETRA: ')
while cont < len(frase):
    if frase[cont] == option:
        nova += option.upper()
    else:
        nova = frase[cont]
    print(nova,end='')
    cont += 1""" # COM WHILE, O QUE FOI USADO NA AULA!
# COM FOR, MAIS ADEQUADO:
frase = 'O rato roeu a roupa do rei de roma'
letra = input('LETRA: ')
for l in frase:
    if l == letra:
        maiuscula = l.upper()
        print(maiuscula,end='')
    else:
        print(l,end='')

