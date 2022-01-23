num=(float(input('Digite o seu salário para saber quanto ganhará com 15% de aumento:R$')))
m=(num*15/100)
print('Seu novo salário é de R${:.2F}'.format(num+m))
print('O aumento (em reais) foi de R${:.2f}'.format(m))