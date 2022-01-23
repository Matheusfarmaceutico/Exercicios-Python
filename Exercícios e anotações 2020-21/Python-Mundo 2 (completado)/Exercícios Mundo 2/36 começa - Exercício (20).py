maior=0
menor=0
from datetime import date
for pessoa in range (1,8):
    nascimento=int(input('Digite o seu ano de nascimento:'))
    idade=date.today().year-nascimento
    if idade>=21:
        maior=maior+1
    else:
        menor=menor+1
print('{} pessoa(s) são maiores de idade.'.format(maior))
print('{} pessoas(s) são menores de idade.'.format(menor))


