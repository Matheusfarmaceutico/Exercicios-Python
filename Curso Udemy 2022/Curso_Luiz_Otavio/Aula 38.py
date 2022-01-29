"""lista = ['Banana','Abacate','Repolho','Naruto','BEN10','QUEIJO']
del lista[1::2]
print(lista)"""

"""l2 = list(range(1,300))
print(l2)"""
from random import randint
secreto = ['casa','rapariga','manchete','doente','louco']
secreto = (secreto[randint(0, len(secreto))])
chutes = []
vidas = 3
while True:
    letra = str(input('Chute uma letra: '))
    if len(letra) > 1:
        print('Apenas uma palavra, por favor!')
        continue
    chutes.append(letra)
    if letra in secreto:
        print(f'Letra {letra } presente na palavra secreta')
    else:
        print(f'Erouuuu!')
        vidas -= 1
        chutes.pop()
    if vidas == 0:
        print('Você esgotou o número de tentivas')
        break
    secreto_temporario = ''
    for string in secreto:
        if string in chutes:
            secreto_temporario += string
        else:
            secreto_temporario += '*'
    print(secreto_temporario)
    if secreto_temporario == secreto:
        print('Você ganhou! Fim de jogo.')
        break