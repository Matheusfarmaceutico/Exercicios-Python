dis=(float(input('Digite a quantidade de Km:')))
if dis<=200:
    print('O preço da passagem será de R${:.2f}'.format(dis*0.50))
else:
    print('O preço da passagem será de R${:.2f}'.format(dis*0.45))