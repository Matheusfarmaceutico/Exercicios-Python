from random import randint
while True:
    cpf = str(randint(100000000, 999999999))
    total = 0
    novo_cpf = cpf
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
    print(novo_cpf)
    option = ' '
    while option not in 'SsNn':
        option = str(input('Gerar mais um CPF?'))
    if option in 'Nn':
        break