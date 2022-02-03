#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort() No final, mostre a lista ordenada na tela.



c = 0
numbers = []
while True:
    
    n = int(input(f'Enter a valid number: '))
    if c == 0 or n > numbers[-1]:
        numbers.append(n)
        print('Number inserted in the last position! ')
        c += 1
    else:
        for key, value in enumerate(numbers):
            if n <= value:
                numbers.insert(key,n)
                print(f'Number inserted into position {key}.')
                break
    option = ' '
    while option not in 'YyNn':
        option = str(input('Would you like to continue? [Y/N] '))
    if option in 'Nn':
        break
print(numbers)
