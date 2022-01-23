num=1
par=impar=0
while num!=0:
    num=int(input('Digite números para saber quantos deles são pares e ímpares:'))
    if num!=0:
        if num%2==0:
            par=par+1
        else:
            impar=impar+1
print('{} números são pares e {} impares!'.format(par,impar))