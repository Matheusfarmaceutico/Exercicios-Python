frase=str(input('Digite uma frase:')).strip().upper()
print('A letra "A" aparece {} vezes nessa frase'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" apareceu pela última vez na posição {}'.format(frase.rfind('A')+1))


