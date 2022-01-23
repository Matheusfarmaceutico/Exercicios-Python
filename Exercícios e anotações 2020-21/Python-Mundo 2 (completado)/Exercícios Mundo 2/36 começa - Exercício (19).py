frase=str(input('Digite uma frase:')).upper().strip()
separar=frase.split()
juntar=''.join(separar)
inverso=juntar[::-1]
if juntar==inverso:
    print('É um palíndromo! {}/{}'.format(juntar,inverso))
else:
    print('Não é um palíndromo! {}/{}'.format(juntar,inverso))
