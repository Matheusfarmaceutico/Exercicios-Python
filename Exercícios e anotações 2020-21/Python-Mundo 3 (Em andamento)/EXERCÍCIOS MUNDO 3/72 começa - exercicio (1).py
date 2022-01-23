#Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso=('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE')
while True:
    num=int(input('Digite um número de 0 até 20:'))
    print(f'O número digitado por extenso foi {extenso[num]} ')
    opção=str(input('Deseja continuar? [S/N]:')).upper().strip()[0]
    if opção=='N':
        break
print('PROGRAMA FINALIZADO!')