


lista = []
while True:
    try:
        valor = int(input('Digite um valor: '))
    except:
        print('Digite um valor válido!')
        continue
    if valor not in lista:
        valor = lista.append(valor)
    else:
        print('Valor já consta na lista. Tente novamente.')
        continue
    option = ' '
    while option not in 'SsNn':
        option = str(input('Quer continuar cadastrando? [S/N]: '))
    if option in 'Nn':
        break
print(f'Você digitou os valores {lista}')
print(f'Esses valores em ordem crescente são {sorted(lista)}')