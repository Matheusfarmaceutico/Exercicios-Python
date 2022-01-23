num=int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:\n[1]BINÁRIO\n[2]OCTAL\n[3]HEXADECIMAL\n')
opção=int(input('Digite sua opção:'))
if opção==1:
    print('{} convertido para binário é {}'.format(num,bin(num)[2:]))
elif opção==2:
    print('{} convertido para OCTAL é {}'.format(num,oct(num)[2:]))
elif opção==3:
    print('{} convertido para HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.Escolha entre:(1) para BINÁRIO; (2) para OCTAL e (3) para HEXADECIMAL')

