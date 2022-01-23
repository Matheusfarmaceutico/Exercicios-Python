nome=str(input('\033[1;30mQual é o seu nome? ')).capitalize()
if nome=='Matheus':
    print('\033[0;35mQue belo nome!')
elif nome=='Pedro'or nome== 'Maria' or nome=='João' or nome=='Paulo':
    print('\033[0;34mSeu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem comum, mas não tão popular.')
print('\033[1;33mTENHA UM BOM DIA, \033[0;31m{}!'.format(nome))