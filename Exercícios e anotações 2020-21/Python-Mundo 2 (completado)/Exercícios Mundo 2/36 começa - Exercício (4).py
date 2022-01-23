from datetime import date
atual=date.today().year
ano=int(input('Digite o ano de seu nascimento:'))
idade=atual-ano
if idade==18:
    print('Você tem 18 anos! Compareça a uma junta militar imediatamente.')
elif idade<18:
    print('Você ainda não tem a idade mínima para se alistar. Falta(m)-te {} ano(s)! Assim, seu ano de alistamento será em {}'.format(18-idade,ano+18))
elif idade >18:
    anoa=ano+18
    print('Você já passou da idade de alistamento, que deveria ter sido em {}! Ou seja, há {} ano(s)'.format(anoa,atual-anoa))
