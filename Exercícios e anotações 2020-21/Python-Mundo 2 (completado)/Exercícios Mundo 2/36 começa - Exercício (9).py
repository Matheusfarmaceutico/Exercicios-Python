print('{:=^40}'.format(' LOJAS ITA '))
preço=float(input('Digite o preço do produto R$'))
print('''Escolha uma opção válida:
[1]à vista no dinheiro/cheque com 10% de desconto
[2]à vista no cartão com 5% de desconto
[3]2x sem juros no cartão
[4]3x ou mais no cartão com 20% de acréscimo''')
opção=int(input('Qual a sua opção? '))
if opção==1:
    total=preço-(preço*10/100)
    print('Sua compra de R${:.2f} sairá por {:.2f}'.format(preço, total))
if opção==2:
    total=preço-(preço*5/100)
    print('Sua compra de R${:.2f} sairá por {:.2f}'.format(preço, total))
if opção==3:
    total=preço
    prestação=preço/2
    print('Em 2x sem juros, no cartão, você pagará R${:.2f}'.format(prestação))
    print('Sua compra de R${:.2f} sairá por {:.2f}'.format(preço, total))
if opção==4:
    total=preço+(preço*20/100)
    parcelas=int(input('Digite a quantidade de parcelas:'))
    if parcelas<3:
        print('Opção Inválida! A quantidade mínima de parcelas é 3.')
    if parcelas>=3:
        print('Você pagará {} parcelas de R${:.2f}'.format(parcelas,total/parcelas))
        print('Sua compra de R${:.2f} sairá por {:.2f}'.format(preço, total))
else:
    print('Opção inválida! Tente novamente!')