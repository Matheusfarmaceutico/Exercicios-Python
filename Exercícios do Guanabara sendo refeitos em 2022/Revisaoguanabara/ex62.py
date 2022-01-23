""""Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
termo = int(input('Digite o primeiro termo desta PA: '))
razao = int(input('Digite a razão: '))
cont = 1
total = 0
pausa = 10
while pausa != 0:
    total += pausa
    while cont <= total:
        print(termo,end= '->')
        termo += razao
        cont += 1
    print('PAUSA')
    pausa = int(input('Quer continuar? Para sair [0]: '))
print(f'FIM PA finalizada com {total} termos mostrados')