#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


def expression_validator():
    stack = []
    math_expression = str(input('Enter a valid math expression: '))
    for value in math_expression:
        if value in "(":
            stack.append("(")
        if len(stack) > 0: 
                if value in ")":
                    stack.pop()
        else:
            stack.append(')')
            break
    if len(stack) > 0:
        print('Invalid!')
    else:
        print('Valid!')


teste = expression_validator()