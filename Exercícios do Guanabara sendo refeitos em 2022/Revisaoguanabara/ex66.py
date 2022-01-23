"""Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só
 vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
  quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)."""
c = s = 0
while True:
    try:
        n = int(input(f'Digite um  {c + 1} número:  '))
    except:
        print('Digite um valor válido!')
        continue
    if n != 999:
        c += 1
        s += n
    else:
        break
print(f'A soma dos {c} valores digitados é {s}')
