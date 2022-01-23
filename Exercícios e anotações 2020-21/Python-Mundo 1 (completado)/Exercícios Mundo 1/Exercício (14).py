num=(float(input('Digite um preço para saber quanto pagará com 5% de desconto: R$')))
m=5*num/100
print('o valor com desconto é de R${:.2f}'.format(num-m))
print ('Você economiza R${:.2f}'.format(m))