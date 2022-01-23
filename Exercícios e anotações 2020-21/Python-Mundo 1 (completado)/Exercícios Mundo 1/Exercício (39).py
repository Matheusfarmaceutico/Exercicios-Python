salario=(float(input('Digite seu salário: R$')))
if salario>1250.00:
    print('Seu novo salário é de R${:.2f}'.format(salario+(salario*10/100)))
if salario<=1250.00:
    print('Seu novo salário é de R${:.2f}'.format(salario+(salario*15/100)))