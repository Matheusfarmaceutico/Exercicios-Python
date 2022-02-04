#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

def math_expression_validator(user_expression):
    stack = []
    for value in user_expression:
        if value == '(':
            stack.append('(')
        elif value == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(')')
                break
                
                
    if len(stack) > 0:
        return 'Invalid!'
    else:
       return 'Valid!'




validate_express = math_expression_validator(str(input('Enter a valid math expression: ')))
print(validate_express)

