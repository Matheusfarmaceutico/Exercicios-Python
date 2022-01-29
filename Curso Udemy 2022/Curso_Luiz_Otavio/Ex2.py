"""
Faça um programa que pergunte a hora ao usuário e dê a ele uma saudação correspondente. (Bom dia: 0-11:00;
Boa tarde: 12-17; Boa noite: 18:00-23:00
"""
while True:
    try:
        hora_string = input("Que horas são? (hh:mm): ")
        hora = int(hora_string.split(':')[0])
        minuto = int(hora_string.split(':')[1])
        if hora < 0 or hora > 23:
            print('Horário inválido! Ele deve estar entre 00:00 e 23:59')
        elif hora <= 11:
            print('Bom dia')
            break
        elif hora <= 17:
            print('Boa tarde!')
            break
        else:
            print('Boa noite!')
            break

    except:
        print('Caracteres inválidos!')
print(f'Você disse que são {hora:0>2}:{minuto:0<2} ')
