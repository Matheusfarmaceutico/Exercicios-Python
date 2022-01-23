"""Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo
 e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
# minha solução ainda utilizando a fórmula mesmo com while
'''primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('RAZÃO: '))
cont = primeiro_termo
form = primeiro_termo + (10 - 1) * razao
while cont <= form:
    print(cont,end='-> ')
    cont += razao

print('FIM')'''
# solução do Guanabara, dispensando uso de fórmula

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    print(primeiro,end=' -> ')
    primeiro += razao
    cont += 1
print('FIM')
