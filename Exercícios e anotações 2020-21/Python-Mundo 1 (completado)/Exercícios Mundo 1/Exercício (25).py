import random
a1=input('Escreva o nome do PRIMEIRO aluno')
a2=input('Escreva o nome do SEGUNDO aluno')
a3=input('Escreva o nome do TERCEIRO aluno')
a4=input('Escreva o nome do Qaurto aluno')
lista=[a1,a2,a3,a4]
n=random.shuffle(lista)
print('A ordem é')
print(lista)
