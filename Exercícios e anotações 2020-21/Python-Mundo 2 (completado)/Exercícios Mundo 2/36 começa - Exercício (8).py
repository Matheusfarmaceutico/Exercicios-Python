peso=float(input('Digite o seu peso:'))
altura=float(input('Digite a sua altura:'))
imc=peso/altura**2
if imc<18.5:
    print('Seu IMC é de {:.1f}. Você está abaixo do peso ideal.'.format(imc))
elif imc>=18.5 and imc<25:
    print('Seu IMC é de {:.1f}. Você está no peso ideal.'.format(imc))
elif imc>=25 and imc<30:
    print('Seu IMC é de {:.1f}. Você está com sobrepeso.'.format(imc))
elif imc>=30 and imc<40:
    print('Cuidado! Você está com obesidade, seu IMC É de {:.1f}'.format(imc))
elif imc>=40:
    print('Cuidado! Você está com obesidade mórbida! Seu IMC é de {:.1f}'.format(imc))