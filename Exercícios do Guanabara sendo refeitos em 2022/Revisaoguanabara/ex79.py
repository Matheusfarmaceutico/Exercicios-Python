#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

def insert_number(valid_number):
    ascending_number_in_list = []
    while True: 
        print(type(valid_number))
        if valid_number not in ascending_number_in_list:
            ascending_number_in_list.append(valid_number)
        else:
            print('It has already been entered. It will not be added.')
        option = ' '
        while option not in 'YyNn':
            option = str(input('Would you like to continue? '))
        if option in 'Nn':
            break
        else:
            valid_number = int(input('Enter a NEW valid number: '))
    return sorted(ascending_number_in_list)


ascending_list = insert_number(int((input('Enter a valid number, please: '))))
print(f'Those numbers in ascending order are: {ascending_list}')