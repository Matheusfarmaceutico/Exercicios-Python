perguntas = {
    'Pergunta 01':
    {'pergunta':'Quanto é 2 + 2?',
    'alternativas':{'a':'1','b':'4','c':'15'},
    'resposta_certa': 'b'},
    'Pergunta 02':
    {'pergunta':'Quanto é 6 + 6?',
    'alternativas':{'a':'13','b':'14','c':'12'},
    'resposta_certa':'c'},
}
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Alternativas: ')
    for rk, rv in pv['alternativas'].items():
        print(f'[{rk}]: {rv}')


    usr_resp = input('Digite a sua resposta: ')


    quant_acertos = 0
    if usr_resp == pv['resposta_certa']:
        print('Resposta Correta!')
        quant_acertos += 1
    else:
        print('Resposta Errada!')
    print()
quant_perguntas = len(perguntas)
print(quant_perguntas)
    
        
        

        




