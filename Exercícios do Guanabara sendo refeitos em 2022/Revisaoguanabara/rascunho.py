lista = []
while True:
    valor = int(input('Digite um valor: '))
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
print(lista)