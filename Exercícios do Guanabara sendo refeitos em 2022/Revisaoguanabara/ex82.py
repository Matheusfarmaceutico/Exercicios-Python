#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


original_list = []
while True:
    try:
        original_list.append(int(input('Enter a valid number: ')))
    except:
        print('Invalid character typed. Please, try again!')
        continue
    option = ' '
    while option not in 'YyNn':
        option = str(input('Would you like to continue? [Y/N]: '))
    if option in 'Nn':
        break
even_values = []
odd_values = []
for i, v in enumerate(original_list):
    if v % 2 == 0:
        even_values.append(v)
    elif v % 2 == 1:
        odd_values.append(v)
print(original_list)
print(even_values)
print(odd_values)