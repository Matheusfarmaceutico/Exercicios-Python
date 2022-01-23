from datetime import date
ano=int(input('Digite um ano para saber se ele é bissexto. Digite 0 para saber se o ano atual é bissexto:'))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
#Precisa-se de 2 ou tres requisitos para um ano ser bissexto: (1)Ele precisa ser divisivel por 4, não ser divisivel por 100 ou talvez
#ser divisivel por 400. Os dois primeiros são obrigatórios quando pelo menos um deles se mostra verdadeiro. Por exemplo, 2016
#é bissesto (2016%4=504) (2016%100=20,16) (2016%400=5,04) Se os dois primeiros não se confirmassem, e o terceiro se provasse verdadeiro
#o ano seria bissexto.