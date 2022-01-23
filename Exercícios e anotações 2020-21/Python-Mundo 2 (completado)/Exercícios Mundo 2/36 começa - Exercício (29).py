resp='S'
s=c=maior=menor=0
while resp in 'Ss':
    num=int(input('Digite um número:'))
    resp=str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    s=s+num
    c=c+1
    if c==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
media=s/c
print('ACABOU! A média foi {}. O maior foi {} e o menor {}'.format(media,maior,menor))