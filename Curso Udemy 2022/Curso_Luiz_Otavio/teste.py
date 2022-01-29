nomes = []
def cadastro(*adicionar):
    while True:
        nomes.append(adicionar)
        option = ' '
        option = str(input('Quer continuar? [S/N]: '))
        if option in 'Ss':
            cadastro(str(input('Adicione mais:  ')))
        if option in 'Nn':
            break
    
        
        

        



users = str(input('Cadastre um usuário: '))
cadastro(users)


