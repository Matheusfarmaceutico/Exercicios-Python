while True:
    cpf = input('Digite um CPF VÁLIDO: ')
    st = ['-','.',',',' ']
    for c, v in enumerate(st):
        if v in cpf:
            cpf = cpf.replace(v, '')
    if len(cpf) != 11:
        print(f"""\033[31mNúmero de caracteres inválidos, você inseriu {len(cpf)} (um número de cpf é formado por 11 
dígitos) e/ ou inserção de caracteres não permitidos.""")
        print('\033[35mCaracteres permitidos "-" "." "espaço vazio" ","')
        print('\033[m')
        continue
    total = 0
    novo_cpf = cpf[:-2]
    reverso = 10
    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    sequencia = novo_cpf == novo_cpf[0] * len(novo_cpf)
    if cpf == novo_cpf and not sequencia:
        print('CPF VÁLIDO')
    else:
        print('CPF INVÁLIDO!')
    option = ' '
    while option not in 'SsNn':
        option = str(input('Quer continuar? [S/N]: '))
    if option in 'Nn':
        break
