num=int(input('Digite um número inteiro para ver sua tabuada:'))
print('-='*20)
for c in range(0,11):
    print('{} x {:2} = {}'.format(num,c,num*c))

