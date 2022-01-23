casa=float(input('Digite o valor do imóvel:'))
salario=float(input('Por favor, digite o valor de seu salário:'))
anos=int(input('Nos diga em quantos anos deseja pagar as parcelas:'))
prestação=casa/anos/12
if prestação<=salario*30/100:
    print('O valor da prestação será de R${:.2f}'.format(prestação))
    print('EMPRÉSTIMO CONCEDIDO!')
else:
    print('Empréstimo negado!')