"""Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
 digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. """
while True:
    try:
        n = int(input('Quer ver uma tabuada de qual número? (número negativo para sair): '))
    except:
        print('Caracter inválido!')
        continue
    if n < 0:
        break
    for c in range(0,11):
        if n >= 0:
            print(f' {n} X {c:2} = {n*c}')


