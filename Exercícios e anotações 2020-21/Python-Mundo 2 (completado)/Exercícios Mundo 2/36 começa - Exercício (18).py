frase=str(input('Digite uma frase:')).strip().upper()
palavras=frase.split()
juntos=''.join(palavras)
inverso=''
for letra in range(len(juntos)-1,-1,-1):
    inverso+=juntos[letra]
if juntos==inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo.')
print(juntos,'/',inverso)

##maneira mais longa e difícil!