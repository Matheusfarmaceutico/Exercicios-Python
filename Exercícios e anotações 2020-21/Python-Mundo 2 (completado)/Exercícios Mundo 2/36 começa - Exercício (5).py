
n1=float(input('Digite a sua PRIMEIRA nota:'))
n2=float(input('Digite a sua SEGUNDA nota:'))
media=(n1+n2)/2
if media<5.0:
    print('Sua média é {:.1f}, abaixo de 5.0, por isso \033[31mvocê foi REPROVADO!'.format(media))
elif media<5.0 or media<=6.9:
    print('Sua média é {:.1f}'.format(media))
    print('\033[33mFICOU DE RECUPERAÇÃO!')
elif media>=7.0:
    print('Sua média foi {:.1f}. \033[34mVOCÊ FOI APROVADO!'.format(media))