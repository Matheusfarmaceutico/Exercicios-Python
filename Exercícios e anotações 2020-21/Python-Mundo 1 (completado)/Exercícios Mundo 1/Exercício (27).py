n=input('Por favor, digite seu nome completo:').strip()
print('Em maiúsculo, seu nome é:',(n.upper()))
print('Em minúsculo, seu nome é:',(n.lower()))
print('Seu nome tem {} letras'.format(len(n)-(n.count(' '))))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))