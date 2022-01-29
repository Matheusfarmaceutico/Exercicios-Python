"""Crie uma função que receba dois números. O primeiro é um valor e o segundo um percentual (ex 10%)
Faça return o valor do primeiro somado do aumento do percentual. """


def juros(valor,percentual):
    return valor + (valor * percentual / 100)


salario = float(input('Digite seu salário: '))
aumento = float(input('Digite a porcentagem de aumento: '))
reajuste = juros(salario,aumento)
print(f'R${reajuste:.2f}  ')