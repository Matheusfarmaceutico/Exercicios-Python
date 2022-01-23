km=float(input('Digite a velocidade do veículo:'))
if km>80.00:
    print('VOCÊ FOI MULTADO! PAGUE R${:.2f}'.format((km-80)*7.00))
else:
    print('DENTRO DA VELOCIDADE PERMITIDA!\nSIGA EM FRENTE!\nBOA VIAGEM!')