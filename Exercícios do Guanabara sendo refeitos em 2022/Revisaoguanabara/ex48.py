"""exercício Python 048: Faça um programa que calcule a soma entre todos os números que são ÍMPARES
 múltiplos de três e que se
 encontram no intervalo de 1 até 500."""
s = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
        print(c, end=' ')
print()
print(f'A Soma  dos {cont} números ímpares múltiplos de 3 é {s}')
