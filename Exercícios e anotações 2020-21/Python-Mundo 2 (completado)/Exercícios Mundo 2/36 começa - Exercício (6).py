from datetime import date
ano=int(input('Digite o ano de nascimento do atleta:'))
atual=date.today().year
idade=atual-ano
if idade<=9:
    print('O atleta tem {} ano(s). Sendo assim, está na categoria MIRIM.'.format(idade))
elif idade<=14:
    print('O atleta tem {} ano(s). Sendo assim, está na categoria INFANTIL.'.format(idade))
elif idade<=19:
    print('O atleta tem {} ano(s). Sendo assim, está na categoria JUNIOR'.format(idade))
elif idade<=20:
    print('O atleta tem {} ano(s). Sendo assim, está na categoria Sênior'.format(idade))
elif idade>20:
    print('O atleta tem {} ano(s). Sendo assim, está na categoria MASTER.'.format(idade))