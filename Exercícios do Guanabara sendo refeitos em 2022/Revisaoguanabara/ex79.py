#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
valores = []
while True:
    try:
        n = int(input('Digite um valor válido: '))
    except:
        print('Apenas números inteiros, por favor.')
        continue
    if n not in valores:
        valores.append(n)
    else:
        print('Valor já presente, não será adicionado')
    option = ' '
    while option not in 'SsNn':
        option = str(input('Quer continuar? [S/N]: '))
    if option in 'Nn':
        break

print(f'Você digitou originalmente os valores {valores}')
print(f'Tais valores ordenados são: {sorted(valores)}')