#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 



def major_minor_pos():
    list_numbers = []
    major = minor = 0
    cont = 0
    while cont < 5:
        try:
            number = int(input(f'Enter a valid {cont + 1}:  '))
            cont += 1
        except:
            print('Invalid. Try Again!')
            continue
        list_numbers.append(number)
    for key, value in enumerate(list_numbers):
        if key == 0:
            major = minor = value
        else:
            if value > major:
                major = value
            if value < minor:
                minor = value
    for key, value in enumerate(list_numbers):
        if value == major:
            print(f'Major is {value}, whose is at position {key + 1}')
        if value == minor:
            print(f'Minor is {value}, whose is at position {key + 1} ')
    return ''

test = major_minor_pos()
print(test)
