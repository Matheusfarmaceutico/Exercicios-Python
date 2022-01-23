n1=int(input('Digite o Primeiro Termo:'))
razão=int(input('Digite a Razão:'))
pa=n1+(10-1)*razão
for c in range(n1,pa+razão,razão):
    print(c,end=' - ')
print('ACABOU')

