n1=int(input('Digite um número para saber o seu fatorial:'))
c=n1
f=1
while c>0:
    print('{}'.format(c) ,end='')
    print(' x ' if c>1 else ' = ',end='')
    f=f*c
    c=c-1
print('{}'.format(f))

#sem modúlo math factorial
