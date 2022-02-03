#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
parentheses = []
exp = str(input('Enter a valid mathematical expression: '))
for value in exp:
    if value in '(':
        parentheses.append(value)
    elif value in ')':
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append(')')
            
if len(parentheses) == 0:
    print('Valid!')
else:
    print('Invalid!')
