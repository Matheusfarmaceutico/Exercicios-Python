n1=(float(input('Digite O valor da PRIMEIRA reta:')))
n2=(float(input('Digite o valor da SEGUNDA reta:')))
n3=(float(input('Digite o valor da TERCEIRA reta:')))
if n1+n2>n3 and n1+n3>n2 and n3+n2>n1:
    print('As retas {},{} e {} podem formar um triângulo '.format(n1,n2,n3),end='')
    if n1 == n2 and n1 == n3 and n2 == n3:
        print('equilátero.')
    if n1!=n2 and n1!=n3 and n2!=n3:
        print('escaleno.')
    else:
        print('isósceles.')

else:
    print('As retas {},{} e {} não podem formar um triângulo'.format(n1,n2,n3))


