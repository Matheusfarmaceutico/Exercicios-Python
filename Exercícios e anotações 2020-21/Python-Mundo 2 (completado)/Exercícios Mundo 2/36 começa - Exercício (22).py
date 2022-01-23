s=0
totmulher20=0
nomehomemvelho=''
idadehomemvelho=0
c=0
for dados in range (1,5):
    print('-=-=-=-= {} PESSOA -=-=-=-='.format(dados))
    nome=str(input('Digite o seu nome:')).upper().strip()
    idade=int(input('Digite a sua idade:'))
    print('[M] Masculino\n[F] Feminino ')
    sexo=str(input('Digite a letra que corresponda ao seu sexo:')).upper().strip()
    s=s+idade
    c=c+1
    if dados==1 and sexo in'Mm':
        idadehomemvelho=idade
        nomehomemvelho=nome
    if sexo in'Mm' and idade>idadehomemvelho:
        idadehomemvelho=idade
        nomehomemvelho=nome
    if sexo in 'Ff' and idade<20:
        totmulher20=totmulher20+1
media=s/c
print('A média da idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(idadehomemvelho,nomehomemvelho))
print('A quantidade de mulheres com menos de vinte anos é {}'.format(totmulher20))