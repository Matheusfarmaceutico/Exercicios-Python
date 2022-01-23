num=c=s=0
num = int(input('Digite um número:'))
while num!=999:
    s=s+num
    c=c+1
    num=int(input('Digite um número:'))
print('FIM DO PROGRAMA! {} números foram digitados e a soma entre eles é de {}'.format(c,s))