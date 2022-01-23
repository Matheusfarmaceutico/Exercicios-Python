while True:
    num=int(input('Digite um número para ver sua tabuada:'))
    if num<0:
        break
    for c in range(1,11):
        m=num*c
        print(f'{num} X {c} = {m}')
print('FIM DO PROGRAMA!')