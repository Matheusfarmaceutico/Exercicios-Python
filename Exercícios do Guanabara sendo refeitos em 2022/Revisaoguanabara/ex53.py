"""Exercício Python 053: Crie um programa que leia uma frase qualquer e
diga se ela é um palíndromo, desconsiderando os espaços."""
# MINHA SOLUÇÃO MAIS ENXUTA!
phrase = str(input('Enter a phrase: ')).strip().upper()
phrase = phrase.replace(' ','')
reverse = phrase[::-1]
print(f'The reverse of {phrase} is {reverse}, so',end=' ')
if phrase == reverse:
    print('\033[33mWe got a palindrome! ',end=' ')
else:
    print("\033[31mWe don't have a palindrome! ",end=' ')