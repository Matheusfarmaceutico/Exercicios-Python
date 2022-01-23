#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
s=0
lista=('Lápis', 1.70,
       'Caneta',2.00,
       'Caderno',20.00,
       'Estojo colorido',25.00,
       'Lápis de cor',30.00,
       'TOTAL')
print('-='*30)
print('LISTA DE COMPRAS!')
print('-='*30)
for pos in range (0,len(lista)):
    if pos%2==0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        s=s+lista[pos]
        print(f'R${lista[pos]:>7.2f}')
print(f'R${s:>7.2f}')