"""def inverter_nomes(nome, sobrenome):
    trocar = sobrenome + ',' + nome
    return trocar


print('Lista de alimentos: banana, maçã, abacate, etc')
print(inverter_nomes(input('Digite o primeiro nome:' ), input('Digite o Segundo nome: ')))"""


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1/n2
    # se nao, é um valor false.


v1 = int(input('N1: '))
v2 = int(input('N2: '))
conta_dividir = divisao(v1, v2)

if conta_dividir:  # checando se é um valor True
    print(conta_dividir)
else:
    print('inválido!')
