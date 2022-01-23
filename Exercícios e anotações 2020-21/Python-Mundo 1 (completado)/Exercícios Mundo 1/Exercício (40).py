a=float(input('Digite a primeira reta:'))
b=float(input('Digite a segunda reta:'))
c=float(input('Digite a terceira reta:'))
if a+b>c and a+c>b and b+c>a:
    print('A retas {},{} e {} podem formar um triângulo'.format(a,b,c))
else:
    print('As retas {}, {} e {} não podem formar um triângulo'.format(a,b,c))