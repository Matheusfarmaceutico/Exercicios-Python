a=int(input('Digite o PRIMEIRO valor:'))
b=int(input('Digite o SEGUNDO valor:'))
c=int(input('Digite o TERCEIRO valor'))

menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=b
if a>b and a>c:
    maior=a
if c>a and c>b:
    maior=c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))