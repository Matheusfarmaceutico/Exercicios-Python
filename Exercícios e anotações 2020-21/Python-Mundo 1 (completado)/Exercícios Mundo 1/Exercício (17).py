dias=int(input('Quantos dias:'))
km=float(input('Quantos km:'))
pago=(dias*60)+(0.15*km)
print('O total a pagar será de R${:.2f}'.format(pago))