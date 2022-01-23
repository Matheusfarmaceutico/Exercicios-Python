#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
idadecont=homenscont=mulherjovenscont=0
while True:
    print('==== CADASTRE UMA PESSOA ====')
    idade=int(input('Qual é a sua idade? '))
    if idade>=18:
        idadecont+=1
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Qual é o seu sexo? [M/F]:')).upper().strip()[0]
        if sexo=='M':
            homenscont+=1
        if sexo=='F':
            if idade<20:
                mulherjovenscont+=1
    opção=' '
    while opção not in 'SN':
        opção=str(input('Quer continuar? [S/N]:')).upper().strip()
    if opção=='N':
            break
print(f'PROGRAMA FINALIZADO! {idadecont} pessoas são maiores de idade\n{homenscont} homens foram cadastrados\n{mulherjovenscont} mulheres têm menos de 20 anos')
