program_name = "Matheus's Calculator"
print(f'{program_name:#^30}')
numeric_operator = ''
sair = ''
while True:
    try:
        number_1 = float(input('Enter a number:'))
    except:
        print('Invalid character')
        continue
    try:
        number_2 = float(input('Enter another number: '))
    except:
        print('Invalid character')
        continue

    while numeric_operator not in ('+', '-', '/', '*'):
        numeric_operator = input('Enter a valid numeric operator ( +, -,/, *: ')
    if numeric_operator == '+':
        print(f'You added the number {number_1} with {number_2}, resulting in: {number_1 + number_2}')
    elif numeric_operator == '-':
        print(f'You subtracted the number {number_1} with {number_2}, resulting in {number_1 - number_2}')
    elif numeric_operator == '/':
        print(f'You divided the number {number_1} for{number_2}, resulting in {number_1 / number_2}')
    elif numeric_operator == '*':
        print(f'You multiplied the number {number_1} for {number_2}, resulting in {number_1 * number_2}')
    while sair not in ('S','N'):
        sair = str(input('Deseja sair? [S/N]')).upper()
    if sair == 'S':
        break
print('The end')
