s=c=0
while True:
    num=int(input('Digite um número:'))
    if num == 999:
        break
    c=c+1
    s=s+num

print('A soma dos números é {}'.format(s))
