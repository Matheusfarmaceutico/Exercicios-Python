""""variavel = ['Matheus','Luana','Renata','Cláudia']
for n in variavel:
    if n.startswith('M'):
        print('Começa com M')
    else:
        print('Não começa com M')"""
# outra forma de fazer utilizando bool


pass
"""variavel = ['Matheus','Luana','Renata','Cláudia', 'João']
comeca_j = False
for p in variavel:
    if p.startswith('J'):
        comeca_j = True
if comeca_j:
    print(f'Há uma palavra que começa com j')
else:
    print(f'Nenhuma palavra começa com J')"""
pass

"""variavel = ['Matheus','Luana','Renata','Cláudia', 'João']
for v in variavel:
    if v.lower().startswith('j'):
        print(f'{v} começa com j')
        break
else:
    print('Nenhum valor começa com j')"""
pass

variavel = ['Matheus','Luana','Renata','Cláudia', 'João']
for v in variavel:
    if v.lower().startswith('j'):
        continue
    print(v) # pular execução de um elemento
